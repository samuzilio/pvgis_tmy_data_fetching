# main.py

import pandas as pd
from tqdm import tqdm
from preprocessing import VARIABLE_MAP, fetch_pvgis_tmy_data

def main():
    # Read point data from the CSV file
    df = pd.read_csv("sample_point_data.csv")

    # Prompt the user to select a variable for calculation
    while True:
        selected_variable = input(
            "Enter the variable you want to calculate the mean for (e.g., ghi, dni, dhi, etc.): "
        )
        if selected_variable in VARIABLE_MAP.values():
            break
        else:
            print("Invalid variable name! Please try again.")

    # Process point data for each row (i.e., calculate mean variable values for given set of coordinates)
    for row in tqdm(
        df.itertuples(index=False),
        total=len(df),
        desc="Processing locations",
    ):
        identifier, latitude, longitude = row.id, row.latitude, row.longitude
        data, months_selected, inputs, meta = fetch_pvgis_tmy_data(
            latitude, longitude, startyear=2010, endyear=2020 # Specify the first and the last year of the time period (the period should be >= 10 years)
        )
        variable_values = data[selected_variable]
        mean_variable_values = variable_values.mean()
        df.loc[df["id"] == identifier, f"mean_{selected_variable}"] = (
            mean_variable_values
        )

    # Store the result in a new CSV file
    df.to_csv(f"sample_point_data_with_mean_{selected_variable}.csv", index=False)

if __name__ == "__main__":
    main()
