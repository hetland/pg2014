
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='lcc',
            llcrnrlon=-100, 
            urcrnrlon=-50, 
            llcrnrlat=15, 
            urcrnrlat=40,
            lat_0=25.0,
            lon_0=-75,
            resolution='i')

for x, y in m.coastpolygons:
    plt.fill(x, y, 'g')



# loads faster with no coastline info
proj = Basemap(projection='lcc',
               llcrnrlon=-100, 
               urcrnrlon=-50, 
               llcrnrlat=15, 
               urcrnrlat=40,
               lat_0=25.0,
               lon_0=-75,
               resolution=None)

