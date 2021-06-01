"""Group Bar plot for asean countries"""
import csv
import json
from collections import defaultdict


def convert_group():
    """This function convert required data in json"""
    # years = [x for x in range(2004, 2015)]
    asean = []

    with open("dataset/asean.csv", "r") as csvfile:
        read = list(csv.DictReader(csvfile, delimiter=","))
        for row in read:
            asean.append(row["Country_Name"])

    with open("population-estimates_csv.csv", "r") as csvfile:

        asean_population = []
        plots = list(csv.DictReader(csvfile, delimiter=","))
        for row in plots:
            if row["Region"] in asean and 2004 <= int(row["Year"]) <= 2014:
                asean_population.append(row)

        data_p = defaultdict(int)
        for i in asean:
            temp = []
            for row in asean_population:
                if row["Region"] == i:
                    temp.append(float(row["Population"]))
            data_p[i] = temp
        # for i in d:
        #     print(i, d[i])

    data = [{"name": i, "data": data_p[i]} for i in data_p]

    with open("plot_file/group1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_group()
