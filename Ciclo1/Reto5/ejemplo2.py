import csv

"""""
ranking=["MUY BAJO", "BAJO", "MEDIO", "ALTO", "MUY ALTO"]
with open('GOOG.csv', newline='') as File:
    reader = csv.reader(File)
    next(File, None)
    for row in reader:
        close_value=float(row[4])
        if close_value < 1624:
            print(str(row[0]), ranking[0])
        elif close_value >= 1624 and close_value < 1854:
            print(str(row[0]), ranking[1])
        elif close_value >= 1854 and close_value < 2084:
            print(str(row[0]), ranking[2])
        elif close_value >= 1854 and close_value < 2314:
            print(str(row[0]), ranking[3])
        else:
            print(str(row[0]), ranking[4])
"""""

date_lowest_mean=""
lowest_mean =0.0
date_highest_mean=""
highest_mean=0.0

with open('GOOG.csv', newline='') as File:
    reader = csv.reader(File)
    next(File, None)
    for row in reader:
        prom_value=(float(row[2])+float(row[3]))/2
        if close_value < 1624:
            print(str(row[0]), ranking[0])
