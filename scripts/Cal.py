#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
个性化权重计算过程
"""

from typing import *
from Grade import *

IDEAL_HOUSE_PRICING_MIN = 10000 # 理想房价的最小值
IDEAL_HOUSE_PRICING_MAX = 15000 # 理想房价的最大值
ECONOMIC_PERCENTAGE = 10 # 经济权重
MEDICAL_PERCENTAGE = 10 # 医疗权重
HOUSE_PRICING_PERCENTAGE = 10 # 房价权重
FINANCE_PERCENTAGE = 10 # 财政权重
CONSTRUCTION_PERCENTAGE = 10 # 城建权重
CLIMATE_PERCENTAGE = 10 # 气候权重
TRAFFIC_PERCENTAGE = 10 # 交通权重
EMPLOYMENT_PERCENTAGE = 10 # 就业权重
EDUCATION_PERCENTAGE = 10 # 教育权重

def _re_calculate_house_pricing_grade(grades: List[Grade]):
    """计算房价得分"""
    for grade in grades:
        if grade.house_pricing is None:
            continue
        if grade.house_pricing < IDEAL_HOUSE_PRICING_MIN:
            grade.house_pricing = 1
        elif grade.house_pricing > IDEAL_HOUSE_PRICING_MAX:
            grade.house_pricing = 0
        else:
            grade.house_pricing = (grade.house_pricing - IDEAL_HOUSE_PRICING_MIN) / (IDEAL_HOUSE_PRICING_MAX - IDEAL_HOUSE_PRICING_MIN)

def _re_calculate_total_grade(grades: List[Grade]):
    """重新计算最终房价"""
    percentages = [ECONOMIC_PERCENTAGE, MEDICAL_PERCENTAGE, HOUSE_PRICING_PERCENTAGE, FINANCE_PERCENTAGE, CONSTRUCTION_PERCENTAGE, \
                   CLIMATE_PERCENTAGE, TRAFFIC_PERCENTAGE, EMPLOYMENT_PERCENTAGE, EDUCATION_PERCENTAGE]
    for grade in grades:
        item_grades = [grade.economic, grade.medical, grade.house_pricing, grade.finance, grade.construction,\
                       grade.climate_and_env, grade.traffic, grade.employment, grade.education_and_science]
        grade_total = 0
        weight_tital = 0
        for i in range(len(item_grades)):
            item_grade = item_grades[i]
            if item_grade is not None:
                weight_tital = weight_tital + percentages[i]
                grade_total = grade_total + item_grades[i] * percentages[i]
        grade.total = grade_total / weight_tital

def _sort_by_grade(grades: List[Grade]):
    """根据总分进行排序"""
    def get_total(elem: Grade):
        return elem.total
    grades.sort(key = get_total, reverse=True) 

def _output_console_cities(city_grades: List[Grade]):
    for i in range(len(city_grades)):
        city_grade = city_grades[i]
        print('[%3d] %s 总得分[%.4f] 经济[%.2f] 医疗[%.2f] 财政[%.2f] 城建[%.2f] 气候[%.2f] 交通[%.2f] 就业[%.2f] 房价[%.2f] 科教[%.2f]' % (\
                    i+1, city_grade.city, city_grade.total,\
                    city_grade.economic if city_grade.economic is not None else -1,\
                    city_grade.medical if city_grade.medical is not None else -1,\
                    city_grade.finance if city_grade.finance is not None else -1,\
                    city_grade.construction if city_grade.construction is not None else -1,\
                    city_grade.climate_and_env if city_grade.climate_and_env is not None else -1,\
                    city_grade.traffic if city_grade.traffic is not None else -1,\
                    city_grade.employment if city_grade.employment is not None else -1,\
                    city_grade.house_pricing if city_grade.house_pricing is not None else -1,\
                    city_grade.education_and_science if city_grade.education_and_science is not None else -1))

def _output_cities_matching_house_pricing(grades: List[Grade]):
    """仅输出符合房价的城市"""
    matched_grades: List[Grade] = []
    for grade in grades:
        if grade.house_pricing is not None and grade.house_pricing > 0:
            matched_grades.append(grade)
    _output_console_cities(matched_grades)

if __name__ == "__main__":
    grades: List[Grade] = read_grades()
    _re_calculate_house_pricing_grade(grades)
    _re_calculate_total_grade(grades)
    _sort_by_grade(grades)
    _output_console_cities(grades)
    # _output_cities_matching_house_pricing(grades)
