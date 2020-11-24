import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def format_diagram_report(report:list):
    time = [time for time, _ in report]
    measurements = [measurement for _, measurement in report]
    pdf_name = 'report.pdf'
    with PdfPages(pdf_name) as pdf:

        plt.figure()
        plt.plot(time, measurements, color="Blue")
        plt.xlabel("Time")
        plt.ylabel("CPU Percentage Load")
        plt.title("CPU Report")
        pdf.savefig()
        plt.close()
    return pdf_name




