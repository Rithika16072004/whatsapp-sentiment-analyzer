from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import emoji
import re

# Basic emoji sentiment mapping
emoji_sentiment = {
    "😊": "POSITIVE", "😄": "POSITIVE", "😍": "POSITIVE", "👍": "POSITIVE",
    "😢": "NEGATIVE", "😠": "NEGATIVE", "😡": "NEGATIVE", "👎": "NEGATIVE",
    "😐": "NEUTRAL", "🤔": "NEUTRAL", "😶": "NEUTRAL"
}

# Preprocess text for the CardiffNLP model
def preprocess_message(text):
    text = text.lower()
    text = re.sub(r"http\S+", "http", text)
    text = re.sub(r"@\w+", "@user", text)
    text = re.sub(r"#\w+", "", text)
    text = emoji.demojize(text)  # Turn 😄 into ":smiling_face:"
    return text

# Extract emojis from a message
def extract_emojis(text):
    return [item['emoji'] for item in emoji.emoji_list(text)]

# Calculate emoji-based sentiment
def get_emoji_sentiment(emojis):
    sentiment_count = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
    for e in emojis:
        sentiment = emoji_sentiment.get(e, None)
        if sentiment:
            sentiment_count[sentiment] += 1
    if not any(sentiment_count.values()):
        return None
    return max(sentiment_count, key=sentiment_count.get)

# Main sentiment analysis function
def analyze_sentiments(messages):
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    results = []

    for sender, message in messages:
        emojis = extract_emojis(message)
        emoji_sent = get_emoji_sentiment(emojis)

        try:
            cleaned_msg = preprocess_message(message)
            result = classifier(cleaned_msg[:512])[0]
            label_map = {'LABEL_0': 'NEGATIVE', 'LABEL_1': 'NEUTRAL', 'LABEL_2': 'POSITIVE'}
            predicted_label = label_map.get(result['label'], result['label'])  

            label_map = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}
            text_sent = label_map.get(result['label'], result['label'])
            combined_label = text_sent

            if emoji_sent and emoji_sent != text_sent:
                combined_label = f"{text_sent} (emoji: {emoji_sent})"

            results.append({
                "sender": sender,
                "message": message,
                "text_sentiment": result['label'],
                "emoji_sentiment": emoji_sent,
                "combined_label": combined_label,
                "score": round(result['score'], 2)
            })
        except Exception as e:
            print(f"Error processing message: {message}\n{e}")
            continue

    return pd.DataFrame(results)
