import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


apple_store = pd.read_csv("appstore/AppleStore.csv")
apple_store_desc = pd.read_csv("appstore/appleStore_description.csv")
# importing all data for AppStore

google_play_store = pd.read_csv("googleplay/googleplaystore.csv")
google_play_store_reviews = pd.read_csv("googleplay/googleplaystore_user_reviews.csv")
# importing all data for GooglePlay

for index in google_play_store.index:
    reviews = google_play_store.loc[index, 'Reviews']
    if reviews.find("M") != -1:
        print(int(float(reviews[:-1]) * 10 ** 6))
        google_play_store.loc[index, 'Reviews'] = int(float(reviews[:-1]) * 10 ** 6)

google_play_store = google_play_store.astype({"Reviews": int, "Rating": float})

