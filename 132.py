import plotly.express as px
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
rows = []
import seaborn as sns
name=[]
import csv
with open("dwarf_stars.csv",'r') as f:
  f1=csv.reader(f)
  for a  in f1:
    name.append(a)
star_data=name[1:]
star_data_rows = rows[1:]
gravity=[]
mass=[]
radius=[]
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name.append(star_data[1])

star_gravity=[]

for index,name in enumerate(star_name):
  g=(float(mass[index])) *6.17/100000000000/(float(radius[index]) * float(radius[index]) ) 
  #g=(float(mass[index])*6.17/1000) /(float(radius[index]) * float(radius[index]) ) 
  star_gravity.append(g) 




