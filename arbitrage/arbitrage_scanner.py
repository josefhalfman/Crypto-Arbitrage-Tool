import requests

def fetch_raydium_pools():
    url = "https://api.raydium.io/pairs"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching Raydium pools: {e}")
    return []

def fetch_orca_pools():
    url = "https://api.orca.so/allPools"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("pools", [])
    except Exception as e:
        print(f"Error fetching Orca pools: {e}")
    return []

def find_arbitrage_opportunities(pools):
    opportunities = []
    for pool in pools:
        if "ammId" in pool and "price" in pool:
            price = float(pool["price"])
            reverse_price = 1 / price
            if price > reverse_price:
                opportunities.append({
                    "pool": pool.get("ammId", "unknown"),
                    "price": price,
                    "reverse_price": reverse_price,
                })
    return opportunities

if __name__ == "__main__":
    all_pools = []

    # Fetch data from Raydium
    raydium_pools = fetch_raydium_pools()
    if raydium_pools:
        all_pools.extend(raydium_pools)
    else:
        print("Failed to fetch Raydium pools.")

    # Fetch data from Orca
    orca_pools = fetch_orca_pools()
    if orca_pools:
        all_pools.extend(orca_pools)
    else:
        print("Failed to fetch Orca pools.")

    # Analyze for arbitrage opportunities
    if all_pools:
        opportunities = find_arbitrage_opportunities(all_pools)
        if opportunities:
            for opp in opportunities:
                print(f"Pool: {opp['pool']}, Price: {opp['price']}, Reverse Price: {opp['reverse_price']}")
        else:
            print("No arbitrage opportunities found.")
    else:
        print("No pools data available.")
