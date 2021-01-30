#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/30 15:53 
# @File  : 11111.py
# @IDE   : PyCharm
# -------------------------------
def timeMin(time, n):
    min = time[0]
    k = 0
    for i in range(n):
        if min > time[i]:
            k = i
            min = time[i]

    time[k] = 100  #被处理的作业通过修改时长表示已被处理
    return min


def timeMax(time, n):
    max = time[0]
    for i in range(n):
        if max < time[i]:
            max=time[i]
    return max

# 多cpu多道批处理模拟
def processingTime(m, n, time):
    count = n
    if count == 0:
        return 0   #作业数为0，返回总时间0

    #作业数大于cpu数
    if n > m:
        for i in range(m):
            flag[i][2] = 0

        resultTime=0    #多道多cpu下完成所有作业所需的处理时间
        end=0   #作业全部处理结束的标志
        while end != 1:
            for i in range(m):
                if count>0:
                    # 仍有等待的作业并且有空闲的cpu，则当前cpu对作业进行处理
                    if flag[i][0] == 0:
                        flag[i][0]=1
                        flag[i][1] = timeMin(time, n)  #短作业优先
                        count -= 1  #作业数-1
            #判断是否所有cpu均空闲
            flagK=0   #标志flagK记录当前空闲的cpu数
            for i in range(m):
                if flag[i][1] == 0:
                    flagK += 1

            if flagK == m:
                end=1
                continue  # // cpu均空闲，结束的标志置1

            for i in range(m):
                if flag[i][1] > 0:
                    flag[i][1] -= 1
                if flag[i][1]==0:
                    flag[i][0] = 0
            resultTime += 1   #处理时间增加一个单位

        return resultTime
    # 作业数小于或等于cpu数，完成所有作业所需时间为最长作业时间
    else:
        return timeMax(time, n)


if __name__ == "__main__":
    time = [0]*100
    m, n = map(int, input().split())
    time = list(map(int, input().split()))

    print(processingTime(m, n, time))