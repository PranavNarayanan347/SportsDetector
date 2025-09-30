from collections import defaultdict

def implied_probability(odds):
    """
    Calculate the implied probability of a decimal odd.
    Formula: implied probability = 1 / decimal_odds
    """
    return 1 / float(odds)


def calculate_stakes(odds1, odds2, total_stake=100):
    """
    Given two decimal odds for opposing outcomes and a total stake,
    calculate how much to bet on each outcome to guarantee equal profit.
    Returns a tuple: (stake1, stake2)
    """
    p1 = implied_probability(odds1)
    p2 = implied_probability(odds2)
    arb_sum = p1 + p2
    stake1 = (p1 / arb_sum) * total_stake
    stake2 = (p2 / arb_sum) * total_stake
    return stake1, stake2


def find_arbitrage(odds_list, total_stake=100):
    """
    Scan a list of odds entries (each a dict with keys: 'match', 'bookmaker',
    'outcome', 'odds', and optional 'sport'), group entries by match, and check
    each pair of opposing outcomes for arbitrage.

    If implied_probability(o1) + implied_probability(o2) < 1, calculate stakes
    and profit, and collect an opportunity dict:
      {
        'match': ...,
        'sport': ...,
        'home_team': ...,        <-- the name of team A
        'away_team': ...,        <-- the name of team B
        'home_bookmaker': ...,
        'home_odds': ...,
        'away_bookmaker': ...,
        'away_odds': ...,
        'stake_home': ...,
        'stake_away': ...,
        'profit': ...
      }
    Returns a list of such opportunity dicts.
    """
    opportunities = []
    matches = defaultdict(list)

    # 1) Group odds by match
    for odd in odds_list:
        matches[odd['match']].append(odd)

    # 2) Process each match
    for match, odds in matches.items():
        # Identify the two distinct outcomes (team names)
        unique_outcomes = list({o['outcome'] for o in odds})
        if len(unique_outcomes) != 2:
            # skip anything that isn't a 2-way market
            continue

        # Unpack: team names (could be reversed in some cases, order doesn't matter)
        outcome_a, outcome_b = unique_outcomes

        # 3) For each bookmaker offering outcome_a, pair with each bookmaker offering outcome_b
        for entry_a in [o for o in odds if o['outcome'] == outcome_a]:
            for entry_b in [o for o in odds if o['outcome'] == outcome_b]:
                p1 = implied_probability(entry_a['odds'])
                p2 = implied_probability(entry_b['odds'])

                # 4) Check for arbitrage: sum of implied probabilities < 1
                if p1 + p2 < 1:
                    stake_a, stake_b = calculate_stakes(entry_a['odds'], entry_b['odds'], total_stake)
                    profit = min(stake_a * entry_a['odds'], stake_b * entry_b['odds']) - total_stake

                    opportunities.append({
                        'match': match,
                        'sport': odds[0].get('sport', 'N/A'),
                        'home_team': outcome_a,              # team name for outcome_a
                        'away_team': outcome_b,              # team name for outcome_b
                        'home_bookmaker': entry_a['bookmaker'],
                        'home_odds': entry_a['odds'],
                        'away_bookmaker': entry_b['bookmaker'],
                        'away_odds': entry_b['odds'],
                        'stake_home': stake_a,
                        'stake_away': stake_b,
                        'profit': profit
                    })

    return opportunities
