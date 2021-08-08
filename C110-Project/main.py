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
    first_std_start, first_std_end = sampling_mean - sampling_std_deviation, sampling_mean + sampling_std_deviation
    second_std_start, second_std_end = sampling_mean - (2*sampling_std_deviation), sampling_mean + (2*sampling_std_deviation)
    third_std_start, third_std_end = sampling_mean - (3*sampling_std_deviation), sampling_mean + (3*sampling_std_deviation)
    zScore = (sampling_mean - population_mean) / population_std_deviation
    print("Z-score = ", zScore)
    print("Standard deviation of sampling distribution:- ", sampling_std_deviation)
    print("Mean of samling distribution is ", sampling_mean)
    fig = ff.create_distplot(
        [meanData], ["mean_of_1000_samples"], show_hist=False)
    fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[
              0, 0.18], mode="lines", name="first_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
              0, 0.18], mode="lines", name="first_std_deviation_end"))

    fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[
              0, 0.18], mode="lines", name="second_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
              0, 0.18], mode="lines", name="second_std_deviation_end"))

    fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[
              0, 0.18], mode="lines", name="third_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[
              0, 0.18], mode="lines", name="third_std_deviation_end"))    
    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[
                  0, 1], mode="lines", name="Mean"))
    fig.show()




def random_set_of_mean(counter):
    dataset = []
    for z in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 100):
        individualSampleMean = random_set_of_mean(30)
        mean_list.append(individualSampleMean)
    show_fig(mean_list)


setup()
