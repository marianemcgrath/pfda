import csv
FILENAME= "data.csv"
DATADIR = "Where did you put it?"
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)