# Rob Hetland
# 2014-10-09
# in class demo

import numpy as np
import netCDF4
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# location of ssh data
data_url = 'http://apdrc.soest.hawaii.edu/dods/public_data/satellite_product/TOPEX/topex_weekly'

# time index to plot
tidx = -1  # plot the most recent ssh field.


########################################

m = Basemap(projection='lcc',
            llcrnrlon=-95, 
            urcrnrlon=20, 
            llcrnrlat=0, 
            urcrnrlat=60,
            lat_0=30,
            lon_0=-50,
            resolution='c')

nc = netCDF4.Dataset(data_url)

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

x, y = m(*meshgrid(lon, lat))

ssh = nc.variables['ssh'][tidx, :, :]


# plot commands
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

m.fillcontinents()

pcm = ax.pcolormesh(x, y, ssh, 
                     cmap=plt.cm.RdBu_r, 
                     vmin=-100,
                     vmax=100)
m.drawmeridians(np.arange(-120, 40, 20),
                # dashes=[1, 0],
                labels=[1,0,0,1])
m.drawparallels(np.arange(-20, 80, 20),
                # dashes=[1, 0],
                labels=[0,1,0,0])

cax = fig.add_axes([0.2, 0.57, 0.15, 0.02])
cb = plt.colorbar(pcm, cax=cax, 
                  orientation='horizontal',
                  ticks=[-100, 0, 100])
cb.set_label('Sea Surface Elevation [m]')









