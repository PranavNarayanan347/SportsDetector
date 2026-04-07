# SportsDetector

> Automated arbitrage betting engine that scans sportsbooks, detects guaranteed profit opportunities, and alerts you in real time.

![Python](https://img.shields.io/badge/Python-0d2137?style=flat&logo=python&logoColor=58a6ff)
![Telegram](https://img.shields.io/badge/Telegram_Alerts-0d2137?style=flat&logo=telegram&logoColor=58a6ff)
![Status](https://img.shields.io/badge/status-active-00cc55?style=flat)
![License](https://img.shields.io/badge/license-MIT-1a2e1f?style=flat)

---

## What This Does

SportsDetector continuously monitors odds across multiple sportsbooks and identifies risk-free betting opportunities (arbitrage) where you can lock in profit regardless of the outcome.

Instead of manually comparing lines for hours, this system does it for you — fast, repeatable, and scalable.

---

## Why This Matters

Arbitrage windows are rare, short-lived, and impossible to catch manually at scale. If you're not automated, you're already too late.

| | |
|---|---|
| ⚡ **Speed** | Detect opportunities before they disappear |
| 🎯 **Precision** | Mathematically verified profit scenarios |
| 🔔 **Edge** | Instant alerts so you can act immediately |

---

## Core Concept

Arbitrage exists when:

```
1/odds₁ + 1/odds₂ < 1
```

When the sum of implied probabilities across all outcomes is less than 1, you can distribute stakes across outcomes and guarantee a profit regardless of result.

---

## How It Works

1. **Scrape odds** — pulls live lines from multiple sportsbooks
2. **Normalize markets** — aligns formats and maps equivalent markets across books
3. **Run arbitrage calculations** — flags any scenario where guaranteed profit exists
4. **Send alerts** — fires Telegram notification with opportunity, books, and suggested stakes
5. **Repeat** — runs continuously on a configurable scan interval

---

## Features

- 📊 Automated odds scraping
- 🧮 Arbitrage detection engine
- 🔔 Instant Telegram notifications
- ⏱ Configurable scan frequency
- 🧩 Modular architecture
- 📚 Multi-book support

---

## Tech Stack

- **Python**
- **Requests** / scraping libraries
- **Telegram Bot API**

---

## Roadmap

- [x] Core arbitrage engine
- [x] Telegram alerts
- [ ] Multi-book scaling
- [ ] Stake optimization
- [ ] Smarter market filtering
- [ ] Execution automation
- [ ] Historical tracking
- [ ] UI dashboard

---

## Getting Started

```bash
git clone https://github.com/yourusername/sportsdetector
cd sportsdetector
pip install -r requirements.txt
python main.py
```

### Telegram Setup

1. Create a bot via [BotFather](https://t.me/BotFather)
2. Copy your bot token
3. Get your chat ID
4. Paste both into `config.py`

---

## Reality Check

- Books may limit or flag accounts over time
- Odds move fast — latency affects execution
- Windows are rare and short-lived
- Capital constraints affect realized returns

---

## Bottom Line

If you're serious about arbitrage betting, you need automation. This is your starting point.
