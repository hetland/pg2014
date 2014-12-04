# Class example for interpolating data (with missing values), and creating a netCDF file from 
# the interpolated values.

import numpy as np
from matplotlib import tri
import netCDF4

Ndatapoints = 1000
Ntimes = 20
Nbad = 200

xdata = np.random.rand(Ndatapoints)
ydata = np.random.rand(Ndatapoints)
time = np.arange(Ntimes)

# create a progressive wave
fdata = np.sin((xdata+ydata)[np.newaxis, :]*5.0 + 
               time[:, np.newaxis]/3.0)

# remove some random 'bad' data.
idx = range(fdata.size)
np.random.shuffle(idx)
fdata.flat[idx[:Nbad]] = np.nan

ygrid, xgrid = np.mgrid[0:1:60j, 0:1:50j]
fgrid = np.ma.empty((Ntimes, 60, 50), 'd')

# interpolate
for n in range(Ntimes):
    igood = ~np.isnan(fdata[n])
    t = tri.Triangulation(xdata[igood], ydata[igood])
    interp = tri.LinearTriInterpolator(t, fdata[n][igood])
    fgrid[n] = interp(xgrid, ygrid)

# create netCDF file

nc = netCDF4.Dataset('foo.nc', 'w')
nc.author = 'Hetland'

nc.createDimension('x', 50)
nc.createDimension('y', 60)
nc.createDimension('time', None)

nc.createVariable('f', 'd', ('time', 'y', 'x'))
nc.variables['f'][:] = fgrid
nc.variables['f'].units = 'meters sec-1'

nc.createVariable('x', 'd', ('x',))
nc.variables['x'][:] = xgrid[0, :]
nc.variables['x'].units = 'meters'

nc.createVariable('y', 'd', ('y',))
nc.variables['y'][:] = ygrid[:, 0]
nc.variables['y'].units = 'meters'

nc.createVariable('time', 'd', ('time',))
nc.variables['time'][:] = time
nc.variables['time'].units = 'seconds'

nc.close()




