#plotting code : https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
#animation code : https://stackoverflow.com/questions/33742845/how-to-animate-a-seaborns-heatmap-or-correlation-matrix
import utility as util
from datetime import datetime
from datetime import timedelta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from matplotlib import animation
import numpy as np

s= datetime(2021,1,1) # start datetime
e= datetime(2021,1,2) # end datetime
df = pd.read_csv('book_with_grids.csv')

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
        data_point_values[grid]=(total_data_points)
    print(data_point_values)
    return data_point_values

def convert_to_grid(list_values):
    conversions = {}
    for value in list_values:
        conversions[value] = [int(value/20),int(value%10)]
    return conversions
        
def generate_linklab_heatmap(start_datetime, end_datetime, fields, export_filepath):
    heat_map_values = get_data(start_datetime,end_datetime,fields)
    grid_list= []
    for i in range(0,10):
        grid_list.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(len(heat_map_values))
    converted_values = convert_to_grid(heat_map_values.keys())
    X_col = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    Y_col = [0,1,2,3,4,5,6,7,8,9]
    for value in heat_map_values.keys():
        print(value)
        print([converted_values.get(value)[0],converted_values.get(value)[1]])
        grid_list[converted_values.get(value)[0]][converted_values.get(value)[1]] = heat_map_values.get(value)
    results_df = pd.DataFrame(grid_list,index=Y_col,columns=X_col)
    print(results_df)
    link_lab_heat_map = sns.heatmap(results_df, cmap ='RdYlGn', linewidths = 0.30, annot=True,zorder=2,alpha=0.5)
    link_lab_img = mpimg.imread('img/lll_grid.png') 
    link_lab_heat_map.imshow(link_lab_img,
          aspect = link_lab_heat_map.get_aspect(),
          extent = link_lab_heat_map.get_xlim() + link_lab_heat_map.get_ylim(),
          zorder = 1) #put the map under the heatmap
    # plt.savefig(export_filepath+'/heatmap.png')
    plt.show()
    return results_df
         
def init():
    plt.clf()
    sns.heatmap(np.zeros((20, 10)), vmax=.8, square=True, cbar=False)
def animate(i):
    plt.clf()
    data_frame = generate_linklab_heatmap(s,e+timedelta(days=1),['Humidity_%'],'.') 
    link_lab_heat_map = sns.heatmap(data_frame, cmap ='RdYlGn', linewidths = 0.30, annot=True,zorder=2,alpha=0.5)
    link_lab_img = mpimg.imread('img/lll_grid.png') 
    link_lab_heat_map.imshow(link_lab_img,
          aspect = link_lab_heat_map.get_aspect(),
          extent = link_lab_heat_map.get_xlim() + link_lab_heat_map.get_ylim(),
          zorder = 1) #put the map under the heatmap
    

animate_link_lab = animation.FuncAnimation(fig,animate,init_func=init,repeat=False,frames=20)
plt.show()
#Semi-functioning mostly broken animation code 

    


# generate_linklab_heatmap(s,e,['Humidity_%'],'.')






