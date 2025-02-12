import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

gdf1 = gpd.GeoDataFrame({
  'id': [1, 2, 3,4],
  'name': ['a', 'b', 'c','d'],
  'geometry': [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
})

gdf2 = pd.DataFrame({
  'id': [2, 3, 4, 5],
  'value': [10, 20, 30, 70]
})
outer_merged_gdf_1 = gdf1.merge(gdf2, on='id', how='outer')
outer_merged_gdf_2 = gdf1.merge(gdf2, on='id', how='outer')
print(outer_merged_gdf_1, outer_merged_gdf_2)
