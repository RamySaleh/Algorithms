import sys
from time import process_time
import os
import psutil
import unittest

process = psutil.Process(os.getpid())


def profile(method, *parms):
    proc_size_start = process.memory_info().rss
    t1_start = process_time()

    res = method(parms)

    t1_stop = process_time()
    proc_size_stop = process.memory_info().rss
    elapsed = (t1_stop - t1_start) * 1000
    proc_size = abs(proc_size_stop - proc_size_start)

    print(format_bytes(proc_size))
    print(format_millisecond(elapsed))

    #unittest.main()
    return res

def start():
    proc_size_start = process.memory_info().rss
    t1_start = process_time()
    return {'siza_start' : proc_size_start , 'time_start' : t1_start}

def stop(id , start_data):
    proc_size_stop = process.memory_info().rss

    t1_stop = process_time()
    elapsed = (t1_stop - start_data['time_start']) * 1000
    proc_size = abs(proc_size_stop - start_data['siza_start'])

    print(id + ' : ' + format_millisecond(elapsed) + ' - ' + format_bytes(proc_size))


def size_of(object):
    size = sys.getsizeof(object)
    print(format_bytes(size))


def format_bytes(size):
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    power_labels = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + ' ' + power_labels[n] + 'bytes'


def format_millisecond(time):
    org = time
    second = 1000
    min = 60000

    labels = {0: 'ms', 1: 's', 2: 'm'}

    if time < second:
        time = time #* 1000
        n = 0
    elif second <= time <= min:
        time /= second
        n = 1
    else:
        time /= min
        n = 2

    return f'{str(round(time, 2))} {labels[n]}'
