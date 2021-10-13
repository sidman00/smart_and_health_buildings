import utility as util
from datetime import datetime
from datetime import timedelta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from matplotlib import animation
import numpy as np

#Areas : 5,6,7,8,9,48,66

#9/22 : 10-11 am, 2:00 -3:30 pm
s= datetime(2021,9,22) # start datetime
e= datetime(2021,9,23) # end datetime
df = pd.read_csv('book_with_grids.csv')
print(df['fields'])


fig = plt.figure()
def get_ids():
    grid_ids = {}
    df = pd.read_csv('book_with_grids.csv')
    grid_values = set(df['grid'].tolist())
    for grid_value in grid_values:
        grid_devices = list(set(df[df['grid']==grid_value]['device_id'].values))
        grid_ids[grid_value] = grid_devices
    return grid_ids

def get_data(start_datetime, end_datetime, fields):
    # start_day= datetime(2021,1,1) # start datetime
    # end_day= datetime(2021,1,2) # end datetime
    delta_days = (end_datetime-start_datetime).days
    grid_id_values = get_ids()
    data_point_values = {}
    for grid in grid_id_values.keys():
        total_data_points = 0
        for field in fields:
            print(grid)
            print(field)
            for i in range(0,delta_days):
                return_ldf = util.get_lfdf(field, start_datetime+timedelta(days=i), start_datetime+timedelta(days=i+1), grid_id_values.get(grid))
                if return_ldf is not None:
                    total_data_points+=len(return_ldf)
        data_point_values.update({grid:total_data_points})
    print(data_point_values)
    return data_point_values
def get_total_data_points(data_values):
    sum = 0
    for value in data_values.values():
        sum+=value
    return sum
def get_all_fields(filename):
    field_file = open(filename,'r',encoding='UTF-8')
    all_fields = set()
    for line in field_file:
        cleaned_line = line.replace('...','').lstrip().rstrip().split(',')
        print(cleaned_line)
        for element in cleaned_line:
            if element!='':
                all_fields.add(str(element))
    return list(all_fields)

#Areas : 5,6,7,8,9,48,66
#Added area 70 to get another value in
def create_frequency_graph(data_values):
    areas_observed = [5,6,7,8,9,48,66]
    final_areas = {}
    for key in data_values.keys():
        if key in areas_observed:
            final_areas[key] = data_values.get(key)
    print(final_areas) 
    final_areas[70] = data_values.get(70)
    final_areas[45] = data_values.get(45)
    final_areas[18] = data_values.get(18)
    plt.bar(list(final_areas.keys()),list(final_areas.values()))
    plt.savefig('./assignment2_graphs/value_bar.png')
    plt.show()  
    return final_areas

def get_average_illumination_value(field,start_date,end_date,grid_value):
    grid_ids = get_ids()
    return_ldf = util.get_lfdf(field, start_date, end_date, grid_ids.get(grid_value))
    # print(return_ldf)
    return float(return_ldf['value'].mean())



#use 45 and 18, although not observed to see illumination levels close to windows versus middle of room

s_postcovid= datetime(2021,9,22) # start datetime
e_postcovid= datetime(2021,9,23) # end datetime

s_covid= datetime(2020,10,29) # start datetime
e_covid= datetime(2020,10,30) # end datetime








all_field_values = get_all_fields('field_values.txt')
print(all_field_values)
data_values = get_data(s_postcovid,e_postcovid,all_field_values)
print(get_total_data_points(data_values))
create_frequency_graph(data_values)

post_covid_mean_45 = get_average_illumination_value('Illumination_lx',s_postcovid,e_postcovid,45)

post_covid_mean_18 = get_average_illumination_value('Illumination_lx',s_postcovid,e_postcovid,18)


covid_mean_45 = get_average_illumination_value('Illumination_lx',s_covid,e_covid,45)
covid_mean_18 = get_average_illumination_value('Illumination_lx',s_covid,e_covid,18)

plt.bar(['post_covid_45','post_covid_18'],[post_covid_mean_45,post_covid_mean_18])
plt.savefig('./assignment2_graphs/post_covid.png')
plt.show()

plt.bar(['covid_45','covid_18','post_covid_45','post_covid_18'],
[covid_mean_45,covid_mean_18,post_covid_mean_45,post_covid_mean_18])
plt.savefig('./assignment2_graphs/comparsion.png')
plt.show()