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
    installs = google_play_store.loc[index, 'Installs']
    if installs.find("+") != -1:
        google_play_store.loc[index, 'Installs'] = installs[:-1].replace(",", "")

google_play_store = google_play_store.astype({"Reviews": int, "Rating": float, "Installs": int})

google_play_store = google_play_store.astype({"Reviews": int, "Rating": float})

google_play_store[(google_play_store["Reviews"] > 300) & (google_play_store["Rating"] >= 4.9)].sort_values(by=["Reviews"]) # apps with multiple genres are not in this top
