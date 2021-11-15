import csv
import pandas as pd
import plotly.express as px

rows = []

with open('Stars.csv', 'r') as f:
    csv_r = csv.reader(f)
    for row in csv_r:
        rows.append(row)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

print(headers)

df = pd.read_csv('Stars.csv')

star_name = df['Star Name'].tolist()
star_name.pop(0)

mass = df['Mass'].tolist()
mass.pop(0)

radius = df['Radius'].tolist()
radius.pop(0)

distance = df['Distance'].tolist()
distance.pop(0)

gravity = df['Gravity'].tolist()
gravity.pop(0)

fig = px.bar(x = star_name, y = mass, title = 'Star vs. Mass')
fig.show()

fig = px.bar(x = star_name, y = radius, title = 'Star vs. Radius')
fig.show()

fig = px.bar(x = star_name, y = distance, title = 'Star vs. Distance')
fig.show()

fig = px.bar(x = star_name, y = gravity, title = 'Star vs. Gravity')
fig.show()