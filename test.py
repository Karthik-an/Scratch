import csv
import subprocess
 
with open('o.csv') as File:  
    reader = csv.reader(File)
    servers = []
    for row in reader:
        servers.append(row)
    print (servers)





#with open('in.txt', 'r') as f:
    