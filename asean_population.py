import csv
import json
import matplotlib.pyplot as plt
from collections import defaultdict


def convert_asean():
    population = []
    asean_name = []
    population_asean_2014 = defaultdict(int)

    with open("dataset/asean.csv", "r") as csvfile:
        rd = list(csv.DictReader(csvfile, delimiter=","))
        for row in rd:
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
            population_asean_2014[row["Region"]] = row["Population"]
    
    data = [[key, float(population_asean_2014[key])] for key in population_asean_2014]
    with open("plot_file/asean1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    


if __name__ == "__main__":
    convert_asean()
