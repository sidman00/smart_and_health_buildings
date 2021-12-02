from adafruit_ble import BLERadio
import math
#Gotten from last bit of representation of ibeacon advertisment
power = 6

coordinates = {
    '<Address c2:00:7d:00:00:72>' : [60.11,26.8], #C2
    '<Address c2:00:7d:00:00:71>' : [48.46,19.33] #C1
}

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
    for advertisement in ble.start_scan():
        addr = advertisement.address
        print(addr)
        if str(addr) in address_list:
            ibeacons.append({
                'address' : str(advertisement.address),
                'tx_power':str(advertisement.tx_power),
                'rssi':str(advertisement.rssi),
                'repr':str(repr(advertisement))})
            found.add(addr)
            print(ibeacons)
            address_list.remove(str(addr))
            print(repr(advertisement))
        if len(address_list)==0:
            break
    return ibeacons


def localize_me(ibeacons):
    ranges = []
    for ibeacon in ibeacons: 
        current_range = math.exp(float(0.029*(power - float(ibeacon['rssi']))))
        ranges.append(current_range)
    coordinate_values = []
    for key in coordinates.keys():
        coordinate_values.append(coordinates[key])
    U = math.sqrt(math.pow(coordinate_values[0][0]-coordinate_values[1][0],2) + math.pow(coordinate_values[0][1]-coordinate_values[1][1],2))
    x_coordinate = (math.pow(ranges[0],2) - math.pow(ranges[1],2) + math.pow(U,2))/(2*U) 
    y_coordinate = math.sqrt(abs(math.pow(ranges[0],2) - math.pow(x_coordinate,2))) 
    print("Localization in relation to C1 "+str([48.46,19.33])+" being set as origin")
    return [[x_coordinate,y_coordinate],[x_coordinate,0-y_coordinate]]
    
    
    # for beacon_address in ranges.keys():


        
        



ibeacons = get_ibeacon_devices_from_list(['<Address c2:00:7d:00:00:72>','<Address c2:00:7d:00:00:71>'])
for i in range(0,5):
    print(localize_me(ibeacons))
