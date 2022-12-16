from osgeo import gdal
fn = "D:/gdal/n27e083_to_n28e085_arc_v3.tif"
ds = gdal.Open(fn)
band1 = ds.GetRasterBand(1).ReadAsArray()
print(band1.shape)
print(band1.sum())
print(band1.max())
print(band1.min())
print(band1.mean())