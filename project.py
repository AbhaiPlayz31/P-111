import statistics
import plotly.figure_factory as ff 
import pandas as pd 
import csv 
import random



df = pd.read_csv('medium_data.csv')

data = df['reading_time'].tolist()


def randomSetOfMean(counter):

    dataSet = []

    for i in range(0,counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    
    sampleMean = statistics.mean(dataSet)

    return sampleMean


def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ['reading_time'], show_hist=False)
    mean = statistics.mean(meanList)
    print('Mean is:', mean)
    fig.show()
    
    

def setUp():
    meanList=[]

    for i in range(0,100):
        SetOfMean = randomSetOfMean(30)
        meanList.append(SetOfMean)
    showFig(meanList)



setUp()



sampleSTD = statistics.stdev(dataSet)