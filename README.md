import csv 
from math import *
table=[]
listedu89=[]




with open('donnees_2008.csv', newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=",")
	for row in reader:
		table.append(row)
		if row[2]=='89':
			listedu89.append(row[6])
			

print(listedu89)