import numpy as np
import richdem as rd
import numpy as np
from scipy.ndimage import label, generate_binary_structure
from scipy.ndimage import maximum

input_dem_path = "COP30_Corinth_30m_epsg32634.tif"
output_dem_path = "COP30_Corinth_30m_epsg32634.tif_nan_sinks.tif"

# 1. Load raw DEM
dem = rd.LoadGDAL(input_dem_path)

# 2. Fully fill depressions to determine max potential spill levels
dem_filled = rd.FillDepressions(dem, epsilon=True, in_place=False)

# 3. Calculate sink depth and apply partial fill threshold
sink_depth = dem_filled - dem
# rd.rdShow(sink_depth, ignore_colours=[0], axes=False, cmap="jet", figsize=(8, 5.5))
FILL_DEPTH_LIMIT = 10.0  # Set your maximum fill depth (e.g., 5 meters)

sink_mask = sink_depth.copy()
sink_mask[sink_depth < FILL_DEPTH_LIMIT] = np.nan
sink_mask[~np.isnan(sink_mask)] = 1
sink_mask[np.isnan(sink_mask)] = 0
sink_mask = sink_mask.astype(np.bool_)

# 2. Define connectivity structure
# Use structure with 8-connectivity (includes diagonals) so diagonal sink pixels join the same label
s_structure = generate_binary_structure(rank=2, connectivity=2)

# 3. Label connected component sinks
sink_labels, num_sinks = label(sink_mask, structure=s_structure)
print(f"Identified {num_sinks} distinct connected sink components.")

max_per_component = maximum(sink_depth, labels=sink_labels, index=sink_labels)

# 2. Assign NaN where sink_depth matches its component's maximum (ignoring background 0)
is_max_pixel = (sink_labels > 0) & (sink_depth == max_per_component)
dem[is_max_pixel] = np.nan

# 7. Save corrected DEM to GeoTIFF file
rd.SaveGDAL(output_dem_path, dem)
