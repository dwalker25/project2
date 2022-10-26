import json

# Opening JSON file
f = open('astros.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
crafts = ['ISS', 'Tiangong']
counts = []
count_ISS =  0
count_Tiangong = 0
people = data['people']
for person in people:
    if person['craft'] == 'ISS':
        count_ISS += 1
    if person['craft'] == 'Tiangong':
        count_Tiangong += 1
counts.append(count_ISS)
counts.append(count_Tiangong)

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(crafts, counts)
plt.title('# of Astronauts in Space vs. Craft')
plt.xlabel('Crafts')
plt.ylabel('# of Astronauts')
plt.savefig('astros_plot.png')
plt.show()
#save direct to file

import csv
file = open('nchs_death_causes.csv')
reader = csv.reader(file)
xss = list(reader)
'''
state_accumulator = []
count_accumulator_acc = []
count_accumulator_alz = []
for xs in xss:
    if xs[0] == '2017':
        if xs[1] == "Accidents (unintentional injuries) (V01-X59,Y85-Y86)":
            if xs[3][0] == 'A':
                state_accumulator.append(xs[3])
                count_accumulator_acc.append(int(xs[4]))
        if xs[1] == "Alzheimer's disease":
            if xs[3][0] == 'A':
                count_accumulator_alz.append(int(xs[4]))
'''

# # of accidental deaths in New York and North Dakota vs. time

accum_year = []
accum_count_ny = []
accum_count_nd = []
for xs in xss:
    if xs[1] == "Accidents (unintentional injuries) (V01-X59,Y85-Y86)":
        if xs[3] == 'New York':
            accum_year.append(int(xs[0]))
            accum_count_ny.append(int(xs[4]))
        if xs[3] == 'North Dakota':
            accum_count_nd.append(int(xs[4]))
fig, ax = plt.subplots()
plt.title('Accidental deaths in New York and North Dakota vs. Time')
plt.plot(accum_year, accum_count_ny, label = "# of Deaths in New York")
plt.plot(accum_year, accum_count_nd, label = "# of Deaths in North Dakota")
plt.xticks(np.arange(min(accum_year), max(accum_year)+1, 3.0))
plt.xlabel('Time (years)')
plt.ylabel('# of Deaths')
plt.legend()
plt.show()

'''
fig, ax = plt.subplots()
ax.bar(state_accumulator, count_accumulator_acc)
plt.title('Causes of Death in 2017: Accidents and Alzheimer\'s disease vs. states starting with the letter A')
plt.xlabel('Causes of Death')
plt.ylabel('# of Deaths')
plt.savefig('death_plots.png')
plt.show()
'''



            

