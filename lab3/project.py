import pandas as pd
import utility as util
from datetime import date, datetime,timedelta
import numpy as np

#Olsson 120 | 70886B1239A5
#Olsson 005 | 70886B1238B9

olsson120_id = "70886b1239a5"
olsson005_id = "70886b1238b9"

#df = pd.read_csv('book_with_grids.csv')
#print(df[df['device_id'] == "70886b1239a5"])

#Dates of observation -- 11/16 and 11/30

s_1= datetime(2021,11,15) # start datetime
e_1= datetime(2021,11,18) # end datetime

s_2= datetime(2021,11,28) # start datetime
e_2= datetime(2021,12,1) # end datetime

s_1_lux = datetime(2021,12,5)
e_1_lux = datetime(2021,12,8)

# ldf_co2_day1_olsson120 = util.get_lfdf('co2_ppm', s_1, e_1, [olsson120_id])
# ldf_co2_day1_olssson005 = util.get_lfdf('co2_ppm', s_1, e_1, [olsson005_id])

# ldf_co2_day2_olsson120 = util.get_lfdf('co2_ppm', s_2, e_2, [olsson120_id])
ldf_co2_day1_olssson005 = util.get_lfdf('co2_ppm', s_1, e_1, [olsson005_id])
ldf_co2_day1_olsson120 = util.get_lfdf('co2_ppm', s_1, e_1, [olsson120_id])
ldf_co2_day2_olssson005 = util.get_lfdf('co2_ppm', s_2, e_2, [olsson005_id])
ldf_co2_day2_olsson120 = util.get_lfdf('co2_ppm', s_2, e_2, [olsson120_id])

ldf_lux_day1_olssson005 = util.get_lfdf('Illumination_lx', s_1, e_1, [olsson005_id])
ldf_lux_olsson120 = util.get_lfdf('Illumination_lx', s_1_lux, e_1_lux, [olsson120_id])
ldf_lux_day2_olssson005 = util.get_lfdf('Illumination_lx', s_2, e_2, [olsson005_id])

# ldf_lux_day2_olsson120 = util.get_lfdf('Illumination_lx', s_2, e_2, [olsson120_id])
# ldf_lux_day2_olssson005 = util.get_lfdf('Illumination_lx', s_2, e_2, [olsson005_id])

def filter_by_class_time(ldf,star_time,end_time):
    # filtered_ldf = pd.DataFrame()
    filtered_list = []
    for index,row in ldf.iterrows():
        if row['time'].to_pydatetime().replace(tzinfo=None) > star_time and row['time'].to_pydatetime().replace(tzinfo=None) < end_time:
            filtered_list.append(row)
    # print(filtered_list)
    return pd.DataFrame(filtered_list)

# print(ldf_co2_day1_olsson120)
# print(ldf_co2_day1_olssson005)
# print(ldf_co2_day2_olsson120)
# print(ldf_co2_day2_olssson005)

# print(ldf_lux_day2_olssson005)
# print(ldf_lux_day2_olsson120)

#Olssoon 120 8:30 to 9:20 
class_time_lux_120 = datetime(2021,12,7,8,30)
class_time1_005 = datetime(2021,11,16,13,00)
class_time2_005 = datetime(2021,11,30,13,00)
class_time1_120 = datetime(2021,11,16,8,30)
class_time2_120 = datetime(2021,11,30,8,30)
print("Lux Olsoon 120 Results")
for i in range(10,60,10):
    # print(filter_by_class_time(ldf_co2_day1_olsson120,class_time1_120,class_time1_120+timedelta(minutes=i))['value'].mean())
    print(filter_by_class_time(ldf_lux_olsson120,class_time_lux_120,class_time_lux_120+timedelta(minutes=i))['value'].mean())
print("Lux Day 1 Olssoon 005 Results")
for i in range(10,60,10):
    # print(filter_by_class_time(ldf_co2_day1_olsson120,class_time1_120,class_time1_120+timedelta(minutes=i))['value'].mean())
    print(filter_by_class_time(ldf_lux_day1_olssson005,class_time1_005,class_time1_005+timedelta(minutes=i))['value'].mean())
print("Lux Day 2 Olssoon 005 Results")
for i in range(10,60,10):
    # print(filter_by_class_time(ldf_co2_day1_olsson120,class_time1_120,class_time1_120+timedelta(minutes=i))['value'].mean())
    print(filter_by_class_time(ldf_lux_day2_olssson005,class_time2_005,class_time2_005+timedelta(minutes=i))['value'].mean())

co2_005_day_1 = filter_by_class_time(ldf_co2_day1_olssson005,class_time1_005,class_time1_005+timedelta(minutes=50))
# co2_005_day_1.to_csv('co2_005_day_1.csv',',')
co2_005_day_2 = filter_by_class_time(ldf_co2_day2_olssson005,class_time2_005,class_time2_005+timedelta(minutes=50))
# co2_005_day_2.to_csv('co2_005_day_2.csv',',')
lux_005_day_1 = filter_by_class_time(ldf_lux_day1_olssson005,class_time1_005,class_time1_005+timedelta(minutes=50))
# lux_005_day_1.to_csv('lux_005_day_1.csv',',')
lux_005_day_2 = filter_by_class_time(ldf_lux_day2_olssson005,class_time2_005,class_time2_005+timedelta(minutes=50))
# lux_005_day_2.to_csv('lux_005_day_2.csv',',')

# co2_120_day1 = filter_by_class_time(ldf_co2_day1_olsson120,class_time1_120,class_time1_120+timedelta(minutes=50))
# co2_120_day1.to_csv('co2_120_day1.csv',',')
# co2_120_day2 = filter_by_class_time(ldf_co2_day2_olsson120,class_time2_120,class_time2_120+timedelta(minutes=50))
# co2_120_day2.to_csv('co2_120_day2.csv',',')
# lux_120 = filter_by_class_time(ldf_lux_olsson120,class_time_lux_120,class_time_lux_120+timedelta(minutes=50))
# lux_120.to_csv('lux_120.csv',',')
# Olsoon 005 1:00 to 1:50 Values
# class_time1_005 = datetime(2021,11,16,13,00)
# class_time2_005 = datetime(2021,11,30,13,00)
# class_time_base_005  =  datetime(2021,11,30,9,00)
# class_time_inbetween_005 = datetime(2021,11,30,12,15)
# print("Day 1 Olsoon 005 Results")
# for i in range(10,60,10):
#     print(filter_by_class_time(ldf_co2_day1_olssson005,class_time1_005,class_time1_005+timedelta(minutes=i))['value'].mean())
# print("Day 2 Olsoon 005 Results")
# for i in range(10,60,10):
#     print(filter_by_class_time(ldf_co2_day2_olssson005,class_time2_005,class_time2_005+timedelta(minutes=i))['value'].mean())

# print("Baseline measurment")
# for i in range(10,60,10):
#     print(filter_by_class_time(ldf_co2_day2_olssson005,class_time_base_005,class_time_base_005+timedelta(minutes=i))['value'].mean())

# print("Break Measurment")
# for i in range(10,60,10):
#     print(filter_by_class_time(ldf_co2_day2_olssson005,class_time_inbetween_005,class_time_inbetween_005+timedelta(minutes=i))['value'].mean())









