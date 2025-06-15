import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure 'output' folder exists
os.makedirs('output', exist_ok=True)

def visualize_sentiment(df):
    sentiment_counts = df['combined_label'].value_counts()

    # 🎨 Define color palette explicitly
    colors = sns.color_palette("pastel")[0:len(sentiment_counts)]

    # 📊 Pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=colors)
    plt.title('Sentiment Distribution')
    plt.tight_layout()
    plt.savefig('output/sentiment_pie_chart.png')
    plt.show()

    # 📊 Bar chart
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='combined_label', palette='Set2')
    plt.title('Number of Messages per Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('output/sentiment_bar_chart.png')
    plt.show()

