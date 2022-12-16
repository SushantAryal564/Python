from osgeo import gdal
fn = r"D:\gdal\n27e083_to_n28e085_arc_v3.tif"
ds = gdal.Open(fn)
print("Printing Metadata")
print("Projection",ds.GetProjection())
print("six parameters",ds.GetGeoTransform())
print("colums",ds.RasterXSize)
print("rows",ds.RasterYSize)
print("Number of Bands",ds.RasterCount)

# print raster band
band1 = ds.GetRasterBand(1)
print("No data value",band1.GetNoDataValue())
print("max_value",band1.GetMaximum())
print("min_value",band1.GetMinimum())
print("data type",band1.GetUnitType())
