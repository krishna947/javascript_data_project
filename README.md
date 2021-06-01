# Dataproject JavaScript

Data project to plot graph on web browser using JavaScipt.

## Download the required csv file
To Download the csv file click here <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">link</a>  and paste it in the  project directory .

## How to run ?
You can clone this repo and follow the steps :
#### To generate JSON files, run the command :
```bash
python3 generate_json.py
```
This command will generate the JSON files.

NOTE: After generating json file it should be in plot_file.

Next run the command :
```bash
python3 -m http.server
```
This command will start the server and also provide the link with that click on that link to visit the website.

Alternatively,
Click this <a href="">Link</a> to see the live website hosted on Heroku.





