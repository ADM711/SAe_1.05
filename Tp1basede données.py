import csv
import matplotlib.pyplot as plt
table=[]
liste=[]
liste1=[]
liste2=[]
liste3=[]
liste4=[]
total2008=0
total2016=0
total2021=0
total2023=0



with open ('donnees_2008.csv',newline='') as csvfile:
     reader=csv.reader(csvfile,delimiter=',')
     for row in reader:
         table.append(row)
         table.pop(0)
         if row[2]=='89':
            liste1.append(float(row[9]))
                



total2008= sum(liste1)
print(total2008)

with open ('donnees_2016.csv',newline='') as csvfile:
     reader=csv.reader(csvfile,delimiter=',')
     for row in reader:
         table.append(row)
         table.pop(0)
         if row[2]=='89':
            liste2.append(float(row[9]))


total2016= sum(liste2)
print(total2016)
with open('donnees_2021.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)
        table.pop(0)  
        if row[1] == '89':  
            liste3.append(float(row[5]))  




total2021 = sum(liste3)
print(total2021)





with open('donnees_2023.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)
        table.pop(0) 
        if row[2] == '89':  
            liste4.append(float(row[10])) 
total2023 = sum(liste4)
print(total2023)


années = [2008, 2016, 2021, 2023]
population = [total2008, total2016, total2021, total2023]

plt.figure(figsize=(8, 6))
plt.plot(années, population, marker='o', linestyle='-', color='b')
plt.title("Évolution de la population dans l'Yonne")
plt.xlabel("Année")
plt.ylabel("Population")
plt.grid(True)

plt.show()

    
    


        

