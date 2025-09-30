# auto_run.py

import time
from datetime import datetime
from odds_scraper import fetch_all_odds
from arb_calculator import find_arbitrage
from notifier import send_telegram  # or send_sms, depending on your setup

def main():
    seen_keys = set()

    # Wait one hour (3600 seconds) between scrapes
    SCRAPE_INTERVAL = 3600

    # Define your “daytime” window (24-hour clock)
    DAY_START_HOUR = 8    #  8 AM
    DAY_END_HOUR   = 22   # 10 PM

    try:
        while True:
            try:
                # 1) Fetch odds and detect arbitrages
                odds_list     = fetch_all_odds()
                opportunities = find_arbitrage(odds_list)
                now           = datetime.now()

                print(f"[{now:%Y-%m-%d %H:%M:%S}] Fetched {len(odds_list)} odds entries.")

                for opp in opportunities:
                    # Build a unique key: "Match|BookA:OddsA|BookB:OddsB"
                    key = (
                        f"{opp['match']}|"
                        f"{opp['home_bookmaker']}:{opp['home_odds']:.2f}|"
                        f"{opp['away_bookmaker']}:{opp['away_odds']:.2f}"
                    )

                    # Skip if we've already alerted on this one
                    if key in seen_keys:
                        continue

                    # Only consider if profit > $5
                    if opp['profit'] > 5:
                        # Check if current hour is within 8 AM – 10 PM
                        current_hour = now.hour
                        if DAY_START_HOUR <= current_hour < DAY_END_HOUR:
                            # It’s within the window → send notification now
                            home_team    = opp['home_team']
                            away_team    = opp['away_team']
                            home_book    = opp['home_bookmaker']
                            away_book    = opp['away_bookmaker']
                            home_odds    = opp['home_odds']
                            away_odds    = opp['away_odds']
                            stake_home   = opp['stake_home']
                            stake_away   = opp['stake_away']
                            total_risked = stake_home + stake_away
                            profit       = opp['profit']
                            payout_home  = stake_home * home_odds
                            payout_away  = stake_away * away_odds

                            message = (
                                f"🏅 Arbitrage Alert! 🏅\n"
                                f"Match: {opp['match']}\n\n"
                                f"— Bet Details —\n"
                                f"Bet **{home_team}** at {home_book} @ {home_odds:.2f} → Stake ${stake_home:.2f}\n"
                                f"Bet **{away_team}** at {away_book} @ {away_odds:.2f} → Stake ${stake_away:.2f}\n\n"
                                f"— Payout Scenarios —\n"
                                f"If {home_team} wins:  ${stake_home:.2f} × {home_odds:.2f} = ${payout_home:.2f}\n"
                                f"If {away_team} wins:  ${stake_away:.2f} × {away_odds:.2f} = ${payout_away:.2f}\n\n"
                                f"Total Risked: ${total_risked:.2f}\n"
                                f"Guaranteed Profit: ${profit:.2f}\n\n"
                                f"(No matter who wins, lock in ≈${profit:.2f} profit.)"
                            )

                            send_telegram(message)
                            print(f"[{now:%Y-%m-%d %H:%M:%S}] Sent Telegram: {message}")

                            # Mark as seen so we don't re‐alert this same opportunity
                            seen_keys.add(key)

                        else:
                            # Outside 8 AM–10 PM → skip sending but keep the key untracked
                            print(f"[{now:%Y-%m-%d %H:%M:%S}] Opportunity found but outside 08:00–22:00; deferring alert: {key}")

            except Exception as e:
                now = datetime.now()
                print(f"[{now:%Y-%m-%d %H:%M:%S}] Error: {e}")

            # Wait until the next scheduled scrape
            now = datetime.now()
            print(f"[{now:%Y-%m-%d %H:%M:%S}] Sleeping for {SCRAPE_INTERVAL} seconds...\n")
            time.sleep(SCRAPE_INTERVAL)

    except KeyboardInterrupt:
        print("\nExiting arbitrage scraper gracefully.")

if __name__ == "__main__":
    main()
