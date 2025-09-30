import requests

# 🔑 Replace this with your actual API key from The Odds API
API_KEY = '03082ad9eb391b2b7d2f3eedfcc91f70'

# Request parameters
REGIONS = 'us'          # us / uk / eu
MARKETS = 'h2h'         # head-to-head (moneyline)
ODDS_FORMAT = 'decimal' # We want decimal odds

# API endpoints
SPORTS_ENDPOINT = 'https://api.the-odds-api.com/v4/sports/'
ODDS_ENDPOINT = 'https://api.the-odds-api.com/v4/sports/{sport}/odds/'

def get_all_sports():
    """
    Returns a list of sports available in The Odds API.
    Each sport is a dict with keys 'key' and 'title'.
    """
    params = {'apiKey': API_KEY}
    response = requests.get(SPORTS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def fetch_odds_for_sport(sport_key):
    """
    Fetches odds for a specific sport_key.
    Returns a list of odds dicts for that sport.
    """
    url = ODDS_ENDPOINT.format(sport=sport_key)
    params = {
        'apiKey': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    odds_list = []
    for game in data:
        home_team = game.get('home_team')
        away_team = game.get('away_team')
        match = f"{home_team} vs {away_team}"

        for bookmaker in game.get('bookmakers', []):
            book_name = bookmaker.get('title')
            for market in bookmaker.get('markets', []):
                if market.get('key') == MARKETS:
                    for outcome in market.get('outcomes', []):
                        odds_list.append({
                            'sport': sport_key,
                            'match': match,
                            'bookmaker': book_name,
                            'outcome': outcome.get('name'),
                            'odds': float(outcome.get('price'))
                        })
    return odds_list


def fetch_all_odds():
    """
    Fetches odds for all available sports.
    Returns a combined list of odds dicts across all sports.
    """
    sports = get_all_sports()
    all_odds = []
    for sport in sports:
        sport_key = sport.get('key')
        try:
            odds = fetch_odds_for_sport(sport_key)
            all_odds.extend(odds)
        except Exception as e:
            print(f"Failed to fetch odds for {sport_key}: {e}")
    return all_odds


# Example usage:
if __name__ == '__main__':
    odds = fetch_all_odds()
    print(f"Fetched total of {len(odds)} odds entries across all sports.")
    for entry in odds[:10]:
        print(entry)
