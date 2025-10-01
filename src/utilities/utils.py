# -*- coding: utf-8 -*-
#**********************************************************************************
# content		= utils.py functions
#
# version		= 1.0.0
# date			= 26-08-2025
#
# how to		= gets imported automatically from notebooks
# dependencies	= ...
# todos         = good for now
# 
# license		= MIT
# author		= Enrico Vaccari <e.vaccari99@gmail.com>
#
# © ALL RIGHTS RESERVED
#**********************************************************************************

# -------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------

from pathlib import Path

# -------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------

def save_dataset(dataset, filename, subfolder):
    """
    Saves a DataFrame to the specified subfolder under the 'data' directory.
    Supports .xlsx, .csv, and .pkl formats. Overwrites the file if it already exists.

    Parameters:
        dataset (pd.DataFrame): The DataFrame to save.
        filename (str): The filename with extension (e.g., 'data.xlsx', 'data.csv', 'data.pkl').
        subfolder (str): Subfolder inside the 'data' directory to save the file.

    Returns:
        None
    """
    # Build the output path: <project_root>/data/<subfolder>/
    PROJECT_PATH = Path.cwd().resolve().parent
    DATA_PATH = PROJECT_PATH / "data"
    OUTPUT_DIR_PATH = DATA_PATH / subfolder
    OUTPUT_DIR_PATH.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH = OUTPUT_DIR_PATH / filename

    if filename.endswith('.xlsx'):
        dataset.to_excel(OUTPUT_PATH, index=False)
    elif filename.endswith('.csv'):
        dataset.to_csv(OUTPUT_PATH, index=False)
    elif filename.endswith('.pkl'):
        dataset.to_pickle(OUTPUT_PATH)
    else:
        raise ValueError("Unsupported file format. Use '.xlsx', '.csv', or '.pkl'.")

    print(f"File saved as: {OUTPUT_PATH}")

# -----------------------------------------------------------------