import pandas as pd
import platform 

url= ('https://health.data.ny.gov/resource/46xm-urtu.csv')

sparcs= pd.read_csv(url)
sparcs
sparcs.to_csv('sparcs_data.csv', index=False)
sparcs.columns

sparcs['total_charges']
sparcs['total_costs']

# total_charges_numeric column
sparcs['total_charges_clean']= sparcs['total_charges'].str.replace(',','')
sparcs['total_charges_clean']= pd.to_numeric(sparcs['total_charges_clean'], errors= 'coerce')
sparcs['total_charges_clean'].dtype

sparcs['total_costs_clean']= sparcs['total_costs'].str.replace(',','')
sparcs['total_costs_clean']= pd.to_numeric(sparcs['total_costs_clean'], errors= 'coerce')
sparcs['total_costs_clean'].dtype

sparcs.to_csv('total_costs_clean', index=False)