# Data Aggregate tool for Covid numbers from API site

from selenium import webdriver
from Beautifulsoup4 import Beautifulsoup4
import pandas as pd

for url in ['https://covidtracking.com/api']:
    try:
        response = request.get('https://covidtracking.com/api')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
