from modules.chat_parser import parse_chat
from modules.sentiment import analyze_sentiments
from modules.visualizer import visualize_sentiment

def main():
    # Path to your WhatsApp exported .txt file
    chat_file = "data/chat.txt"
 # Make sure the actual exported chat is saved with this name in the project folder

    print("📄 Parsing chat...")
    messages = parse_chat(chat_file)

    if not messages:
        print("⚠️ No valid messages found. Please check your chat file.")
        return

    print("🔍 Running sentiment analysis...")
    df = analyze_sentiments(messages)

    print("📊 Generating sentiment visualizations...")
    visualize_sentiment(df)

    # Optionally save to CSV
    df.to_csv("whatsapp_sentiment_output.csv", index=False)
    print("✅ Analysis complete. Output saved to whatsapp_sentiment_output.csv")

if __name__ == "__main__":
    main()
