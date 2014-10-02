
import datetime

import numpy as np

class UglyGPS(object):
    
    def __init__(self, filename):
        self.filename = filename
        
        f = open(self.filename)
        
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
        
        self.time = np.array(times)
        self.lat = np.array(latitudes)
        self.lon = np.array(longitudes)
    
    def lat_range(self):
        return self.lat.min(), self.lat.max()
    
    def __repr__(self):
        return "UglyGPS('%s')" % self.filename
    
if __name__ == '__main__':
    filename =  'ugly_gps_data1.dat'
    gps1 = UglyGPS(filename)