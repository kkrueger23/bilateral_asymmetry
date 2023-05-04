# Install fpdf package
from fpdf import FPDF
#Install DateTime
from datetime import date
from subject import *
from initial_data.get_data import *

class Report(FPDF):
    def header(self):
        """
        :return: Header and about for report template
        """
        # creating title
        title = "Asymmetry Report and Findings"
        self.ln(10)
        self.set_font('Arial','B',18)
        # centering it
        w = self.get_string_width(title)+6
        self.set_x((210-w)/2)
        self.cell(40, 10, title)
        self.ln(10)

    def footer(self):
        # adds page number
        self.set_y(-25)
        self.set_font('Arial', 'I', 10)
        self.set_text_color(80)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    def about_subject(self,subject):
        """
        :return: subject specific demographics
        """
        # add name and date
        self.set_font('Arial', size=12)
        self.cell(0, 10, 'Subject ID: ' + subject.id, 0, 0, 'L')
        # Getting date
        today = date.today()
        d4 = today.strftime("%b-%d-%Y")
        self.cell(-40, 10, 'Date: ' + d4, 0, 0, 'C')
        self.ln(10)
        # add about study
        with open('about.txt', 'rb') as fh:
            txt = fh.read().decode()
        self.set_font('Arial',style = 'I',size=12)
        self.multi_cell(0,5,txt)
        self.ln()

    def demographics(self,subject):
        # adds height, age, weight, and sex
        self.set_font('Arial',style='',size = 12)
        self.cell(0,7,' Age: '+ str(subject.demographics.age) +
                  '                            Weight (lbs): '+str(subject.demographics.weight)+
                  '                            Height (in): '+str(subject.demographics.height)+
                  '                            Sex: '+subject.demographics.sex,'T,B',align='C')
        self.ln(15)

    def rlsd_data(self,subject):
        """
        :return: subject specific rlsd asymmetries
        """
        # formats heading
        rlsd = subject.calculate_asymmetry(percent_bilat_asymmetry)['rlsd']
        self.set_font('Arial',style='B',size=14)
        self.cell(0,6,'STEP-DOWN ASYMMETRY',align='C')
        self.ln()
        self.set_font('Arial', style='BI', size=12)
        # looks at specific measures and presents percent asymmetry
        self.cell(0, 6, 'Measures of Flexion/Extension:')
        self.ln()
        self.set_font('Arial',style='',size=11)
        self.cell(63,6,'Ankle: '+ str(round(rlsd['ankle_flexion'],4))+'%',1,align='C')
        self.cell(63,6,'Knee: ' + str(round(rlsd['knee_flexion'],4))+'%',1,align='C')
        self.cell(63, 6, 'Hip: ' + str(round(rlsd['hip_flexion'], 4)) + '%', 1,align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Measures of Power:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(63, 6, 'Ankle: ' + str(round(rlsd['ankle_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Knee: ' + str(round(rlsd['knee_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Hip: ' + str(round(rlsd['hip_power'], 4)) + '%', 1, align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Other:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(95, 6, 'Medial/Lateral Knee Displacement: ' + str(round(rlsd['knee_displacement'], 4)) + '%', 1, align='C')
        self.ln(20)

    def bwsq_data(self,subject):
        """
        :return: subject specific bwsq asymmetries
        """
        # formats heading
        bwsq = subject.calculate_asymmetry(percent_bilat_asymmetry)['bwsq']
        self.set_font('Arial',style='B',size=14)
        self.cell(0,6,'BODY-WEIGHT SQUAT ASYMMETRY',align='C')
        self.ln()
        self.set_font('Arial', style='BI', size=12)
        # looks at specific measures and presents percent asymmetry
        self.cell(0, 6, 'Measures of Flexion/Extension:')
        self.ln()
        self.set_font('Arial',style='',size=11)
        self.cell(63,6,'Ankle: '+ str(round(bwsq['ankle_flexion'],4))+'%',1,align='C')
        self.cell(63,6,'Knee: ' + str(round(bwsq['knee_flexion'],4))+'%',1,align='C')
        self.cell(63, 6, 'Hip: ' + str(round(bwsq['hip_flexion'], 4)) + '%', 1,align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Measures of Power:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(63, 6, 'Ankle: ' + str(round(bwsq['ankle_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Knee: ' + str(round(bwsq['knee_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Hip: ' + str(round(bwsq['hip_power'], 4)) + '%', 1, align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Measures of Abduction/Adduction:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(95, 6, 'Knee: ' + str(round(bwsq['knee_adduction'], 4)) + '%', 1, align='C')
        self.cell(95, 6, 'Hip: ' + str(round(bwsq['hip_adduction'], 4)) + '%', 1, align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Other:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(95, 6, 'Medial/Lateral Knee Displacement: ' + str(round(bwsq['knee_displacement'], 4)) + '%', 1,
                  align='C')
        self.cell(95, 6, 'Foot Weighting: ' + str(round(bwsq['foot_weight'], 4)) + '%', 1,
                  align='C')
        self.ln(20)

    def rllun_data(self,subject):
        """
        :return: subject specific rllun asymmetries
        """
        # formats header
        rllun = subject.calculate_asymmetry(percent_bilat_asymmetry)['rllun']
        self.set_font('Arial', style='B', size=14)
        self.cell(0, 6, 'LUNGE ASYMMETRY', align='C')
        self.ln()
        self.set_font('Arial', style='BI', size=12)

        # looks at specific measures and presents percent asymmetry
        self.cell(0, 6, 'Measures of Flexion/Extension:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(63, 6, 'Ankle: ' + str(round(rllun['ankle_flexion'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Knee: ' + str(round(rllun['knee_flexion'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Hip: ' + str(round(rllun['hip_flexion'], 4)) + '%', 1, align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Measures of Power:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(63, 6, 'Ankle: ' + str(round(rllun['ankle_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Knee: ' + str(round(rllun['knee_power'], 4)) + '%', 1, align='C')
        self.cell(63, 6, 'Hip: ' + str(round(rllun['hip_power'], 4)) + '%', 1, align='C')
        self.ln(8)
        self.set_font('Arial', style='BI', size=12)
        self.cell(0, 6, 'Other:')
        self.ln()
        self.set_font('Arial', style='', size=11)
        self.cell(95, 6, 'Medial/Lateral Knee Displacement: ' + str(round(rllun['knee_displacement'], 4)) + '%', 1,
                  align='C')
        self.cell(95, 6, 'Foot Weighting: ' + str(round(rllun['foot_weight'], 4)) + '%', 1,
                  align='C')
        self.ln(20)

    def about_concerns(self,txt_file):
        """
        :param concerns_txt: a text file with stated concerns from the researcher
        :return: Statements of the concerns of the researcher regarding asymmetry in movement
        """
        self.set_font('Arial', size=12)
        # adds paragraph about concern, but needs to be edited for each person to talk about the individual issues
        with open('concerns_header.txt', 'rb') as fh:
            txt = fh.read().decode()
        self.set_font('Arial', style='', size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        with open(file="/Users/kkrueger/desktop/Asymmetry/data/"+txt_file) as concerns_txt:
            subject_concerns = concerns_txt.read()
        self.multi_cell(0,5,subject_concerns)





