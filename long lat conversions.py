from math import radians, cos, sin, asin, sqrt
import pandas as pd


data = pd.read_csv('Documents/AP Statistics/Final Project/dataset.csv')
print(data)
def convert(lat,lng, degrees=True):
  r = 6371
  a = sin(lat/2)**2 + cos(lat) * sin(lng/2)**2
  d = 2 * r * asin(sqrt(a)) 
  return d
a = data.reclong 
b = data.reclat
a = int(a)
b = int(b)
print(convert(b,a))