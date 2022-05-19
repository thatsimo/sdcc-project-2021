import random
import json
from shapely.geometry import Point, shape


def add_location(boundaries_file, data_file):
    geojson_file = json.loads(open(boundaries_file).read())
    input_file = open(data_file)
    output_file = open(data_file.replace(
        ".json", "") + "_USA.json", 'w')

    poly = shape(geojson_file['features']
                     [238]['geometry'])
    min_x, min_y, max_x, max_y = poly.bounds

    for line in input_file.readlines():
        entry = json.loads(line)
        while True:
            random_point = Point(
                [random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                entry['coordinates'] = {
                    'lat': random_point.y, 'lon': random_point.x}
                print(random_point)
                break
        output_file.write(json.dumps(entry) + "\n")


add_location('land-boundaries.geojson',
             'us-presidential-tweet-id-2020-10-01-04_hydrated.json')