"""India population"""
import csv
import json
from collections import defaultdict


def convert_india():
    """This function convert required data in json"""
    years_wise = defaultdict(int)

    with open("population-estimates_csv.csv", "r") as csvfile:
        population = list(csv.DictReader(csvfile, delimiter=","))

        for row in population:
            if row["Region"] == "India" and int(row["Year"]) >= 2005:
                years_wise[row["Year"]] = row["Population"]

    data = [[int(key), float(years_wise[key])] for key in years_wise]

    with open("plot_file/Names.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_india()
