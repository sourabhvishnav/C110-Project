import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()


population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)

print("population mean ", population_mean)
print("population std_deviation ", population_std_deviation)


def show_fig(meanData):
    df = meanData
    sampling_mean = statistics.mean(meanData)
    sampling_std_deviation = statistics.stdev(meanData)
    zScore = (sampling_mean - population_mean) / population_std_deviation
    print("Z-score = ", zScore)
    print("Standard deviation of sampling distribution:- ", sampling_std_deviation)
    print("Mean of samling distribution is ", sampling_mean)
    fig = ff.create_distplot(
        [meanData], ["mean_of_1000_samples"], show_hist=False)
    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[
                  0, 1], mode="lines", name="Mean"))
    fig.show()


def random_set_of_mean():
    dataset = []
    for z in range(0, 100):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 1000):
        individualSampleMean = random_set_of_mean()
        mean_list.append(individualSampleMean)
    show_fig(mean_list)


setup()
