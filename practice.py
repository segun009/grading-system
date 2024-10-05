# modules, inbuilt and user defined, math, random, time, 5  raise 3
# import math
# import math as m  #alias
# from math import *
from math import pi, pow, sqrt, ceil, floor
# rounding up = ceil
# rounding down = floor
# print(ceil(2.6))
# print(floor(2.6))

import random as rd

# 1 to 10 0 to 0.9 9
# print(floor(rd.random() * 10) + 1)
# print(rd.randint(3, 8))
# cars = ["benz", "bmw", "toyota", "audi"]
# # bias
# bias = [0, 4, 7, 16]
# print(rd.choices(cars, bias, k = 3))
# # print(rd.choice(cars))
# # print(rd.sample(cars, 2))

# import time
# import second
# from second import age, name, show
# # print(dir(second))
# # print(second.name)
# print(age)
# print(name)

import time as tm
#  1970 unix epub
# print(tm.time())
# year-month-day hour:min:sec

# print(tm.localtime())
# print(tm.strftime("%Y-%m-%d %H:%M:%S"))

print("hi")
tm.sleep(6)

print("we have seen you, bye")