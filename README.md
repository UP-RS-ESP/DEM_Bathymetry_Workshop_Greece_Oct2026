# INITIATE: DEM and Bathymetry Data Processing Exercise - Greece September / October 2026

Bodo Bookhagen (bodo.bookhagen@uni-potsdam.de)

The analyses require the following packages (best installed through conda or similar):
```bash
conda create -n DEMdata -c conda-forge python ipython jupyterlab numba numpy scipy cartopy pygmt geopandas xarray rioxarray scikit-learn scikit-image
conda activate DEMdata
ipython kernel install --user --name=DEMdata
pip install topotoolbox
```


The COP10 directory contains the Copernicus 10m data for two clipped areas: 
1. The eastern Corinth rift area including the city of Corinth.
2. An area on the south-eastern rift that is characterized by closed drainage basins.

![ecorinth_chi_tandemX_10m.jpg](https://github.com/UP-RS-ESP/DEM_Bathymetry_Workshop_Greece_Oct2026/blob/6c6968d20fa982bc443e4486a2e2f7aeb8d0d1a2/COP10m/ecorinth_chi_tandemX_10m.jpg)

The COP30m directory contains the entire Corinth rift area.

![DEM30m_clip.jpg](https://github.com/UP-RS-ESP/DEM_Bathymetry_Workshop_Greece_Oct2026/blob/bddc03fbfd69f407a7f8f93b3f13bf443645ae51/COP30m/DEM30m_clip.jpg)
