# Install fpdf package
from fpdf import FPDF
#Install DateTime
from datetime import date



title = "Asymmetry Report and Findings"
id = '74'
today = date.today()
d4 = today.strftime("%b-%d-%Y")
class Report(FPDF):
    def header(self):
        """
        :return: Header and about for report template
        """
        # creating title
        self.set_font('Arial','B',15)
        # centering it
        w = self.get_string_width(title)+6
        self.set_x((210-w)/2)
        pdf.cell(40, 10, title)
        self.ln(10)
        # add name and date
        pdf.set_font('Arial',size=12)
        pdf.cell(0,10,'Subject ID: '+id,0,0,'L')
        pdf.cell(-40,10,'Date: '+d4,0,0,'C')
        self.ln(10)

    def about_subject(self):
        """
        :return: subject specific demographics
        """
        with open('about.txt', 'rb') as fh:
            txt = fh.read().decode()
        self.set_font('Arial',style = 'I',size=11)
        self.multi_cell(0,5,txt)
        self.ln()


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
        """
        :param concerns_txt: a text file with stated concerns from the researcher
        :return: Statements of the concerns of the researcher regarding asymmetry in movement
        """

pdf = Report()
pdf.alias_nb_pages()
pdf.add_page()
pdf.about_subject()
pdf.output('tuto1.pdf')



