from adafruit_ble import BLERadio
import math
#Gotten from last bit of representation of ibeacon advertisment
power = 6


known_beacons = {'<Address c2007d000052>': [3.72, 6.71], '<Address c2007d000059>': [8.54, 3.54], '<Address c2007d00009f>': [7.79, 9.97], '<Address c2007d000392>': [15.58, 5.08], '<Address c2007d00038c>': [22.12, 5.08], '<Address c2007d000097>': [30.66, 7.11], '<Address c2007d000098>': [35.13, 5.08], '<Address c2007d000064>': [37.7, 6.62], '<Address c2007d000099>': [44.95, 5.08], '<Address c2007d00038e>': [52.45, 3.14], '<Address c2007d00009d>': [56.41, 7.64], '<Address c2007d00006d>': [52.18, 13.46], 
'<Address c2007d00036f>': [43.09, 13.46], '<Address c2007d00036e>': [49.89, 16.88], '<Address c2007d000068>': [52.11, 22.56], '<Address c2007d000069>': [57.51, 18.71], '<Address c2007d00006f>': [60.11, 23.49], 
'<Address c2007d000067>': [55.84, 30.42], '<Address c2007d000076>': [48.7, 28.83], '<Address c2007d000075>': [43.35, 22.65], '<Address c2007d000370>': [39.98, 24.37], '<Address c2007d000077>': [41.68, 28.86], '<Address c2007d000078>': [31.71, 26.85], '<Address c2007d000391>': [48.65, 20.65], '<Address c2007d00008f>': [31.45, 24.16], '<Address c2007d000062>': [22.13, 28.86], '<Address c2007d00038a>': [12.65, 22.63], '<Address c2007d000061>': [15.95, 13.48], '<Address c2007d00009c>': [13.59, 10.01], '<Address c2007d00008e>': [31.49, 18.98], '<Address c2007d00006b>': [37.8, 10.21], '<Address c2007d00008d>': [43.12, 18.71], '<Address c2007d000096>': [13.0, 26.87], '<Address c2007d000063>': [19.29, 1.97], '<Address c2007d000093>': [60.11, 13.09], '<Address c2007d00006e>': [54.36, 22.48], '<Address c2007d00036a>': [54.63, 18.88], '<Address c2007d000074>': [60.11, 20.25], '<Address c2007d000072>': [60.11, 26.8], '<Address c2007d000065>': [45.3, 22.48], '<Address c2007d000071>': [48.46, 19.33], '<Address c2007d00006a>': [33.79, 24.2], '<Address c2007d00005a>': [40.15, 18.81], '<Address c2007d00005c>': [19.89, 13.98], '<Address c2007d00009b>': [17.73, 14.54], '<Address c2007d000094>': [28.63, 28.86], '<Address c2007d000095>': [12.54, 23.69], '<Address c2007d000091>': [8.46, 30.39], '<Address c2007d000092>': [1.63, 30.4], '<Address c2007d00009e>': [1.5, 23.2], '<Address c2007d000060>': [1.46, 16.99], '<Address c2007d00009a>': [8.05, 16.06], '<Address c2007d000396>': [4.68, 16.88], '<Address c2007d00005f>': [5.2, 10.13]} 
# coordinates = {
#     '<Address c2:00:7d:00:00:9d>' : [56.41,7.64], #C2
#     '<Address c2:00:7d:00:00:6b>' : [37.8,10.21] #C1
# }

# ibeacons = [{'repr': 'Advertisement(data=b"\\x1a\\xff\\x4c\\x00\\x02\\x15\\x74\\x27\\x8b\\xda\\xb6\\x44\\x45\\x20\\x8f\\x0c\\x72\\x0e\\xaf\\x05\\x99\\x35\\x27\\x11\\x4c\\xb9\\xc5\\x02\\x01\\x06")', 'tx_power': 'None', 'rssi': '-70', 'address': '<Address c2:00:7d:00:00:71>'}, {'repr': 'Advertisement(data=b"\\x1a\\xff\\x4c\\x00\\x02\\x15\\x74\\x27\\x8b\\xda\\xb6\\x44\\x45\\x20\\x8f\\x0c\\x72\\x0e\\xaf\\x05\\x99\\x35\\x27\\x11\\x4c\\xb9\\xc5\\x02\\x01\\x06")', 'tx_power': 'None', 'rssi': '-78', 'address': '<Address c2:00:7d:00:00:72>'}]
def get_ibeacon_devices(inputs):
    ble = BLERadio()
    print("scanning")
    ibeacons = []
    found= set()
    for advertisement in ble.start_scan():
        if advertisement.scan_response and addr not in scan_responses:
            scan_responses.add(addr)
        elif not advertisement.scan_response and addr not in found:
            found.add(addr)
        else:
            continue
        if advertisement.tx_power!=None:
            print(advertisement.tx_power)
            print(advertisement.complete_name)
            print("\t" + repr(advertisement))

        addr = advertisement.address
        if str(repr(advertisement)).find('xff'+chr(92)+'x4c'+chr(92)+'x00'+chr(92)+'x02'+chr(92)+'x15')!=-1 and addr not in found :
            print("\t" + repr(advertisement))
            ibeacons.append({
                'address' : str(advertisement.address),
                'tx_power':str(advertisement.tx_power),
                'rssi':str(advertisement.rssi),
                'repr':str(repr(advertisement))})
            found.add(addr)
            print(ibeacons)
           
    print("scan done")
    return ibeacons

def get_ibeacon_devices_from_list(address_list):
    ble = BLERadio()
    print("scanning")
    ibeacons = []
    found= set()
    found_beacons = 0
    for advertisement in ble.start_scan():
        addr = advertisement.address
        print(addr)
        addr = str(addr).replace(':','')
        if str(addr) in address_list:
            ibeacons.append({
                'address' : str(addr),
                'tx_power':str(advertisement.tx_power),
                'rssi':str(advertisement.rssi),
                'repr':str(repr(advertisement))})
            found.add(addr)
            print(ibeacons)
            print(repr(advertisement))
        if len(found)==2:
            break
    ble.stop_scan()
    return ibeacons


def localize_me(ibeacons):
    ranges = []
    coordinates = {}
    print(coordinates)
    for ibeacon in ibeacons: 
        current_range = math.exp(float(-0.026*(float(ibeacon['rssi'])-power)))
        ranges.append(current_range)
        #Same order
        coordinates[ibeacon['address']] = known_beacons[ibeacon['address']]
    coordinate_values = []
    print(coordinates)
    print(coordinates.keys())
    for key in coordinates.keys():
        coordinate_values.append(coordinates[key])
    U = math.sqrt(math.pow(coordinate_values[0][0]-coordinate_values[1][0],2) + math.pow(coordinate_values[0][1]-coordinate_values[1][1],2))
    x_coordinate = (math.pow(ranges[0],2) - math.pow(ranges[1],2) + math.pow(U,2))/(2*U) 
    y_coordinate = math.sqrt(abs(math.pow(ranges[0],2) - math.pow(x_coordinate,2))) 
    print(x_coordinate,y_coordinate)
    print("Localization in relation to C1 "+str(coordinate_values[0])+" being set as origin")
    return [x_coordinate,y_coordinate],coordinates
    
    
    # for beacon_address in ranges.keys():







# current_estimates = localize_me(ibeacons)
# print(current_estimates)
all_data = []
for i in range(0,3):
    ibeacons = get_ibeacon_devices_from_list(known_beacons.keys())
    current_estimates,current_beacons = localize_me(ibeacons)
    all_data.append([current_estimates,current_beacons])
print(all_data)