import csv
import pandas as pd
import numpy as np

year = '1991'

df = pd.read_csv('../data/brfss' + year + '.csv', encoding='cp1252')
income = df['income']
race = df['race']
state = df['x.state']
age = df['x.ageg5yr']
sex = df['sex']
height = df['height']
weight = df['weight']

income_replace = {1:'<10k', 2:'10k-15k', 3:'15k-20k', 4:'20k-25k', 5:'25k-35k', 6:'35k-50k', 7:'>50k', 8:np.nan, 9:np.nan}
race_replace = {1:'white', 2:'black', 3:'hispanic', 4:'hispanic', 5:'hispanic', 6:'asian/pacific islander', 7:'native american', 8:'other/multiracial', 77:'refused/unknown', 99:'refused/unknown'}
age_replace = {1:'18-24', 2:'25-29', 3:'30-34', 4:'35-39', 5:'40-44', 6:'45-49', 7:'50-54', 8:'55-59', 9:'60-64', 10:'65-69', 11:'70-74', 12:'75-79', 13:'80+', 14:np.nan}
sex_replace = {1:'male', 2:'female'}
hw_replace = {777:np.nan, 999:np.nan}
metric = False
max_weight = 777

income = income.replace(income_replace)
race = race.replace(race_replace)
age = age.replace(age_replace)
sex = sex.replace(sex_replace)
height = height.replace(hw_replace)
weight = weight.replace(hw_replace)

height = height.tolist()
new_height = []
for row in height:
    h = str(row)

    if row < 1:
        meters = np.nan

    elif row < 712:
        feet = float(h[0])
        inches = float(h[1:])
        if inches > 12:
            meters = np.nan
        else:
            inches = inches + feet*12
            meters = inches * 0.0254

    elif row < 9999 and row >= 9000 and metric:
        meters = float(h[1])+float(h[2:])*0.01
        if meters == 0:
            meters = np.nan

    else:
        meters = np.nan

    new_height.append(meters)

weight = weight.tolist()
new_weight = []
for row in weight:
    
    if row < 10:
        kg = np.nan

    elif row < max_weight:
        kg = row * 0.453592

    elif row < 9999 and metric:
        w = str(row)
        kg = float(w[1:])
        if kg < 10:
            kg = np.nan

    else:
        kg = np.nan

    new_weight.append(kg)

bmi = []
for h, w in zip(new_height, new_weight):
    b = w/(h*h)
    if b < 10 or b > 200:
        b = np.nan
    bmi.append(b)

height = pd.Series(new_height)
weight = pd.Series(new_weight)
bmi = pd.Series(bmi)

brfss_out = pd.concat([income, race, state, age, sex, height, weight, bmi], axis=1)
brfss_out.columns = ['income', 'race', 'state', 'age', 'sex', 'height', 'weight', 'bmi']
brfss_out.to_csv('brfss'+year+'clean.csv')

