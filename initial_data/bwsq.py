class Squat:
    def __init__(self,squat_dict):
        self.id = squat_dict['subject']
        self.rotational_pelvic_tilt = float(squat_dict['rotational_max_pelvic_tilt'])
        self.ankle_flexion = [float(squat_dict['plantar_dorsiflexion_R_ankle']),float(squat_dict['plantar_dorsiflexion_L_ankle'])]
        self.knee_flexion = [float(squat_dict['flexion_R_Knee']),float(squat_dict['flexion_L_Knee'])]
        self.knee_adduction = [float(squat_dict['ab_ad_R_knee']),float(squat_dict['ab_ad_L_knee'])]
        self.knee_displacement = [float(squat_dict['M_L_disp_R_knee']),float(squat_dict['M_L_disp_L_knee'])]
        self.hip_flexion = [float(squat_dict['flexion_R_hip']),float(squat_dict['flexion_L_hip'])]
        self.hip_adduction = [float(squat_dict['ab_ad_R_hip']),float(squat_dict['ab_ad_L_hip'])]
        self.foot_weight = [float(squat_dict['FP2_RESULTANTMEAN_MEAN']),float(squat_dict['FP1_RESULTANTMEAN_MEAN'])]
        self.hip_power = [float(squat_dict['perc_R_HIP_POWER']), float(squat_dict['perc_L_HIP_POWER'])]
        self.knee_power = [float(squat_dict['perc_R_KNEE_POWER']), float(squat_dict['perc_L_KNEE_POWER'])]
        self.ankle_power = [float(squat_dict['perc_R_ANKLE_POWER']), float(squat_dict['perc_L_ANKLE_POWER'])]

    def get_bwsq_pairs(self):
        """
        :return: a dictionary with all data pairs
        """