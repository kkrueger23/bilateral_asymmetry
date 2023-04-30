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

def percent_asymmetry(r_leg, l_leg):
    """
    :param r_leg: measure of right leg in specific motion(angle, power, moment)
    :param l_leg: measure of left leg in specific motion (angle, power, moment)
    :return: standard percent asymmetry value between the two legs (doesn't account for direction)
    """
    try:
        return 100 * (r_leg - l_leg) / ((r_leg + l_leg) / 2)
    except ZeroDivisionError:
        return ValueError

def percent_bilat_asymmetry(r_leg, l_leg):
    """
    :param r_leg: measure of right leg in specific motion(angle, power, moment)
    :param l_leg: measure of left leg in specific motion (angle, power, moment)
    :return: standard percent bilateral asymmetry value between the two legs (accounts for direction)
    """
    try:
        return 100*((max(r_leg,l_leg)-min(r_leg,l_leg))/min(r_leg,l_leg))
    except ZeroDivisionError:
        return ValueError

def percent_gait_asymmetry1(r_leg, l_leg):
    """
    :param r_leg:r_leg: measure of right leg in specific motion(angle, power, moment)
    :param l_leg: measure of left leg in specific motion (angle, power, moment)
    :return: standard percent asymmetry value between the two legs (tends to be used during gait analysis)
    """
    try:
        return 100 * (1 - ((min(r_leg, l_leg) / (max(r_leg, l_leg)))))
    except ZeroDivisionError:
        return ValueError

def percent_gait_asymmetry2(r_leg, l_leg):
    """
    :param r_leg:r_leg: measure of right leg in specific motion(angle, power, moment)
    :param l_leg: measure of left leg in specific motion (angle, power, moment)
    :return: standard percent asymmetry value between the two legs (most conservative used during gait analysis)
    """
    try:
        return 100*(abs(r_leg-l_leg))/(2*(abs(r_leg+l_leg)))
    except ZeroDivisionError:
        return ValueError

