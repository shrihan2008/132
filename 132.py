import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
rows = []
import seaborn as sns
name=[]
import csv
import pandas as pd
f=pd.read_csv('star_with_gravity.csv')
star_data=name[1:]
star_data_rows = rows[1:]
gravity=[]
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name.append(star_data[1])

star_gravity=[]






plt.plot(mass,radius)
plt.show()