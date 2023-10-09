import csv     # imports the csv module
import sys      # imports the sys module

count = 0
sum_13th_column = 0   #e_mort_exc_tbhiv_100k

f = open('/Users/sameenrasheedi/Desktop/Lab 1 - DS/TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    print(row)
    count += 1
    if len(row) > 13 and row[13].isdigit():
            sum_13th_column += int(row[13])
print(count)
print(sum_13th_column)
avg = round(sum_13th_column / (count -1),2)
print(avg)

#%%

import matplotlib.pyplot as plt # first import library
import numpy as np

x = np.linspace(5, 15, 7)
y = np.linspace(0, 23, 7)
z = np.random.randint(-1, 1)
plt.hist(x, y)       # hist plot
#plt.plot(x, y, 'v')  # dot plot
plt.show()           # <-- shows the plot (not needed with Ipython/Spyder console)

#%%

array_1 = np.random.rand(10)
array_2 = np.random.rand(10)

#print(array_1)
diff_sqr = (array_1 - array_2) ** 2
#print(diff_sqr)
sum_of_diff_sqr = np.sum(diff_sqr)
dist = np.sqrt(sum_of_diff_sqr)

print(dist)