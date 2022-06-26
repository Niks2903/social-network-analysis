import matplotlib.pyplot as plt
import pandas as pd
import json

if __name__ == '__main__':

    df = pd.read_csv("FrequencyTable.csv")
    timeFrequency = pd.Series(data=df["frequency"].values, index=df["date"])
    timeFrequency.plot(figsize=(16, 4), label="frequency", legend=True)
    plt.show()
    # tweets = []
    # for line in open('pulwamadata50000.txt', 'r'):
    #     tweets.append(json.loads(line))
    # print(tweets.__len__())
