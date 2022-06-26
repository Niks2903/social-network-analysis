from  threading import Thread
import schedule
import time
import StoreFrequencyCount
import KeyPlayerDetector
import TweetStreamer


def job():
    print("I'm working")
    objKeyPlayerDetector = KeyPlayerDetector.KeyPlayerDetector()
    objKeyPlayerDetector.add_score()
    objStoreFrequencyCount = StoreFrequencyCount.StoreFrequencyCount()
    objStoreFrequencyCount.frequency_count()


schedule.every(15).minutes.do(job)
schedule.every(10).seconds.do(job)


if __name__ == "__main__":
    hash_tag_list = ["#jihad", "#lashkar-e-taiba", "#ISIS", "#isis", "#taliban", "#islamists", "#Al Qaeda",
                     "#Al-Shabaab", "#jaesh", "#islamicState", "#kashmir", "#FreedomForKashmir", "#KashmirCrisis",
                     "#wahhabism", "#goharshahi", "#wahhabi"]
    fetched_tweets_filename = "tweets.txt"
    objTwitterStreamer = TweetStreamer.TwitterStreamer()
    objTwitterStreamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    while True:
        schedule.run_pending()
        time.sleep(1)
    pulwama_keywords_list = ["#kashmir", "#pulwama", "#illegalindianoccupation", "#IllegalIndianOccupation", "#FreedomForKashmir", "#freedomforkashmir",
                             "#KashmirCrisis", "#kashmircrisis", "#savekashmir", "#Saveashmir", "#freedomforkashmir", "#FreedomForKashmir",
                              "#KashmirIsBleeding", "#kashmirisbleeding" ]
