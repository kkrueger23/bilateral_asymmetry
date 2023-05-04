from dataset_summary import *
from individual_report import *
from export_data import *


def create_report(subject,concerns_txt):
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
    subject1 = Subject(dem_dict[0], rlsd_dict[1], rllun_dict[1], bwsq_dict[1])
    subject2 = Subject(dem_dict[1], rlsd_dict[2], rllun_dict[2], bwsq_dict[2])
    subject3 = Subject(dem_dict[2], rlsd_dict[3], rllun_dict[3], bwsq_dict[3])


    # generates pdf document about subject indicating
    create_report(subject1,"concerns_74.txt")
    create_report(subject2,"concerns_75.txt")
    create_report(subject3, "concerns_75.txt")


if __name__ == "__main__":
    main()