# Install fpdf package
from fpdf import FPDF

class DataReport(FPDF):
    def header(self):
        """
        :return: Header and about for report template
        """
        # creating title
        title = "Bilateral Asymmetry in Standard Rehabilitation and Strength Exercises"
        self.ln(10)
        self.set_font('Arial','B',18)
        # centering it
        self.multi_cell(0, 7, title, align='C')
        self.ln()

    def footer(self):
        # adds page number
        self.set_y(-25)
        self.set_font('Arial', 'I', 10)
        self.set_text_color(80)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    def about_study(self):
        """
        :return: subject specific demographics
        """
        # potential to add info about the study
        self.set_font('Arial', size=12)
        with open('txt_files/about_study.txt', 'rb') as fh:
            txt = fh.read().decode()
        self.set_font('Arial', style='I', size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font('Arial', style='BI', size=12)
        self.cell(0,5,"STUDY RESULTS:")
        self.ln()

    def demographics(self,dataset):
        # adds height, age, weight, and sex
        self.set_font('Arial',style='',size = 12)
        self.cell(47.5,6,('Sample Size: '+ str(dataset.subject_count()) + " (m = " + str(dataset.count_by_sex()[0]) +
                          ", f = " +  str(dataset.count_by_sex()[1])+")"), align = 'L')
        self.ln()
        self.cell(63,6,'Age: '+str(round(dataset.avg_demographics()['age'][0],2)) + ' ± '
                  +str(round(dataset.avg_demographics()['age'][1],2)),align='L')
        self.cell(63, 6, 'Height (in): ' + str(round(dataset.avg_demographics()['height'][0],2)) + ' ± '
                  +str(round(dataset.avg_demographics()['age'][1],2)),align='C')
        self.cell(63, 6, 'Weight (lbs): ' + str(round(dataset.avg_demographics()['weight'][0],2)) +' ± '
                  + str(round(dataset.avg_demographics()['age'][1], 2)), align='R')
        self.ln(10)

    def rlsd_data(self,all_data):
        """
        :return: subject specific rlsd asymmetries
        """
        # formats heading
        rlsd = all_data.final_dict_format()['rlsd']
        self.set_font('Arial',style='B',size=14)
        self.set_fill_color(203, 207, 212)
        self.cell(0,6,'STEP-DOWN ASYMMETRY',align='C',border=1,fill=True)
        self.ln()
        self.set_fill_color(252, 252, 252)
        self.set_font('Arial', style='B', size=11)
        self.cell(38,6,'',border=1)
        self.cell(38, 6, 'Average', border=1)
        self.cell(38, 6, 'St. Dev', border=1)
        self.cell(38, 6, 'Minimum', border=1)
        self.cell(38, 6, 'Maximum', border=1)
        self.ln()
        self.set_font('Arial', style='', size=11)
        # adds data
        for exercise in rlsd:
            self.cell(38,6,exercise,border=1,align='C')
            self.cell(38, 6, str(round(rlsd[exercise]['average'], 3)), border=1,align='C')
            self.cell(38, 6, str(round(rlsd[exercise]["standard deviation"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(rlsd[exercise]["minimum"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(rlsd[exercise]["maximum"], 3)), border=1, align='C')
            self.ln()
        self.ln(8)

    def bwsq_data(self,all_data):
        """
        :return: subject specific bwsq asymmetries
        """
        # formats heading
        bwsq = all_data.final_dict_format()['bwsq']
        self.set_font('Arial', style='B', size=14)
        self.set_fill_color(203, 207, 212)
        self.cell(0, 6, 'BODY-WEIGHT SQUAT ASYMMETRY', align='C', border=1, fill=True)
        self.ln()
        self.set_fill_color(252, 252, 252)
        self.set_font('Arial', style='B', size=11)
        self.cell(38, 6, '', border=1)
        self.cell(38, 6, 'Average', border=1)
        self.cell(38, 6, 'St. Dev', border=1)
        self.cell(38, 6, 'Minimum', border=1)
        self.cell(38, 6, 'Maximum', border=1)
        self.ln()
        self.set_font('Arial', style='', size=11)
        # adds data
        for exercise in bwsq:
            self.cell(38, 6, exercise, border=1, align='C')
            self.cell(38, 6, str(round(bwsq[exercise]['average'], 3)), border=1, align='C')
            self.cell(38, 6, str(round(bwsq[exercise]["standard deviation"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(bwsq[exercise]["minimum"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(bwsq[exercise]["maximum"], 3)), border=1, align='C')
            self.ln()
        self.ln(8)

    def rllun_data(self,all_data):
        """
        :return: data specific rllun asymmetries
        """
        # formats heading
        rllun = all_data.final_dict_format()['bwsq']
        self.set_font('Arial', style='B', size=14)
        self.set_fill_color(203, 207, 212)
        self.cell(0, 6, 'BODY-WEIGHT SQUAT ASYMMETRY', align='C', border=1, fill=True)
        self.ln()
        self.set_fill_color(252, 252, 252)
        self.set_font('Arial', style='B', size=11)
        self.cell(38, 6, '', border=1)
        self.cell(38, 6, 'Average', border=1)
        self.cell(38, 6, 'St. Dev', border=1)
        self.cell(38, 6, 'Minimum', border=1)
        self.cell(38, 6, 'Maximum', border=1)
        self.ln()
        self.set_font('Arial', style='', size=11)
        # adds data
        for exercise in rllun:
            self.cell(38, 6, exercise, border=1, align='C')
            self.cell(38, 6, str(round(rllun[exercise]['average'], 3)), border=1, align='C')
            self.cell(38, 6, str(round(rllun[exercise]["standard deviation"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(rllun[exercise]["minimum"], 3)), border=1, align='C')
            self.cell(38, 6, str(round(rllun[exercise]["maximum"], 3)), border=1, align='C')
            self.ln()
        self.ln(8)