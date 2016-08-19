#coding=utf-8
import json
from qgis.core import QgsVectorFileWriter as QW
from coord_convert import gcj2bd, wgs2gcj

shp_path = "G:/brandon/greenway/0819/"
inputshp = shp_path+"city.shp"
outpushp = shp_path+"city_gcj.shp"
inputjson = shp_path + "city_wgs"
outpujson = shp_path + "city_gcj"

def convert(input, output, method="wgs2gcj"):
    methods={"wgs2gcj":wgs2gcj,"gcj2bd":gcj2bd}
    with open(input, 'r') as file:
        data = file.read()
        geojson = json.loads(data)
        features = geojson['features']
        for feature in features:
            feature['geometry'] = methods[method](feature['geometry'])
        with open(output, 'w') as wfile:
            wfile.write(json.dumps(geojson))


def conversion(input_name,output_name,input_json,output_json):
    vlayer = QgsVectorLayer(input_name,'shp','ogr')
    error=QW.writeAsVectorFormat(vlayer, input_json,'utf-8',None,'GeoJSON')
    if error == QW.NoError:
        print "succeed in json conversion"
        convert(input_json+'.geojson',output_json+'.geojson')
        jlayer = QgsVectorLayer(output_json+'.geojson','json','ogr')
        err_shp = QW.writeAsVectorFormat(jlayer, output_name, "utf-8", None, "ESRI Shapefile")
        if error == QW.NoError:
            print "succeed in shp conversion"

conversion(inputshp,outpushp,inputjson,outpujson)