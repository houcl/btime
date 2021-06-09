# -*- coding: utf-8 -*-
'''
@File    :   question_list.py
@Time    :   2021/06/08 14:53:16
@Author  :   houchenglong
@Version :   1.0
@Contact :   houchenglong@luojilab.com
@License :   (C)Copyright 2017-2020
@Desc    :
'''

import json


class QuestionList(object):
    def __init__(self):

        self.qa = self.get_qa()

    def get_qa(self):
        # 获取问题和答案
        data = {}
        with open("qa.txt", "r") as rf:
            for rl in rf.readlines():
                rls = rl.rstrip("\n").split("\t")
                data[rls[0]] = rls[-1].split(",")

        return data

    def main(self):

        # 本质，essence，回写答案
        for key, value in self.challenge_dict.items():
            essence = self.qa.get(key, None)
            if essence:
                if not value.get("essence", None):
                    value["essence"] = essence
                    self.challenge_dict[key] = value

        # 写文件
        self.set_challenge_map()

    def get_result(self):
        # 根据问题获取答案的流程
        data = None
        with open("q.txt", "r") as rf:
            data = rf.readlines()[0].strip()
            data_json = json.loads(data)
            questions = data_json["data"]["questions"]

            for question in questions:
                question_id = question["question_id"]
                question_title = question["title"]
                question_answer = question["answer"]

                essence = self.qa.get(question_id, None)
                if essence:
                    print(essence)


if __name__ == "__main__":
    QL = QuestionList()
    # QL.main()
    QL.get_result()
