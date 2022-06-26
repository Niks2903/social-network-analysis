import datetime
import pandas as pd
import json


class StoreFrequencyCount:

    def __init__(self):
        pass

    @staticmethod
    def frequency_count():
            tweets = []
            for line in open('tweets.txt', 'r'):
                tweets.append(json.loads(line))
            now = datetime.datetime.now();
            open("tweets.txt", "w").close()
            frequency = tweets.__len__()
            time = now.strftime("%Y-%m-%d %H:%M")

            df = pd.DataFrame(data=[time], columns=['date'])
            df["frequency"] = frequency

            df.to_csv("FrequencyTable.csv", mode='a', header=False)


if __name__ == '__main__':
    StoreFrequencyCount.frequency_count()
