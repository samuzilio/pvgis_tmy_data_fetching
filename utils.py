# utils.py

import pandas as pd
import requests
import io
import os

# Provide API entry point for PVGIS 5.2
URL = "https://re.jrc.ec.europa.eu/api/v5_2/"

# Rename PVGIS TMY variables to more descriptive names
VARIABLE_MAP = {
    "G(h)": "ghi",
    "Gb(n)": "dni",
    "Gd(h)": "dhi",
    "G(i)": "poa_global",
    "Gb(i)": "poa_direct",
    "Gd(i)": "poa_sky_diffuse",
    "Gr(i)": "poa_ground_diffuse",
    "H_sun": "solar_elevation",
    "T2m": "temp_air",
    "RH": "relative_humidity",
    "SP": "pressure",
    "WS10m": "wind_speed",
    "WD10m": "wind_direction",
}

# Function to fetch PVGIS TMY data
def fetch_pvgis_tmy_data(
    latitude,
    longitude,
    outputformat="csv",
    usehorizon=True, # Set to True to include effects of horizon, False to exclude
    userhorizon=None,
    startyear=None,
    endyear=None,
    map_variables=True,
    url=URL,
    timeout=30,
):
    params = {"lat": latitude, "lon": longitude, "outputformat": outputformat}
    params["usehorizon"] = int(usehorizon)
    # If `usehorizon` is set to True:
    # you can provide your own horizon information (and eventually modify this part depending on your needs)
    if os.path.isfile("sample_horizon_information.txt"):
        with open("sample_horizon_information.txt", "r") as file:
            lines = file.readlines()
            horizon_heights = []
            i = 0
            while i < len(lines):
                if lines[i].startswith("Point:") and lines[i].find(f"{latitude}, {longitude}") != -1:
                    i += 2
                    while i < len(lines) and not lines[i].startswith("Point"):
                        if not lines[i].startswith("-"):
                            data = lines[i].strip().split(",")
                            horizon_heights.append(max(0, float(data[1])))
                        i += 1
                else:
                    i += 1
        params["userhorizon"] = ",".join(map(str, horizon_heights))
    # or you can use PVGIS built-in horizon information
    else:
        params["userhorizon"] = (
            ",".join(map(str, userhorizon)) if userhorizon is not None else None
        )
    params["startyear"] = startyear
    params["endyear"] = endyear
    res = requests.get(url + "tmy", params=params, timeout=timeout)
    res.raise_for_status()
    data, months_selected, inputs, meta = None, None, None, None
    if outputformat == "csv":
        with io.BytesIO(res.content) as src:
            data, months_selected, inputs, meta = parse_fetched_pvgis_tmy_data(src)
    if map_variables:
        data = data.rename(columns=VARIABLE_MAP)
    return data, months_selected, inputs, meta

# Function to parse fetched PVGIS TMY data
def parse_fetched_pvgis_tmy_data(src):
    inputs = {}
    inputs["latitude"] = float(src.readline().split(b":")[1])
    inputs["longitude"] = float(src.readline().split(b":")[1])
    inputs["elevation"] = float(src.readline().split(b":")[1])
    src.readline()
    months_selected = [
        {"month": month + 1, "year": int(src.readline().split(b",")[1])}
        for month in range(12)
    ]
    headers = [h.decode("utf-8").strip() for h in src.readline().split(b",")]
    data = pd.DataFrame(
        [src.readline().split(b",") for _ in range(8760)], columns=headers
    )
    dtidx = pd.to_datetime(
        data["time(UTC)"].apply(lambda dt: dt.decode("utf-8")),
        format="%Y%m%d:%H%M",
        utc=True,
    )
    data = data.drop("time(UTC)", axis=1)
    data = pd.DataFrame(data, dtype=float)
    data.index = dtidx
    meta = [line.decode("utf-8").strip() for line in src.readlines()]
    return data, months_selected, inputs, meta
