import csv
import json
import matplotlib.pyplot as plt
from collections import defaultdict

from numpy import TooHardError


def convert_saarc():

    saarc = []
    total_population_saarc = defaultdict(int)

    with open("dataset/saarc.csv", "r") as csvfile:
        rd = list(csv.DictReader(csvfile, delimiter=","))
        for row in rd:
            saarc.append(row["Country_Name"])

    with open("population-estimates_csv.csv", "r") as csvfile:
        plots = csv.DictReader(csvfile, delimiter=",")

        saarc_population = []
        for row in plots:
            if row["Region"] in saarc:
                saarc_population.append(row)

        for row in saarc_population:
            total_population_saarc[row["Year"]] += float(row["Population"])

    data = [[int(key), float(total_population_saarc[key])] for key in list(total_population_saarc.keys())[-12:]]
    with open("plot_file/saarc1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_saarc()
