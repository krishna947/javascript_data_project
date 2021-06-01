"""asean population"""
import csv
import json
from collections import defaultdict


def convert_asean():
    """This function convert required data in json"""
    population = []
    asean_name = []
    asean_2014 = defaultdict(int)

    with open("dataset/asean.csv", "r") as csvfile:
        read = list(csv.DictReader(csvfile, delimiter=","))
        for row in read:
            asean_name.append(row["Country_Name"])
        # print(asean_name)

    with open("population-estimates_csv.csv", "r") as csvfile:
        plots = csv.DictReader(csvfile, delimiter=",")

        for row in plots:
            if row["Region"] in asean_name and int(row["Year"]) == 2014:
                population.append(row)

        for row in population:
            if row["Region"] == "Lao People's Democratic Republic":
                row["Region"] = "Laos"
            elif row["Region"] == "Brunei Darussalam":
                row["Region"] = "Brunei"
            elif row["Region"] == "Viet Nam":
                row["Region"] = "Vietnam"
            asean_2014[row["Region"]] = row["Population"]

    data = [[key, float(asean_2014[key])] for key in asean_2014]

    with open("plot_file/asean1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_asean()
