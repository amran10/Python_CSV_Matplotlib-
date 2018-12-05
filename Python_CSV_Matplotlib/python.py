import matplotlib.pyplot as amran
import csv

x = []
y = []

with open('DPOS.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

amran.plot(x,y, label='Loaded from file!')
amran.xlabel('Tahun')
amran.ylabel('Cost')
amran.title('Procurment')
amran.legend()
amran.show()