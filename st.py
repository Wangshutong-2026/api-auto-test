import csv

def read_csv(path ):
    f = open("data.csv")

    # reader = csv.DictReader(f)
    reader = csv.reader(f)
    return  list(reader)[1:]