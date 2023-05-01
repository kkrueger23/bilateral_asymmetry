from initial_data.bwsq import *
from initial_data.demographics import *
from initial_data.rllun import *
from initial_data.rlsd import *

class Subject:
    def __init__(self,demographics_dict,rlsd_dict,rllun_dict,bwsq_dict):
        self.id = demographics_dict['Subject ']
        self.demographics = Demographics(demographics_dict)
        self.rlsd = StepDown(rlsd_dict)
        self.rllun = Lunge(rllun_dict)
        self.bwsq = Squat(bwsq_dict)

    def get_asymmetry_pairs(self):
        """
        :return: a dictionary containing each motion and all associated measurements
        """
        all_motion_pairs = {}
        all_motion_pairs['rlsd'] = self.rlsd.get_rlsd_pairs()
        all_motion_pairs['bwsq'] = self.bwsq.get_bwsq_pairs()
        all_motion_pairs['rllun'] = self.rllun.get_rllun_pairs()

        return all_motion_pairs

    def calculate_asymmetry(self, asymmetry_fx):
        """
        :param asymmetry_fx: takes one of the asymmetry functions below
        :return: returns a dictionary(?) that groups by motion and then by each measurement, and calculates the asymmetry for each joint
        """
        motion_pairs = self.get_asymmetry_pairs()
        motion_asymmetry = motion_pairs.copy()
        for movement in motion_asymmetry:
            movement_dict = motion_asymmetry[movement]
            for measurement in movement_dict:
                pair = movement_dict[measurement]
                motion_asymmetry[movement][measurement] = asymmetry_fx(pair)
        return motion_asymmetry


def percent_asymmetry(motion_pair):
    """
    :param motion_pair: right and left leg measurements for a given motion
    :return: standard percent asymmetry value between the two legs (doesn't account for direction)
    """
    r_leg = motion_pair[0]
    l_leg = motion_pair[1]
    try:
        return 100 * (r_leg - l_leg) / ((r_leg + l_leg) / 2)
    except ZeroDivisionError:
        return ValueError

def percent_bilat_asymmetry(motion_pair):
    """
    :param motion_pair: right and left leg measurements for a given motion
    :return: standard percent bilateral asymmetry value between the two legs (accounts for direction)
    """
    r_leg = motion_pair[0]
    l_leg = motion_pair[1]
    try:
        return 100*((max(r_leg,l_leg)-min(r_leg,l_leg))/min(r_leg,l_leg))
    except ZeroDivisionError:
        return ValueError

def percent_gait_asymmetry1(motion_pair):
    """
    :param motion_pair: right and left leg measurements for a given motion
    :return: standard percent asymmetry value between the two legs (tends to be used during gait analysis)
    """
    r_leg = motion_pair[0]
    l_leg = motion_pair[1]
    try:
        return 100 * (1 - ((min(r_leg, l_leg) / (max(r_leg, l_leg)))))
    except ZeroDivisionError:
        return ValueError

def percent_gait_asymmetry2(motion_pair):
    """
    :param motion_pair: right and left leg measurements for a given motion
    :return: standard percent asymmetry value between the two legs (most conservative used during gait analysis)
    """
    r_leg = motion_pair[0]
    l_leg = motion_pair[1]
    try:
        return 100*(abs(r_leg-l_leg))/(2*(abs(r_leg+l_leg)))
    except ZeroDivisionError:
        return ValueError

