import csv
import pandas as pd
import numpy as np

year = '2014'

df = pd.read_csv('../data/brfss' + year + '.csv', encoding='cp1252')

income = df['income2']
race = df['x.race']
state = df['x.state']
age = df['x.ageg5yr']
sex = df['sex']
height = df['height3']
weight = df['weight2']
general_health = df['genhlth']
# physical_health = df['physhlth']
# mental_health = df['menthlth']
doctor = df['persdoc2']
medical_costs = df['medcost']
checkup = df['checkup1']
exercise = df['exerany2']
sleep = df['sleptim1']
# heart_attack = df['cvdinfr4']
# heart_disease = df['cvdcrhd4']
# stroke = df['cvdstrk3']
# asthma = df['asthma3']
# depression = df['addepev2']
marital = df['marital']
education = df['educa']
smoking = df['smokday2']
alcohol = df['alcday5']
diabetes = df['diabete3']

income_replace = {1:'<10k', 2:'10k-15k', 3:'15k-20k', 4:'20k-25k', 5:'25k-35k', 6:'35k-50k', 7:'50k-75k', 8:'>75k', 77:'35k-50k', 99:'35k-50k'}
race_replace = {1:'white', 2:'black', 3:'native american', 4:'asian/pacific islander', 5:'asian/pacific islander', 6:'other/multiracial', 7:'other/multiracial', 8:'hispanic', 9:np.nan}
age_replace = {1:'18-24', 2:'25-29', 3:'30-34', 4:'35-39', 5:'40-44', 6:'45-49', 7:'50-54', 8:'55-59', 9:'60-64', 10:'65-69', 11:'70-74', 12:'75-79', 13:'80+', 14:np.nan}
sex_replace = {1:'male', 2:'female'}
hw_replace = {7777:np.nan, 9999:np.nan}
metric = True
max_weight = 999
general_health_replace = {1:'excellent', 2:'very good', 3:'good', 4:'fair', 5:'poor', 7:np.nan, 9:np.nan}
# physical_health_replace = {88: 0, 77: np.nan, 99: np.nan}
# mental_health_replace = {88: 0, 77: np.nan, 99: np.nan}
doctor_replace = {1:'yes', 2:'yes', 3:'no', 7:np.nan, 9:np.nan}
medical_costs_replace = {1:'yes', 2:'no', 7:np.nan, 9:np.nan}
checkup_replace = {1:'1 year', 2:'2 years', 3:'5 years', 4:'>5 years', 7:'unknown', 8:'never', 9:np.nan}
exercise_replace = {1:'yes', 2:'no', 7:np.nan, 9:np.nan}
sleep_replace = {1:'1-3', 2:'1-3', 3:'1-3', 4:'4-6', 5:'4-6', 6:'4-6', 7:'7-8', 8:'7-8', 9:'9-10', 10:'9-10', 11:'11-12', 12:'11-12', 13:'>12', 14:'>12', 15:'>12', 16:'>12', 17:'>12', 18:'>12', 19:'>12', 20:'>12', 21:'>12', 22:'>12', 23:'>12', 24:'>12', 77:'7-8', 99:'7-8'}
marital_replace = {1:'married', 2:'divorced', 3:'widowed', 4:'separated', 5:'single', 6:'living together', 9:np.nan}
education_replace = {1:'none', 2:'1-8', 3:'9-11', 4:'12/ged', 5:'c1-3', 6:'cg', 9:np.nan}
smoking_replace = {1:'yes', 2:'yes', 3:'no', 7:np.nan, 9:np.nan}
alcohol_replace = {777:'yes', 888:'no', 999:'no'}
diabetes_replace = {1:'yes', 2:'yes', 3:'no', 4:'yes', 7:np.nan, 9:np.nan}

income = income.replace(income_replace)
income = income.fillna('35k-50k')
race = race.replace(race_replace) #drop na
age = age.replace(age_replace) #drop na
sex = sex.replace(sex_replace)
height = height.replace(hw_replace)
weight = weight.replace(hw_replace)
general_health = general_health.replace(general_health_replace) #drop na
# physical_health = physical_health.replace(physical_health_replace) #drop na
# mental_health = mental_health.replace(mental_health_replace) #drop na
doctor = doctor.replace(doctor_replace) #drop na
medical_costs = medical_costs.replace(medical_costs_replace) #drop na
checkup = checkup.replace(checkup_replace) #drop na
exercise = exercise.replace(exercise_replace) #drop na
sleep = sleep.replace(sleep_replace)
sleep = sleep.fillna('7-8')
marital = marital.replace(marital_replace) #drop na
education = education.replace(education_replace) #drop na
smoking = smoking.replace(smoking_replace)
smoking = smoking.fillna('no')
alcohol = alcohol.replace(alcohol_replace)
alcohol = alcohol.fillna('no')
diabetes = diabetes.replace(diabetes_replace) #drop na

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
bmi_class = []
for h, w in zip(new_height, new_weight):
    b = w/(h*h)
    if b < 10 or b > 200:
        b = np.nan
    bmi.append(b)
    if b < 15:
        bmi_class.append('very severely underweight')
    elif b < 16:
        bmi_class.append('severely underweight')
    elif b < 18.5:
        bmi_class.append('underweight')
    elif b < 25:
        bmi_class.append('normal')
    elif b < 30:
        bmi_class.append('overweight')
    elif b < 35:
        bmi_class.append('obese class I')
    elif b < 40:
        bmi_class.append('obese class II')
    elif b >= 40:
        bmi_class.append('obese class III')

height = pd.Series(new_height)
weight = pd.Series(new_weight)
bmi = pd.Series(bmi)
bmi_class = pd.Series(bmi_class)
bmi_class.fillna('overweight')

brfss_out = pd.concat([income, race, state, age, sex, bmi_class, ], axis=1)
brfss_out.columns = ['income', 'race', 'state', 'age', 'sex', 'bmi']
brfss_out.to_csv('brfss'+year+'diabetes.csv')
