from osgeo import gdal
#new raster name
fn = "D:/gdal/new_raster.tif"
fn2 = "D:/gdal/n27e083_to_n28e085_arc_v3.tif"
ds = gdal.Open(fn2)
# get geotransform adn projection of existing raster
geot = ds.GetGeoTransform()
gproj = ds.GetProjection()
# get gdal driver to use for raster creation
driver_tiff = gdal.GetDriverByName("GTiff")
#Create the new raster dataset
new_ds = driver_tiff.Create(fn,xsize=ds.RasterXSize,ysize=ds.RasterYSize,bands=1,eType=gdal.GDT_Float32)
print("raster Created")
# set Geo transform
new_ds.SetGeoTransform(geot)
new_ds.SetProjection(gproj)
del(new_ds)