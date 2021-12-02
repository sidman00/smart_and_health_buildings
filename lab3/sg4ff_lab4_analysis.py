import time
import sys
import os
from blinkytape import BlinkyTape
import time
import utility as util
from datetime import datetime
from datetime import timedelta




bb = BlinkyTape('/dev/ttyACM0', 120)
# s= datetime(2021,10,28) # start datetime
# e= datetime(2021,10,29) # end datetime
# df = pd.read_csv('book_with_grids.csv')


# def get_ids():
#     grid_ids = {}
#     df = pd.read_csv('book_with_grids.csv')
#     grid_values = set(df['grid'].tolist())
#     for grid_value in grid_values:
#         grid_devices = list(set(df[df['grid']==grid_value]['device_id'].values))
#         grid_ids[grid_value] = grid_devices
#     return grid_ids

# def get_data(start_datetime, end_datetime, fields):
#     delta_days = (end_datetime-start_datetime).days
#     grid_id_values = get_ids()
#     data_point_values = {}
#     for grid in grid_id_values.keys():
#         total_data_points = 0
#         for field in fields:
#             print(grid)
#             print(field)
#             for i in range(0,delta_days):
#                 return_ldf = util.get_lfdf(field, start_datetime+timedelta(days=i), start_datetime+timedelta(days=i+1), grid_id_values.get(grid))
#                 if return_ldf is not None:
#                     total_data_points+=len(return_ldf)
#         data_point_values[grid]=(total_data_points)
#     print(data_point_values)
#     return data_point_values

#bb = BlinkyTape('COM8')

# while True:

#     for x in range(60):
#         bb.sendPixel(100, 100, 100)
#     bb.show()

#     time.sleep(.5)

#     for x in range(60):
#         bb.sendPixel(0, 0, 0)
#     bb.show()

#     time.sleep(.5)

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()
# sensor.SET_InterruptThreshold(0xff00, 0x0010)
try:
    while True:
        lux = sensor.Lux
        print('Lux: %d'%lux)
        sensor.TSL2591_SET_LuxInterrupt(50, 200)
        if float(lux)>500:
            for x in range(60):
                bb.sendPixel(100, 100, 100)
            bb.show()
        if float(lux)<500:
            for x in range(60):
                bb.sendPixel(0, 0, 0)
            bb.show()
        infrared = sensor.Read_Infrared
        print('Infrared light: %d'%infrared)
        visible = sensor.Read_Visible
        print('Visible light: %d'%visible)
        full_spectrum = sensor.Read_FullSpectrum
        print('Full spectrum (IR + visible) light: %d\r\n'%full_spectrum)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    sensor.Disable()
    exit()