import pyproj
import csv
import shapely.geometry as geom
import fiona
import fiona.crs
import shapely
import rtree
import geopandas as gpd
import numpy as np
import operator
import pandas as pd

def countLine(partID, records):
    import pyproj
    import csv
    import shapely.geometry as geom
    import fiona
    import fiona.crs
    import shapely
    import rtree
    import geopandas as gpd
    import numpy as np
    import operator
    import pandas as pd
    
    #[set dir]
    taxi = pd.read_pickle('../why_yellow_taxi/Data/df_shuffle.pkl')
    #[If necessary]
    del taxi['Unnamed: 0']
    #[set dir]
    shapefile = '../why_yellow_taxi/Buffer/entr_buffer_100_feet_epsg4269_nad83/entr_buffer_100_feet_epsg4269_nad83.shp'
    
    entr_buf = gpd.read_file(shapefile)
    entr_buf = entr_buf.to_crs(fiona.crs.from_epsg(2263))
    
    routes = ['Route_' + str(n) for n in range(1, 12)]
    entr2line = []
    for i in xrange(len(entr_buf)):
        lines = []
        for line in list(entr_buf.loc[:,routes].ix[i].dropna().values):
            try:
                line = str(int(line))
            except ValueError:
                pass
            lines.append(line)
        entr2line.append(lines)
    entr_buf['entr2line'] = entr2line
    
    index = rtree.Rtree()
    for idx, geometry in enumerate(entr_buf.geometry):
        index.insert(idx, geometry.bounds)
    
    entr_lines = {}
    proj = pyproj.Proj(init='epsg:2263', preserve_units=True)
    
    if partID==0:
        records.next()
    reader = csv.reader(records)
    
    for row in reader:
        if ((float(row[5])!=0) and float(row[9]!=0)):
            p = geom.Point(proj(float(row[5]), float(row[6])))
            d = geom.Point(proj(float(row[9]), float(row[10])))
            p_potential = index.intersection((p.x,p.y,p.x,p.y))
            d_potential = index.intersection((d.x,d.y,d.x,d.y))
            p_match = None # The first one match, should be the closest one? No!
            d_match = None
            
            for p_idx in p_potential:
                if entr_buf.geometry[p_idx].contains(p):
                    p_match = p_idx # print 'p',p_idx
                    p_lines = set(entr_buf.entr2line[p_idx])
                    break
            
            for d_idx in d_potential:
                if entr_buf.geometry[d_idx].contains(d):
                    d_match = d_idx # print 'd',d_idx
                    d_lines = set(entr_buf.entr2line[d_idx])
                    break
            
            if ((p_match and d_match) and (p_match != d_match)):
                dirct_lines = tuple(p_lines.intersection(d_lines))
                if dirct_lines:
                    entr_lines[dirct_lines] = entr_lines.get(dirct_lines, 0)+1
    return entr_lines.items()

def mapper(record):
    for key in record[0]:
        yield key, record[1]

if __name__ == '__main__':
    taxi_csv = './df_shuffle.csv'
    rdd = sc.textFile(taxi_csv)
    counts = rdd.mapPartitionsWithIndex(countLine).flatMap(mapper).reduceByKey(lambda x,y: x+y).collect()
    print counts