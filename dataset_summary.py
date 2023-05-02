from subject import *

class DatasetSummary:
    def __init__(self,demographics_dict,rlsd_dict,rllun_dict,bwsq_dict):
        self.all_subjects = []
        for i in range(len(demographics_dict)):
            self.all_subjects.append(Subject(demographics_dict[i],rlsd_dict[i+1],rllun_dict[i+1],bwsq_dict[i+1]))
        self.subject_count = len(demographics_dict)

    def find_subject(self,id):
        """
        :param id: id (str) of subject that is being looked for
        :return: subject object
        """

    def sort_by_sex(self):
        """
        :return: 2 lists of subjects sorted by their sex (are women more asymmetrical than men)
        """

    def get_min(self):
        """
        :return: dictionary with the minimum asymmetry for each exercise and its motions
        """

    def get_max(self):
        """
        :return: dictionary with the maximum asymmetry for each exercise and its motions (can tell us where there may
        have been some issues with data capture)
        """

    def avg_demographics(self):
        """
        :return: list of average height, weight, and age values (data summary)
        """

    def avg_asymmetry(self):
        """
        :return: dictionary with the avg asymmetry for each exercise and its motions (data summary)
        """

    def sort_asymmetry(self):
        """
        :return: uses avg_asymmetry function to get dict and sorts the motion greatest to least % asymmetry (this can
        inform us about which motions are the mos problematic)
        """
