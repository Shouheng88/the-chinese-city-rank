#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import *

class Grade:
    """各项评分"""
    def __init__(self, city) -> None:
        self.city: str = city
        self.economic = None
        self.medical = None
        self.finance = None
        self.construction = None
        self.climate_and_env = None
        self.traffic = None
        self.employment = None
        self.house_pricing = None
        self.education_and_science = None
        self.total = 0

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

def read_grades() -> List[Grade]:
    """读取成绩数据"""
    with open('res/result.json', 'r', encoding="utf-8") as f:
        grade_str_list = json.load(f)
    grades: List[Grade] = []
    for grade_str_item in grade_str_list:
        grade_data = json.loads(grade_str_item)
        grade = Grade(grade_data['city'])
        grade.economic = grade_data['economic']
        grade.medical = grade_data['medical']
        grade.finance = grade_data['finance']
        grade.construction = grade_data['construction']
        grade.climate_and_env = grade_data['climate_and_env']
        grade.traffic = grade_data['traffic']
        grade.employment = grade_data['employment']
        grade.house_pricing = grade_data['house_pricing']
        grade.education_and_science = grade_data['education_and_science']
        if grade.city.endswith('省') or grade.city.endswith('自治区'):
            continue
        grades.append(grade)
    return grades
