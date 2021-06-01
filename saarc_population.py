"""Saarc population"""
import csv
import json
from collections import defaultdict


def convert_saarc():
    """This function convert required data in json"""
    saarc = []
    t_saarc = defaultdict(int)

    with open("dataset/saarc.csv", "r") as csvfile:
        read = list(csv.DictReader(csvfile, delimiter=","))
        for row in read:
            saarc.append(row["Country_Name"])

    with open("population-estimates_csv.csv", "r") as csvfile:
        plots = csv.DictReader(csvfile, delimiter=",")

        saarc_population = []
        for row in plots:
            if row["Region"] in saarc:
                saarc_population.append(row)

        for row in saarc_population:
            t_saarc[row["Year"]] += float(row["Population"])

    data = [
        [int(key), float(t_saarc[key])] for key in list(t_saarc.keys())[-12:]
    ]

    with open("plot_file/saarc1.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_saarc()
