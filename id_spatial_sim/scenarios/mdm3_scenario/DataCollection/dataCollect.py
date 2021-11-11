# $ python3 dataCollect.py <jsonPath> <Local authority name in quotes> <outCSVPath>

from uk_covid19 import Cov19API
import pandas as pd
import sys
import json



with open(sys.argv[1]) as f:
  extraFilters = json.load(f)

metrics = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode"
}

for x in extraFilters:
    metrics[x]=extraFilters[x]


# Location, LAD
la_only = ['areaType=ltla','areaName='+sys.argv[2]]

api = Cov19API(filters=la_only, structure=metrics)
data = api.get_csv(save_as=sys.argv[3])