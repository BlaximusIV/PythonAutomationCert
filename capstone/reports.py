#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    """ 
    Creates the pdf report email to the supplier
    paragraph = text descriptions previously processed
    title = the report title
    attachment = the location and name of the file to be created
    """
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()

    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["BodyText"])

    report.build([report_title, report_body])



