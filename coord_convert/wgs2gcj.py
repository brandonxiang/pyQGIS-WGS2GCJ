import json
from geojson_utils import wgs2gcj


def convert(input, output):
    with open(input, 'r') as file:
        data = file.read()
        geojson = json.loads(data)
        features = geojson['features']
        for feature in features:
            feature['geometry'] = wgs2gcj(feature['geometry'])
        with open(output, 'w') as wfile:
            wfile.write(json.dumps(geojson))


if __name__ == '__main__':
    convert('../sample/greenway.geojson', '../sample/greenway_gcj.geojson')
