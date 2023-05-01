# Install fpdf package
from fpdf import FPDF
from subject import *

class PDF_report(FPDF):
    def header(self):
        """
        :return: Header and about for report template
        """

    def about_subject(self):
        """
        :return: subject specific demographics
        """
    def rlsd_data(self):
        """
        :return: subject specific rlsd asymmetries
        """
    def bwsq_data(self):
        """
        :return: subject specific bwsq asymmetries
        """
    def rllun_data(self):
        """
        :return: subject specific rlsd asymmetries
        """

    def about_concerns(self,concerns_txt):
