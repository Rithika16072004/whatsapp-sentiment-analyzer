# 💬 WhatsApp Sentiment Analyzer

Analyze the sentiment of your WhatsApp chat conversations using NLP and emoji interpretation! This project leverages HuggingFace's transformer models to classify messages into **Positive**, **Negative**, or **Neutral**, with optional emoji-based analysis and visualizations.

---

## 🚀 Features

- 📄 Parses WhatsApp chat exports (`.txt` files)
- 🧠 Uses [CardiffNLP's Twitter RoBERTa model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) for text-based sentiment classification
- 😊 Includes emoji sentiment analysis
- 📊 Generates pie and bar charts for sentiment distribution
- 📁 Saves all output visuals in an `output/` folder

---

## 🛠️ Project Structure

  whatsapp-sentiment-analyzer/
│
├── main.py # Main entry point
├── chat.txt # Your exported WhatsApp chat
│
├── modules/
│ ├── chatparser.py # Extracts sender & message from chat
│ ├── sentiment.py # Runs sentiment analysis
│ ├── visualizer.py # Creates pie/bar charts
| ├──analytics.py # Optional) Additional analysis
│
├── output/
│ ├── sentiment_pie_chart.png # Pie chart output
│ └── sentiment_bar_chart.png # Bar chart output
│
├── .venv/ # Your Python virtual environment (optional)
├── requirements.txt # Python dependencies
└── README.md # This file



---

## 📦 Installation

### ✅ Prerequisites

- Python 3.8 or above
- pip

### 🔧 Setup

```bash
# Clone this repo
git clone https://github.com/yourusername/whatsapp-sentiment-analyzer.git
cd whatsapp-sentiment-analyzer

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate      # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
