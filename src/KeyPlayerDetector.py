import pandas as pd
import json
import numpy as np
from pandas import DataFrame


class KeyPlayerDetector:
    tweet_score = 10
    retweet_score = 7
    follower_score = 2

    def __init__(self):
        pass

    def delete_duplicates(self):
        df = pd.read_csv("KeyPlayersPulwama.csv")
        df = df.drop_duplicates(subset="Id")
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.to_csv("KeyPlayersPulwama.csv", mode="w")
        return

    def make_file(self):
        tweets = []
        for line in open("pulwamadata50000.txt", "r"):
            tweets.append(json.loads(line))
        users = []
        for tweet in tweets:
            users.append(tweet["user"])
        index = []
        for user in users:
            index.append(user["id"])
        df = DataFrame(data=[user["id"] for user in users], columns=["Id"])
        df["Name"] = np.array([user["name"] for user in users])
        df["Location"] = np.array([user["location"] for user in users])
        df["FollowersCount"] = np.array([user["followers_count"] for user in users])
        df["FriendsCount"] = np.array([user["friends_count"] for user in users])
        df["RetweetCount"] = 0
        df["TweetCount"] = 1
        df["Score"] = 5
        for i in df.index:
            df.at[i, "Score"] = df.at[i, "Score"] + (df.at[i, "FollowersCount"]* KeyPlayerDetector.follower_score)
        df = df.drop_duplicates(subset="Id")
        df.to_csv("KeyPlayersPulwama.csv", mode="w")

        place_array = []
        for tweet in tweets:
            if tweet["place"]:
                place_array.append(tweet["place"]["full_name"])
        df_places = DataFrame(data=[place for place in place_array], columns=["Place"])
        df_places.to_csv("PlacesPulwama.csv", mode="w")
        return True

    def add_score(self):
        df_table = pd.read_csv("KeyPlayersPulwama.csv", index_col="Id")
        tweets = []
        for line in open("pulwamadata50000.txt", "r"):
            tweets.append(json.loads(line))
        source = []
        destination = []
        for i in range(tweets.__len__()):
            if "retweeted_status" in tweets[i]:
                status = tweets[i]["retweeted_status"]
                user = status["user"]
                if user["id"] in df_table.index:
                    df_table.at[user['id'], "RetweetCount"] = df_table.at[user['id'], "RetweetCount"] + 1
                    df_table.at[user['id'], "Score"] = df_table.at[user['id'], "Score"] \
                                                       + KeyPlayerDetector.retweet_score
                    source.append(user["id"])
                    destination.append(tweets[i]["user"]["id"])

        users = []
        for tweet in tweets:
            user = tweet["user"]
            if user["id"] in df_table.index:
                df_table.at[user['id'], "TweetCount"] = df_table.at[user['id'], "TweetCount"] + 1
                df_table.at[user['id'], "Score"] = df_table.at[user['id'], "Score"] \
                                                   + KeyPlayerDetector.tweet_score
            else:
                users.append(user)
        df = DataFrame(data=[user["id"] for user in users], columns=["Id"])
        df["Name"] = np.array([user["name"] for user in users])
        df["Location"] = np.array([user["location"] for user in users])
        df["FollowersCount"] = np.array([user["followers_count"] for user in users])
        df["FriendsCount"] = np.array([user["friends_count"] for user in users])
        df["RetweetCount"] = 0
        df["TweetCount"] = 1
        df["Score"] = 5
        for i in df.index:
            df.at[i, "Score"] = df.at[i, "Score"] + (df.at[i, "FollowersCount"] * KeyPlayerDetector.follower_score)
        df_table.to_csv("KeyPlayersPulwama.csv", mode="w")
        df_table_new = pd.read_csv("KeyPlayersPulwama.csv")
        df_table_new = df.append(df_table_new, ignore_index=True, sort=False)
        df_table_new = df_table_new.loc[:, ~df_table_new.columns.str.contains('^Unnamed')]
        df_table_new = df_table_new.sort_values(by="Score", ascending=False)
        df_table_new = df_table_new.drop_duplicates(subset="Id")
        df_table_new.to_csv("KeyPlayersPulwama.csv", mode="w")

        df_network = DataFrame(data=[source[i] for i in range(source.__len__())], columns=["Source"])
        df_network["Destination"] = np.array([destination[i] for i in range(destination.__len__())])
        print(df_network)
        df_network.to_csv("NetworkPulwama.csv", mode="w")

        place_array = []
        for tweet in tweets:
            if tweet["place"]:
                place_array.append(tweet["place"]["full_name"])
        df_places = DataFrame(data=[place for place in place_array], columns=["Place"])
        df_places.to_csv("PlacesPulwama.csv", mode="a", header=False)


if __name__ == '__main__':
    keyPlayerDetector = KeyPlayerDetector()
    makeFileStatus = keyPlayerDetector.make_file()
    keyPlayerDetector.add_score()
    keyPlayerDetector.delete_duplicates()
