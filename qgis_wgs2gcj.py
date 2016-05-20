from qgis.core import QgsVectorFileWriter as QW
from coord_convert import convert


shp_path = "G:/brandon/greenway/sample/"
input_name = shp_path+"greanway-sample.shp"
vlayer = QgsVectorLayer(input_name,'shp','ogr')
input_json = shp_path+"wgs"
error=QW.writeAsVectorFormat(vlayer, input_json,'utf-8',None,'GeoJSON')
if error == QW.NoError:
    print "succeed in json conversion"
    output_json = shp_path+"gcj"
    convert(input_json+'.geojson',output_json+'.geojson')
    jlayer = QgsVectorLayer(output_json+'.geojson','json','ogr')
    output_name = shp_path+"greenway-gcj.shp"
    err_shp = QW.writeAsVectorFormat(jlayer, output_name, "utf-8", None, "ESRI Shapefile")
    if error == QW.NoError:
        print "succeed in shp conversion"
