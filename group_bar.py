import csv
import json
from collections import defaultdict


def convert_group():

    years = [x for x in range(2004, 2015)]
    y1 = []
    asean = []

    with open("dataset/asean.csv", "r") as csvfile:
        rd = list(csv.DictReader(csvfile, delimiter=","))
        for row in rd:
            asean.append(row["Country_Name"])

    with open("population-estimates_csv.csv", "r") as csvfile:

        asean_population = []
        plots = list(csv.DictReader(csvfile, delimiter=","))
        for row in plots:
            if row["Region"] in asean and 2004 <= int(row["Year"]) <= 2014:
                asean_population.append(row)


        d = defaultdict(int)
        for i in asean:
            y = []
            for row in asean_population:
                if row["Region"] == i:
                    y.append(float(row["Population"]))
            d[i] = y
        # for i in d:
        #     print(i, d[i])

    data = [{'name':i, 'data':d[i]} for i in d]
    with open("plot_file/group1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_group()
