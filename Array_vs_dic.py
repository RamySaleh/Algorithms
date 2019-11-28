from Helpers import profiler as prof
import numpy as np

arr = np.random.randint(1000000, size=1000000)

d_arr = []
def arr_appned(parms):
    s_arr = parms[0]
    for item in s_arr:
        d_arr.append(item)
    return d_arr

dic = {}
def dic_appned(parms):
    s_arr = parms[0]
    for item in s_arr:
        dic[item] = item
    return dic

prof.profile(arr_appned, arr)
prof.size_of(d_arr)
print(len(d_arr))


prof.profile(dic_appned, arr)
prof.size_of(dic)
print(len(dic))