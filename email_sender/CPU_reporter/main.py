from datetime import timedelta
from email_sender import send_email
from report_formatter import format_diagram_report
from report_creator import create_report


class Reporter:
    def __init__(self, creator, formatter, sender):
        self._creator = creator
        self._formatter = formatter
        self._sender = sender
        self.duration = timedelta(seconds=2)

    def send_mail(self):
        report = self._creator(self.duration)
        formatted_report = self._formatter(report)
        self._sender(formatted_report)
        print("Email sent!")


cpu_report = Reporter(create_report, format_diagram_report, send_email)
cpu_report.send.mail()
