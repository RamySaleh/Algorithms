#https://leetcode.com/problems/exclusive-time-of-functions/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Log():
    def __init__(self,logData):
        temp = logData.split(':')
        self.fn = int(temp[0])
        self.event = temp[1]
        self.time = int(temp[2])
        self.overlapping = None

    def calTime(self, s, e):
        return s - e + 1

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def exclusiveTime(self, n, logs):
        stack = []
        res = [0 for _ in range(n)]
        s = Log(logs[0])
        stack.append(s.fn)
        time = s.time;
        for i in range(1, len(logs)):
            s = Log(logs[i])
            if time < s.time:
                res[stack[-1]] += s.time - time
                time = s.time
            if s.event == "start":
                stack.append(s.fn)
            else:
                res[stack[-1]] += 1;
                time += 1
                stack.pop()

        return res


    def test_1(self):
        self.assertEqual([3,4], self.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))

    def test_2(self):
        self.assertEqual([8], self.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))

    def test_3(self):
        self.assertEqual([7,1], self.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))