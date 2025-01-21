'''from django.contrib.gis.geos import Point, LineString  # Import the necessary types
import geopandas as gpd
from Research.models import Location

def process_and_save_geodata(file_path):
    gdf = gpd.read_file(file_path)

    for _, row in gdf.iterrows():
        geometry = row.geometry
        if geometry.is_valid:
            if isinstance(geometry, Point):
                # If it's a Point, just use its x and y coordinates
                geom = Point(geometry.x, geometry.y)
            elif isinstance(geometry, LineString):
                # For LineString, you might want to use the first point (or a centroid)
                geom = Point(geometry.coords[0])  # Get the first point of the LineString
            else:
                # Handle other geometry types (e.g., Polygon, MultiPolygon, etc.)
                print(f"Unsupported geometry type: {type(geometry)}")
                continue

            # Create and save Location object
            Location.objects.create(
                name=row.get('name', 'Unnamed'),
                geom=geom  # This will set the geometry correctly
            )
        else:
            print(f"Invalid geometry for {row.get('name', 'Unnamed')}")
'''