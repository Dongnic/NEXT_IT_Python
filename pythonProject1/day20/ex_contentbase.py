import pandas as pd
import numpy as np

def cos_sim(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

def fn_sim(user, items):
    sim_list = []
    for i in items:
        sim_list.append(round(cos_sim(user, i), 3))
    return sim_list

df = pd.read_excel('./data/ITEM_MATRC.xlsx', engine='openpyxl')
user = [1, 0, 0, 0.67, 0.67, 0.67, 0.33, 0, 0.67, 0.33]
item_list = []
for i in range(len(df.index)):
    item_list.append(df.loc[i].tolist())
print(fn_sim(user, item_list))
