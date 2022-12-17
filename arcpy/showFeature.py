import os, glob, arcpy
def ListEveryFeaturesPropertiesInDirectory(myPath,extension):
    os.chdir(mypath)
    Files = glob.glob("*."+extension)
    print(Files)
    for featureClass in Files:
        desc=arcpy.Describe(featureClass)
        spatialRef= desc.spatialReference
        print(spatialRef.Name)
        print(spatialRef.falseEasting)
        print(spatialRef.falseNorting)
        print(spatialRef.type)
        print(spatialRef.semiMajorAxis)
        print(spatialRef.semiMinorAxis)
        print(desc.name)
        print (desc.catalogPath)
        print(desc.shapeType)
        print("____________________")

