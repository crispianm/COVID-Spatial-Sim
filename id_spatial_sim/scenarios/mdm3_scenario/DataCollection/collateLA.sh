#!/bin/bash
while IFS="," read -r rec_column1 rec_column2
do
   echo "Producing data for $rec_column1"
   echo python3 ./dataCollect.py ./metricsDeaths.json "$rec_column1" ./la_data/"$rec_column2"_deaths.csv
   python3 ./dataCollect.py ./metricsDeaths.json "$rec_column1" ./la_data/"$rec_column2"_deaths.csv
   echo python3 ./dataCollect.py ./metricsPillars.json "$rec_column1" ./la_data/"$rec_column2"_pillars.csv
   python3 ./dataCollect.py ./metricsPillars.json "$rec_column1" ./la_data/"$rec_column2"_pillars.csv
   echo python3 ./dataCollect.py ./metricsJabs.json "$rec_column1" ./la_data/"$rec_column2"_jabs.csv
   python3 ./dataCollect.py ./metricsJabs.json "$rec_column1" ./la_data/"$rec_column2"_jabs.csv
   echo python3 ./dataMerge.py ./la_data/ "$rec_column2" ./la_data/"$rec_column2".csv
   python3 ./dataMerge.py ./la_data/ "$rec_column2" ./la_data/"$rec_column2".csv

done < <(tail -n +2 $1)

echo python3 dataSum.py ./la_data/ $1 ./"$2".csv $2
python3 dataSum.py ./la_data/ $1 ./"$2".csv $2

