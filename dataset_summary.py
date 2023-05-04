# install statistics
from subject import *
import statistics

class DatasetSummary:
    def __init__(self,demographics_dict,rlsd_dict,rllun_dict,bwsq_dict):
        self.all_subjects = []
        for i in range(len(demographics_dict)):
            self.all_subjects.append(Subject(demographics_dict[i],rlsd_dict[i+1],rllun_dict[i+1],bwsq_dict[i+1]))
        self.subject_count = len(demographics_dict)
        self.subject_asymmetries = []
        for subject in self.all_subjects:
            self.subject_asymmetries.append(subject.calculate_asymmetry(percent_bilat_asymmetry))

    def find_subject(self,id):
        """
        :param id: id (str) of subject that is being looked for
        :return: subject object
        """
        if isinstance(id,str) is not True:
            return ValueError
        for subject in self.all_subjects:
            if subject.id == id:
                return subject
            else:
                return None

    def sort_by_sex(self):
        """
        :return: 2 lists of subjects sorted by their sex (are women more asymmetrical than men)
        """
        male_list = []
        female_list = []
        for subject in self.all_subjects:
            if subject.demographics.sex == 'M':
                male_list.append(subject)
            else:
                female_list.append(subject)
        return male_list, female_list

    def count_by_sex(self):
        """
        :return: uses sort_by_sex and counts the given list (important for summarizing data)
        """
        males, females = self.sort_by_sex()
        return [len(males), len(females)]

    def all_asymmetry_dict(self):
        """
        :return: dictionary with all participant data on an exercise-by-exercise, measure-by-measure basis (better
        format for finding average, stdev, minimum and maximum)
        """
        subjects = self.subject_asymmetries
        data_format = {"rlsd":{"ankle_flexion": [],"knee_flexion" : [],"knee_displacement": [],"hip_flexion": [],
                                  "ankle_power":[],"knee_power": [],"hip_power": []},"bwsq": {"ankle_flexion": [],"knee_flexion": [], "knee_adduction": [], "knee_displacement":[],
                                   "hip_flexion": [], "hip_adduction": [],"foot_weight": [], "ankle_power": [],
                                   "knee_power": [],"hip_power": []},"rllun": {"ankle_flexion": [],"knee_flexion":[],"knee_displacement": [],"hip_flexion":[],
                                   "ankle_power":[],"knee_power":[],"hip_power":[],"foot_weight":[]}}
        for subject in subjects:
            for exercise in subject:
                for measure in subject[exercise]:
                    if isinstance(subject[exercise][measure],float) is True:
                        data_format[exercise][measure].append(abs(subject[exercise][measure]))
        return data_format

    def get_min(self):
        """
        :return: dictionary with the minimum asymmetry for each exercise and its motions
        """
        all_data = self.all_asymmetry_dict()
        min_dict = {}
        for exercise in all_data:
            exercise_list = {}
            for motion in all_data[exercise]:
                motion_list = all_data[exercise][motion]
                exercise_list[motion] = min(motion_list)
            min_dict[exercise] = exercise_list
        return min_dict

    def get_max(self):
        """
        :return: dictionary with the maximum asymmetry for each exercise and its motions (can tell us where there may
        have been some issues with data capture)
        """
        all_data = self.all_asymmetry_dict()
        max_dict = {}
        for exercise in all_data:
            exercise_list = {}
            for motion in all_data[exercise]:
                motion_list = all_data[exercise][motion]
                exercise_list[motion] = max(motion_list)
            max_dict[exercise] = exercise_list
        return max_dict

    def avg_demographics(self):
        """
        :return: dictionary of average height, weight, and age values (data summary)
        """
        ages = []
        heights = []
        weights = []
        for subject in self.all_subjects:
            ages.append(subject.demographics.age)
            heights.append(subject.demographics.height)
            weights.append(subject.demographics.weight)
        avg_demographics = {'age':[(sum(ages)/len(ages)),statistics.stdev(ages)],
                            'height':[(sum(heights)/len(heights)),statistics.stdev(heights)],
                            'weight':[(sum(weights)/len(weights)),statistics.stdev(weights)]}
        return avg_demographics

    def avg_asymmetry(self):
        """
        :return: dictionary with the avg asymmetry for each exercise and its motions (data summary)
        """
        all_data = self.all_asymmetry_dict()
        avg_dict = {}
        for exercise in all_data:
            exercise_list = {}
            for motion in all_data[exercise]:
                motion_list = all_data[exercise][motion]
                exercise_list[motion] = (sum(motion_list)/len(motion_list))
            avg_dict[exercise] = exercise_list
        return avg_dict

    def sort_asymmetry(self):
        """
        :return: uses avg_asymmetry function to get dict and sorts the motion greatest to least % asymmetry (this can
        inform us about which motions are the most problematic)
        """
        avg_dict= self.avg_asymmetry().copy()
        sorted_dict = {}
        for exercise in avg_dict:
            ex_dict = avg_dict[exercise]
            sorted_dict[exercise] = sorted(ex_dict.items(), key = lambda x:x[1], reverse = True)
        return sorted_dict

    def st_dev_asymmeetry(self):
        """
        :return: dictionary with the standard deviation of asymmetry for each exercise and its motions (data summary)
        """
        all_data = self.all_asymmetry_dict()
        st_dev_dict = {}
        for exercise in all_data:
            exercise_list = {}
            for motion in all_data[exercise]:
                motion_list = all_data[exercise][motion]
                exercise_list[motion] = statistics.stdev(motion_list)
            st_dev_dict[exercise] = exercise_list
        return st_dev_dict

    def final_dict_format(self):
        """
        :return: collects avg, min, max, and standard deviation in a list using the same dictionary format (this can be
        used by researchers for final analysis)
        """
        all_data = self.all_asymmetry_dict()
        minimums = self.get_min()
        maximums = self.get_max()
        averages = self.avg_asymmetry()
        st_dev = self.st_dev_asymmeetry()
        final_dict = {}
        for exercise in all_data:
            exercise_list = {}
            for motion in all_data[exercise]:
                motion_dict = {'average':averages[exercise][motion],'standard deviation':st_dev[exercise][motion],
                               'minimum':minimums[exercise][motion],'maximum':maximums[exercise][motion]}
                exercise_list[motion] = motion_dict
            final_dict[exercise] = exercise_list

        return final_dict
