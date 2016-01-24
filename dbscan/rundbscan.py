import arcpy
from dbscan import *
import numpy as np
from matplotlib import pyplot as plt

# curs  = arcpy.SearchCursor("C:\Users\huangyixiu\Documents\Course\gisData\SH_hos\Hospital.shp")
curs  = arcpy.SearchCursor("../Export_Output.shp")
pointx = []
pointy = []
c = 0
for row in curs:
	pointx.append(row.Shape.firstPoint.X)
	pointy.append(row.Shape.firstPoint.Y)
	c += 1
	if c%1000 ==0:
		print "processing line %d"%c
m = np.matrix([pointx,pointy])
# 0.005 degree in wgs84, proximately 500m
eps = 0.005
min_points = 4

clusterlis = dbscan(m, eps, min_points)
res = open("../cluster2.csv","w")
res.write("x,y,clusterid\n")
for i in range(0,len(pointy)):
	res.write("%f,%f,%s\n"%(pointx[i],pointy[i],clusterlis[i]))
res.close()
print "result written done!"

