import pandas as pd
from collections import Counter
import emoji

# Summary of sentiments per user
def user_sentiment_summary(df):
    if 'combined_label' in df.columns:
        return df.groupby("sender")["combined_label"].value_counts().unstack(fill_value=0)
    elif 'label' in df.columns:
        return df.groupby("sender")["label"].value_counts().unstack(fill_value=0)
    else:
        raise ValueError("No sentiment label column found.")

# Sentiment trend over time
def sentiment_over_time(df):
    if 'timestamp' not in df.columns:
        raise ValueError("Timestamp column is missing in the DataFrame.")
    if 'combined_label' in df.columns:
        label_column = "combined_label"
    elif 'label' in df.columns:
        label_column = "label"
    else:
        raise ValueError("No sentiment label column found.")
    
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    return df.groupby(['date', label_column]).size().unstack(fill_value=0)

# Extract emojis from a message
def extract_emojis(text):
    return [item['emoji'] for item in emoji.emoji_list(text)]

# Top N emojis used in the chat
def top_emojis(df, n=10):
    all_emojis = []
    for msg in df['message']:
        all_emojis.extend(extract_emojis(msg))
    return Counter(all_emojis).most_common(n)
