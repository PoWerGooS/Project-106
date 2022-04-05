import plotly.express as px
import csv
import numpy as np
def plotFigure(dataPath):
  with open("c.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x='Coffee', y='Sleep')
    fig.show()
def getDataSource(dataPath):
  Coffee = []
  Sleep = []
  with open(dataPath) as f:
    csvReader = csv.DictReader(f)
    for row in csvReader:
      Coffee.append(float(row("Coffee")))
      Sleep.append(float(row("Sleep")))
  return{"x":Coffee, 'y':Sleep}
def findCorrelation(DataSource):
  correlation = np.corrcoef(DataSource["x"], DataSource["y"])
  print(correlation)
dataPath = 'c.csv'
DataSource = getDataSource(dataPath)
findCorrelation(DataSource)
