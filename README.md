# PVGIS TMY Data Fetching
This repository contains a script to fetch [PVGIS TMY](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/pvgis-tools/pvgis-typical-meteorological-year-tmy-generator_en) data for given set of coordinates.

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
