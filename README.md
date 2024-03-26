# PVGIS TMY Data Fetching
This repository contains a script to fetch [PVGIS TMY](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/pvgis-tools/pvgis-typical-meteorological-year-tmy-generator_en) data for given set of coordinates. User can select one of the following variables and calculate its mean value over a specified time period (at least 10 years between 2005-2020):

- G(h) [W/m2] - Global horizontal irradiance
- Gb(n) [W/m2] - Direct normal irradiance
- Gd(h) [W/m2] - Diffuse horizontal irradiance
- G(i) [W/m2] - Global in-plane irradiance
- Gb(i) [W/m2] - Direct in-plane irradiance
- Gd(i) [W/m2] - Diffuse in-plane irradiance
- Gr(i) [W/m2] - Reflected in-plane irradiance
- H_sun [°] - Sun height elevation
- T2m [°C] - Air temperature at 2m
- RH [%] - Relative humidity
- SP [Pa] - Surface air pressure
- WS10m [m/s] - Wind speed at 10m
- WD10m [°] - Wind direction at 10m

> [!IMPORTANT]
> For demonstration purposes, this script uses sample point data stored in a CSV file. You can replace it with your own data (in this case make sure to have the columns `id`, `latitude` and `longitude`) or modify the script.

<br>
<br>
<br>

Follow these steps to set up and run the script on your local machine:

**1**. Clone the repository:
```
$ git clone https://github.com/samuzilio/pvgis_tmy_data_fetching.git
```
**2**. Launch your text editor;

**3**. Open the cloned repository;

**4**. Start a new terminal;

**5**. Create and activate a virtual environment:
```
$ python -m venv .venv
```
```
$ .venv\Scripts\activate (for Windows)
$ source .venv/bin/activate (for macOS and Linux)
```
**6**. Install dependencies:
```
$ pip install -r requirements.txt
```
**7**. Run the script:
```
$ python main.py
```
