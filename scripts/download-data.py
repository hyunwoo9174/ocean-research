# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:00:00 2023
===================================

Download Ocean Observing data from
the Korea Oceanographic Data Center (KODC)
and save it to a local directory.
"""

import os
from urllib import request, error
import json

# Functions to download data from KODC
def downloadData(year, key):
    """
    Get the data from KODC.
    
    Parameters
    ----------
    year: int
        The year of the data to be downloaded.
    key: str
        The OpenAPI key to access KODC SOO data.
    """
    # Define the URL for the KODC API
    url = f"https://www.nifs.go.kr/OpenAPI_json?id=sooList&key={key}&sdate={year}0101&edate={year}1231"  # JSON

    # Download the data
    try:
        response = request.urlopen(url)
        data = json.loads(response.read().decode("euc-kr"))  # Decode using EUC-KR
        # Save the data to a file
        with open(f"./data/sooList_{year}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # Ensure non-ASCII characters are preserved
        print(f"sooList_{year}.json downloaded and saved in ./data directory.")
        return data  # Return the data
    except error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def downloadCode(gru_nam, key):
    """
    Get the code from KODC.
    
    Parameters
    ----------
    gru_nam: str
        The name of the group to be downloaded.
    key: str
        The OpenAPI key to access KODC SOO data.
    """
    # Define the URL for the KODC API
    url = f"https://www.nifs.go.kr/OpenAPI_json?id=sooCode&key={key}&gru_nam={gru_nam}"  # JSON

    # Download the data
    try:
        response = request.urlopen(url)
        data = json.loads(response.read().decode("euc-kr"))  # Decode using EUC-KR
        # Save the data to a file
        with open(f"./data/sooCode_{gru_nam}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)  # Ensure non-ASCII characters are preserved
        print(f"sooCode_{gru_nam}.json downloaded and saved in ./data directory.")
        return data  # Return the data
    except error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == "__main__":
    # Load the API key from an environment variable
    key = os.getenv("KODC_API_KEY")
    # Check if the API key is provided
    if not key:
        print("Error: API key not found. Please set the KODC_API_KEY environment variable.")
        exit(1)

    # Create the directory if it doesn't exist
    os.makedirs("./data", exist_ok=True)

    # Download data for the years 1961 to 2024
    for year in range(1961, 2025):
        downloadData(year, key)
    print("All data downloaded successfully.")
    
    for element in ["E", "W", "S", "EC"]:
        downloadCode(element, key)
    print("All codes downloaded successfully.")