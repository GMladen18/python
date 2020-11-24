from datetime import timedelta
from email_sender import send_email
from report_formatter import format_diagram_report
from report_generator import generate_report


class Reporter:
    def __init__(self, generator, formatter, sender):
        self._generator = generator
        self._formatter = formatter
        self._sender = sender
        self.duration = timedelta(seconds=2)

    def send_mail(self):
        report = self._generator(self.duration)
        formatted_report = self._formatter(report)
        self._sender(formatted_report)
        print("Email sent!")


cpu_report = Reporter(generate_report, format_diagram_report, send_email)
cpu_report.send.mail()
