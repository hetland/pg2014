
import datetime

def read_ugly_gps(filename):
    f = open(filename)
    
    longitudes = []
    latitudes = []
    times = []
    
    for line in f.readlines():
        data = line.split(',')
        # $GPGGA,124628,4907.718,N,12312.802,W,2,06,1.30,5,M,,,,*29
        if (data[0] == '$GPGGA') and (len(data) == 15):
            
            hours = int(data[1][:2])
            minutes = int(data[1][2:4])
            seconds = int(data[1][4:])
            time = datetime.time(hours, minutes, seconds)
            
            lon = float(data[4])//100.0 + (float(data[4])%100.0)/60.0
            lat = float(data[2])//100.0 + (float(data[2])%100.0)/60.0
            
            times.append(time)
            longitudes.append(lon)
            latitudes.append(lat)
    
    return times, longitudes, latitudes


print __name__

if __name__ == '__main__':
    filename =  'ugly_gps_data1.dat'
    time, lon, lat = read_ugly_gps(filename)


