from odds_scraper import fetch_all_odds
from arb_calculator import find_arbitrage
from notifier import send_telegram   # (assuming you’re using Telegram notifications)

def main():
    # 1) Fetch odds across all sports
    odds_list = fetch_all_odds()
    print(f"Fetched total of {len(odds_list)} odds entries across all sports.")

    # 2) Identify arbitrage opportunities
    opportunities = find_arbitrage(odds_list)
    if not opportunities:
        print("No arbitrage opportunities found.")
        return

    # 3) Filter out anything with profit ≤ $5
    profitable_opps = [opp for opp in opportunities if opp['profit'] > 5]

    if not profitable_opps:
        print("No arbitrage opportunities above $5 profit.")
        return

    # 4) Send notifications only for those filtered opportunities
    for opp in profitable_opps:
        sport        = opp.get('sport', 'N/A')
        match        = opp['match']
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

        # Compute payout scenarios
        payout_home = stake_home * home_odds
        payout_away = stake_away * away_odds

        message = (
            f"🏅 Arbitrage Alert! 🏅\n"
            f"Sport: {sport}\n"
            f"Match: {match}\n\n"
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
        print("Sent Telegram:", message)

if __name__ == '__main__':
    main()
