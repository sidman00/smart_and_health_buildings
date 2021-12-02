def get_known_beacons(beacon_file):
    beacon_file = open(beacon_file,'r')
    beacon_file.readline()
    beacon_coordinates = {

    }
    for line in beacon_file:
        parsed_line = line.replace('"','').lstrip().rstrip().split(',')
        beacon_coordinates['<Address '+str(parsed_line[0])+'>'] = [float(str(parsed_line[-3])),float(str(parsed_line[-2]))]
    beacon_file.close()
    print(beacon_coordinates)
    return beacon_coordinates
get_known_beacons('deviceList.csv')