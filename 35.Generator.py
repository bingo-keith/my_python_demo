#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SkillData:
    def __init__(self, id, name, cd, atk, costSP):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.costSP = costSP


list_skills = [
    SkillData(101, '降龙十八掌', 60, 10, 5),
    SkillData(102, '如来神掌', 50, 5, 15),
    SkillData(103, '六脉神剑', 80, 20, 8),
    SkillData(104, '一阳指', 20, 50, 15),
    SkillData(105, '九阴真经', 15, 30, 9)
]


def find_skill(target):
    for item in target:
        if item.id == 102:
            yield item


res = find_skill(list_skills)

for skill in res:
    print(skill.id, skill.name)
