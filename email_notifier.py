"""Email notifier (SMTP).

Behavior
--------
- Sends ONE email per scraper run containing every new job found (not one
  email per job - that would flood an inbox on busy runs, unlike Discord's
  per-job embeds).
- Plain smtplib + email.mime - no extra dependency. Works with Gmail (using
  an App Password: https://myaccount.google.com/apppasswords) or any other
  SMTP provider.
- Jobs are grouped by company and sorted alphabetically within each group.

Environment
-----------
- EMAIL_TO:         Required for actual delivery. Recipient address(es),
                     comma-separated.
- EMAIL_SMTP_USER:  SMTP login username (e.g. your Gmail address). Required.
- EMAIL_SMTP_PASS:  SMTP login password / app password. Required.
- EMAIL_FROM:       Sender address shown on the email. Defaults to
                     EMAIL_SMTP_USER.
- EMAIL_SMTP_HOST:  Defaults to smtp.gmail.com.
- EMAIL_SMTP_PORT:  Defaults to 587 (STARTTLS).

If EMAIL_TO, EMAIL_SMTP_USER, or EMAIL_SMTP_PASS is unset, logs what would
have been sent and returns - useful for local dry runs.
"""

from __future__ import annotations

import logging
import os
import smtplib
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html import escape
from typing import Iterable

from adapters import Job

log = logging.getLogger(__name__)

EMAIL_TO = os.environ.get("EMAIL_TO", "").strip()
SMTP_USER = os.environ.get("EMAIL_SMTP_USER", "").strip()
SMTP_PASS = os.environ.get("EMAIL_SMTP_PASS", "").strip()
EMAIL_FROM = os.environ.get("EMAIL_FROM", "").strip() or SMTP_USER
SMTP_HOST = os.environ.get("EMAIL_SMTP_HOST", "smtp.gmail.com").strip()
SMTP_PORT = int(os.environ.get("EMAIL_SMTP_PORT", "587"))

# Keep a single email readable even on a bulk/first-run dump.
MAX_LISTED = 300


def _subject(n: int) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"{n} new job posting{'s' if n != 1 else ''} - {now}"


def _text_body(jobs: list[tuple[Job, bool]]) -> str:
    lines = [f"{len(jobs)} new job postings found:\n"]
    for job, is_tech in jobs[:MAX_LISTED]:
        tag = "[TECHNICAL] " if is_tech else ""
        lines.append(
            f"- {tag}{job.title} @ {job.company} ({job.location or '—'})\n"
            f"  {job.url}"
        )
    if len(jobs) > MAX_LISTED:
        lines.append(f"\n... and {len(jobs) - MAX_LISTED} more.")
    return "\n".join(lines)


def _html_body(jobs: list[tuple[Job, bool]]) -> str:
    rows = []
    for job, is_tech in jobs[:MAX_LISTED]:
        tag = " <b>[TECHNICAL]</b>" if is_tech else ""
        title = escape(job.title or "(no title)")
        company = escape(job.company or "—")
        location = escape(job.location or "—")
        url = escape(job.url or "#")
        rows.append(
            "<tr>"
            f"<td style='padding:6px 10px;border-bottom:1px solid #eee'>{company}</td>"
            f"<td style='padding:6px 10px;border-bottom:1px solid #eee'>"
            f"<a href='{url}'>{title}</a>{tag}</td>"
            f"<td style='padding:6px 10px;border-bottom:1px solid #eee'>{location}</td>"
            "</tr>"
        )
    table = (
        "<table style='border-collapse:collapse;font-family:sans-serif;font-size:14px'>"
        "<tr>"
        "<th style='text-align:left;padding:6px 10px'>Company</th>"
        "<th style='text-align:left;padding:6px 10px'>Role</th>"
        "<th style='text-align:left;padding:6px 10px'>Location</th>"
        "</tr>" + "".join(rows) + "</table>"
    )
    footer = ""
    if len(jobs) > MAX_LISTED:
        footer = (
            f"<p>...and {len(jobs) - MAX_LISTED} more "
            "(see <code>latest_jobs.md</code> in the repo for the full list).</p>"
        )
    return f"<p>{len(jobs)} new job postings found:</p>{table}{footer}"


def _send(subject: str, text: str, html: str) -> bool:
    if not (EMAIL_TO and SMTP_USER and SMTP_PASS):
        log.info("DRY RUN (EMAIL_TO/EMAIL_SMTP_USER/EMAIL_SMTP_PASS not set): %s", subject)
        return True

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(EMAIL_FROM, [a.strip() for a in EMAIL_TO.split(",")], msg.as_string())
        return True
    except (smtplib.SMTPException, OSError) as e:
        log.error("Email send failed: %s", e)
        return False


def send_batch(new_jobs: Iterable[tuple[Job, bool]]) -> int:
    """Send one summary email for all (job, is_technical) tuples.

    Returns 1 if an email was sent (or would have been, in dry-run mode),
    else 0.
    """
    jobs = list(new_jobs)
    if not jobs:
        log.info("Email: no new jobs to notify.")
        return 0

    ok = _send(_subject(len(jobs)), _text_body(jobs), _html_body(jobs))
    if ok:
        log.info("Email: sent summary for %d new jobs.", len(jobs))
    return 1 if ok else 0
