from qgis.core import QgsVectorFileWriter as QW
from wgs2gcj import convert

def main():
    shp_path = "G:/brandon/greenway/sample/"
    shp_name = shp_path+"greanway-sample.shp"
    vlayer = QgsVectorLayer(shp_name,'origin','ogr')
    input_json = shp_path+"wgs"
    error=QW.writeAsVectorFormat(input_json,'utf-8',None,'GeoJSON')
    if error != QW.NoError:
        return
    
    print "succeed in json conversion"
    output_json = shp_path+"gcj"
    convert(input_json+'.geojson',output_json+'.geojson')
    

    