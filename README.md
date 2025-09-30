Sports Detector – Arbitrage Betting Notifier
📌 Overview

Sports Detector is a Python-based tool designed to identify and notify users of arbitrage betting opportunities across multiple sportsbooks. Arbitrage betting (also called “sure betting”) exploits pricing inefficiencies between bookmakers to guarantee a profit regardless of the match outcome.

This project automates the workflow:

Scrape betting odds from multiple sportsbooks.

Run arbitrage detection algorithms.

Notify the user via Telegram (or other channels like SMS/email).

Repeat at configurable intervals.

🚀 Features

Odds Scraping: Pulls real-time odds from selected sportsbooks.

Arbitrage Calculator: Detects risk-free opportunities using mathematical checks.

Notifications: Sends alerts to Telegram (or extendable to SMS/Email).

Configurable Intervals: Adjust scraping frequency to balance speed and server load.

Extensible: Add new bookmakers, sports, or notification methods with minimal changes.

🛠 Installation
1. Clone the repository
git clone https://github.com/PranavNarayanan347/SportsDetector.git
cd SportsDetector

2. Set up a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

⚙️ Usage
Run the arbitrage notifier
python auto_run.py


This will:

Continuously scrape odds

Detect arbitrage

Send notifications

Configuration

SCRAPE_INTERVAL: Change frequency of scraping inside auto_run.py.

Notifier: Configure Telegram bot token or SMS gateway in notifier.py.

📂 Project Structure
SportsDetector/
│── auto_run.py         # Main entry point
│── odds_scraper.py     # Scrapes odds from sportsbooks
│── arb_calculator.py   # Finds arbitrage opportunities
│── notifier.py         # Sends Telegram/SMS alerts
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

📊 Example Flow

Input: Odds from Bookmaker A and Bookmaker B.

Process:

Calculate implied probabilities.

Detect mismatches where combined probability < 100%.

Output: Alert:

Arbitrage found! 
Match: Lakers vs Celtics
Bookmaker A: Celtics @ 2.10
Bookmaker B: Lakers @ 2.05
Stake split: $48 on A, $52 on B
Guaranteed Profit: $5.20

⚠️ Disclaimer

This tool is for educational and research purposes only. Sportsbooks may restrict or ban accounts engaging in arbitrage betting. Use responsibly and at your own risk.

📌 Future Work

Expand to more bookmakers.

Add live odds APIs for faster updates.

Build a web dashboard for visualizing opportunities.

Integrate portfolio and bankroll management.
