import matplotlib.pyplot as msi
import csv

x = []
y = []

with open('Exam.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(str(row[0]))
		y.append(int(row[1]))

msi.plot(x,y, label ='Algoritma Heuristic Miner')
msi.xlabel('Tahun')
msi.ylabel('Cost')
msi.title('Procurement of Goods and service')
msi.legend()
msi.show()