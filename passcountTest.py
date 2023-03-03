import pygeohash as pgh
import random
import math

# Define the range of latitudes and longitudes
min_lat, max_lat = -37.91451, -37.91450
min_lon, max_lon = 145.12731, 145.12730

# Initialize an empty hash table to keep track of duplicate geohashes
duplicate_counts = {}

def get_next_coordinate():
    # Generate a random latitude and longitude
    lat = round(random.uniform(min_lat, max_lat),6)
    lon = round(random.uniform(min_lon, max_lon),6)

    # Convert the latitude and longitude to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    return lat, lon

# Process incoming latitude and longitude coordinates
#while True:
for i in range (100):
    
    lat, lon = get_next_coordinate()  # function to get the next coordinate
    print('{}.{}'.format(lat, lon))
    geohash_val = pgh.encode(lat, lon)
    if geohash_val in duplicate_counts:
        duplicate_counts[geohash_val] += 1
    else:
        duplicate_counts[geohash_val] = 1

print(duplicate_counts)


