import pandas


patient_data = pandas.read_csv('PatientData.csv')

print(patient_data) 
patient_data.info()
patient_data.plot.scatter(0,2)
patient_data.plot.scatter(0,3)
patient_data.fillna(patient_data.mean())
print(patient_data.corr().sort_values('8'))
