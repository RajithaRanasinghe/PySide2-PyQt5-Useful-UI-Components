import pygeohash as pgh
import random
import math

# Initialize variables for the previous Geohash value and its count
prev_geohash = None
prev_count = 0
lat, lon = 0, 0

# Define the range of latitudes and longitudes
min_lat, max_lat = -37.91451, -37.91450
min_lon, max_lon = 145.12731, 145.12730

# Initialize an empty hash table to keep track of duplicate geohashes
duplicate_counts = {}

def get_next_coordinate():
    # Generate a random latitude and longitude
    lat = round(random.uniform(min_lat, max_lat),6)
    lon = round(random.uniform(min_lon, max_lon),6)

    return lat, lon

lat, lon = get_next_coordinate()

# Process incoming latitude and longitude coordinates
#while True:
for i in range (10):
    if (i%3) == 0:
        #print('repeated {}'.format(pgh.encode(lat, lon)))
        pass
    else:
        lat, lon = get_next_coordinate()
    
    #print('{}.{}'.format(lat, lon))
    print('geohash {}'.format(pgh.encode(lat, lon)))

    geohash_val = pgh.encode(lat, lon)
    if geohash_val != prev_geohash:
        if geohash_val in duplicate_counts:
            duplicate_counts[geohash_val] += 1
        else:
            duplicate_counts[geohash_val] = 1
    else:
        if geohash_val in duplicate_counts:
            pass
        else:
            duplicate_counts[geohash_val] = 1

    prev_geohash = geohash_val

print(duplicate_counts)


