import itertools

def find_triangle_arbitrage(pools):
    opportunities = []
    for token_combination in itertools.combinations(pools, 3):
        try:
            token1, token2, token3 = token_combination

            # Extract prices from pools
            price1 = float(token1.get("price", 1))
            price2 = float(token2.get("price", 1))
            price3 = float(token3.get("price", 1))

            # Check for triangular arbitrage
            forward_trade = price1 * price2 * price3
            reverse_trade = 1 / forward_trade

            if forward_trade > 1.01:  # Threshold for profitability
                opportunities.append({
                    "path": [token1["ammId"], token2["ammId"], token3["ammId"]],
                    "profit": forward_trade - 1
                })
            elif reverse_trade > 1.01:
                opportunities.append({
                    "path": [token3["ammId"], token2["ammId"], token1["ammId"]],
                    "profit": reverse_trade - 1
                })
        except Exception as e:
            continue

    return opportunities

if __name__ == "__main__":
    # Example pools data for testing
    example_pools = [
        {"ammId": "pool1", "price": 1.1},
        {"ammId": "pool2", "price": 0.9},
        {"ammId": "pool3", "price": 1.2},
    ]

    opportunities = find_triangle_arbitrage(example_pools)
    if opportunities:
        for opp in opportunities:
            print(f"Path: {opp['path']}, Profit: {opp['profit']:.2%}")
    else:
        print("No triangular arbitrage opportunities found.")
