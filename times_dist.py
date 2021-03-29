from selenium import webdriver
import pandas as pd
from datetime import date, time, datetime, timedelta
import random as rd
import ctypes

def times(url, cap):
    total_access = round(cap * 100 / 35)
    print(total_access)
    minutes_amount = 24 * 60
    start = datetime.combine(date.today(), time(0, 0))
    minutes = []
    break_point = 0
    for i in range(minutes_amount):
        minutes.append(start)
        start += timedelta(minutes=1)
        if datetime.combine(date.today(), time(0, 0)) > start:
            break_point = i

    # ## ORIGINAL DISTRIBUTION
    # dist = {
    #     1: 0.04,  # %5 0,085
    #     2: 0.02,  # %2 0,105
    #     3: 0.11,  # %10  0,015
    #     4: 0.125,  # %10 0
    #     5: 0.175,  # %10
    #     6: 0.20,  # %20
    #     7: 0.195,  # %43
    #     8: 0.135  # %10 0,01
    # }

    dist = {
        1: 0,  # %5 0,085
        2: 0,  # %2 0,105
        3: 0,  # %10  0,015
        4: 0,  # %10 0
        5: 1,  # %10
        6: 0,  # %20
        7: 0,  # %43
        8: 0  # %10 0,01
    }


    probs = []
    quarter = 0
    filtered_cum_prob = 0
    for i in range(minutes_amount):
        if i % (minutes_amount / 8) == 0:
            quarter += 1

        cum_prob = dist[quarter]
        if i < break_point:
            filtered_cum_prob += cum_prob / (minutes_amount / 8)
            cum_prob = 0
        x = cum_prob / (minutes_amount / 8)
        probs.append(x)

    remaining_minutes = minutes_amount - break_point
    distributed_cum_prob = filtered_cum_prob / remaining_minutes
    new_probs = list(map(lambda x: x + distributed_cum_prob if x != 0 else 0, probs))

    distributed_time_table = rd.choices(minutes, weights=new_probs, k=total_access)
    time_table = [[i, url] for i in distributed_time_table]

    dist = {
        1: 0.1,  # %5
        2: 0.1,  # %2
        3: 0.1,  # %10
        4: 0.1,  # %10
        5: 0.1,  # %10
        6: 0.1,  # %20
        7: 0.1,  # %43
        8: 0.1,  # %10
        9: 0.1,
        10: 0.1,
    }
    probs = []
    quarter = 0
    for i in range(len(time_table)):
        if i % (round(len(time_table) / 10)) == 0:
            quarter += 1
        cum_prob = dist[quarter]
        x = cum_prob / (minutes_amount / 10)
        probs.append(x)

    distributed_ones = rd.choices(time_table, weights=probs, k=cap)
    new_distributed = []
    for i in time_table:
        if i in distributed_ones:
            i.append(1)
        else:
            i.append(0)
        new_distributed.append(i)

    return new_distributed
