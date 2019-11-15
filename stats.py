import pandas as pd
import random
import numpy as np

df = pd.read_excel('salary.xlsx')
salaries = df['CompTotal'].tolist()
samples = list()

for x in range(0, 30):
    samp = list()
    for i in range(0, 5):
        samp.append(salaries.pop(random.randint(0, len(salaries) - 1)))
    samples.append(samp)

samples = np.array(samples)
samples = pd.DataFrame(samples)
samples.to_excel("samples.xlsx")

print(salaries)
print(samples)
