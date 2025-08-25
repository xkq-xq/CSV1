import csv 
csvFile = open("1.csv","r")
reader = csv.reader(csvFile)
a = list(reader)
for i in a:
    print(i)