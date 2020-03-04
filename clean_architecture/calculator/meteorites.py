from typing import (List, Dict, Tuple, Optional)
import requests
import json
import calculator.calc as calc

URL = ("https://data.nasa.gov/resource/y77d-th95.json")


class MeteoriteStats:
    """Class to retrieve meteorite data and calculate the average 
    meteorite mass, while trimming the outliers"""
    def get_data(self):
        return requests.get(URL).json()

    def average_mass(self, data):
        c = calc.Calc()
        masses = [float(d.get("mass")) for d in data if 'mass' in d]
        return c.avg(masses)
