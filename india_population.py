import csv
import json
import matplotlib.pyplot as plt
from collections import defaultdict


def convert_india():
    population_years_wise = defaultdict(int)

    with open("population-estimates_csv.csv", "r") as csvfile:
        population = list(csv.DictReader(csvfile, delimiter=","))

        for row in population:
            if row["Region"] == "India" and int(row['Year'])>=2005:
                population_years_wise[row["Year"]] = row["Population"]
                
    
    data = [[int(key), float(population_years_wise[key])] for key in population_years_wise]
    with open("plot_file/Names.json", "w") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    convert_india()
