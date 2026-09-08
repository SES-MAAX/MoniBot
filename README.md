# 🤖 MoniBot

**MoniBot** is a Telegram bot built with **Python** and **pyTelegramBotAPI** that provides quick access to live Iranian market prices by scraping data from **TGJU**.

> 🚧 This project is currently in Beta.

## ✨ Features

- 💵 US Dollar (USD)
- 🟡 24K Gold
- 🪙 18K Gold
- 🥈 Silver (999)
- 👑 Emami Coin
- 💰 Quarter Gram Coin
- 💲 Tether (USDT)

## 📂 Project Structure

```text
MoniBot/
├── main.py
├── scraper.py
├── .env
├── .gitignore
└── README.md
```

## 🛠️ Requirements

- Python 3.10+
- pyTelegramBotAPI
- requests
- beautifulsoup4
- python-dotenv

Install dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup

Create a `.env` file in the project root and add your Telegram bot token:

```env
TOKEN=YOUR_BOT_TOKEN
```

Run the bot:

```bash
python main.py
```

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/start` | Show the welcome message |
| `/restart` | Reopen the main menu |
| `/help` | Display the help message |

## 📈 Supported Assets

| Asset | Status |
|-------|--------|
| US Dollar | ✅ |
| 24K Gold | ✅ |
| 18K Gold | ✅ |
| Silver (999) | ✅ |
| Emami Coin | ✅ |
| Quarter Gram Coin | ✅ |
| Tether | ✅ |

## 🚀 Future Plans

- Improve error handling
- Add more market assets
- Optimize data refreshing
- Enhance the Telegram interface