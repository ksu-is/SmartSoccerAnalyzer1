pip install requests beautifulsoup4

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def search_player(player_name):
    url = f"https://api.sofascore.com/api/v1/search/all/{player_name.replace(' ', '%20')}"
    res = requests.get(url, headers=HEADERS)
    data = res.json()

    # Find the first player result
    players = data.get("players", [])
    if not players:
        print("Player not found.")
        return None

    player = players[0]
    return player["slug"], player["id"]

def get_player_stats(slug, player_id):
    stats_url = f"https://api.sofascore.com/api/v1/player/{player_id}/statistics/season"
    res = requests.get(stats_url, headers=HEADERS)
    data = res.json()

    stats = data["statistics"]

    print(f"\n📊 Stats for: {slug.replace('-', ' ').title()}")

    def get_stat(key):
        return stats.get(key, {}).get("value", "N/A")

    print(f"Matches played: {get_stat('games')}")
    print(f"Minutes played: {get_stat('minutes')}")
    print(f"Goals: {get_stat('goals')}")
    print(f"Assists: {get_stat('assists')}")
    print(f"Expected Goals (xG): {get_stat('expectedGoals')}")
    print(f"Expected Assists (xA): {get_stat('expectedAssists')}")
    print(f"Shots: {get_stat('shotsTotal')}")
    print(f"Key Passes: {get_stat('bigChancesCreated')}")
    print(f"Interceptions: {get_stat('interceptions')}")
    print(f"Tackles: {get_stat('tackles')}")
    print(f"Rating: {get_stat('averageRating')}")


def get_player_full_stats(player_name):
    slug_id = search_player(player_name)
    if slug_id:
        slug, player_id = slug_id
        get_player_stats(slug, player_id)

# ▶️ Run the script
player = input("Enter player name: ")
get_player_full_stats(player)
