from dataset_summary import *
from individual_report import *
from dataset_report import *
from export_data import *
from initial_data.get_data import *


def create_individual_report(subject,concerns_txt):
    pdf = Report()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.about_subject(subject)
    pdf.demographics(subject)
    pdf.rlsd_data(subject)
    pdf.bwsq_data(subject)
    pdf.rllun_data(subject)
    pdf.add_page()
    pdf.about_concerns(concerns_txt)
    pdf.output('sub_'+subject.id+'.pdf')

def create_all_data_report(all_data,name):
    pdf = DataReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.demographics(all_data)
    pdf.rlsd_data(all_data)
    pdf.bwsq_data(all_data)
    pdf.rllun_data(all_data)
    pdf.output(name + '.pdf')

def main():
    # gets xlsx data
    dem_dict = get_dict_data('Demographics.xlsx', 'Demographics')
    rlsd_dict = get_dict_data('rlsd.xlsx', 'rlsd_data')
    bwsq_dict = get_dict_data('bwsq.xlsx', 'bwsq_data')
    rllun_dict = get_dict_data('rllun.xlsx', 'rllun_data')

    # Creates data set object with all available data
    all_data = DatasetSummary(dem_dict, rlsd_dict, rllun_dict, bwsq_dict)

    # Exports 3 csv files (one per exercise) that can be used for further analysis
    export_data(all_data)

    #creates a subject object
    subject1 = all_data.find_subject("74")
    subject2 = all_data.find_subject("75")

    # generates pdf document about subject indicating
    create_individual_report(subject1,"concerns_74.txt")
    create_individual_report(subject2, "concerns_75.txt")

    # creates additional data objects (male and female)
    male_participants,female_participants = all_data.sort_by_sex()

    male_data = DatasetSummary(dem_dict, rlsd_dict, rllun_dict, bwsq_dict)
    for subject in male_data.all_subjects:
        if subject not in male_participants:
            male_data.all_subjects.remove(subject)

    female_data = DatasetSummary(dem_dict, rlsd_dict, rllun_dict, bwsq_dict)
    for subject in female_data.all_subjects:
        if subject not in female_participants:
            female_data.all_subjects.remove(subject)

    # generates pdf document summarizing the findings of a full dataset
    create_all_data_report(all_data, 'all_subject')
    create_all_data_report(male_data,'males')
    create_all_data_report(female_data, 'females')


if __name__ == "__main__":
    main()