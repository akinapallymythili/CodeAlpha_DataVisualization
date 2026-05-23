import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sentiment_Output.csv")

counts = df["Sentiment"].value_counts()

counts.plot(kind="bar")

plt.title("Amazon Reviews Sentiment Analysis")

plt.xlabel("Sentiment")

plt.ylabel("Number of Reviews")

plt.show()