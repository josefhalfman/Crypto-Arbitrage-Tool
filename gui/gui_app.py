import tkinter as tk
from arbitrage.arbitrage_scanner import find_arbitrage_opportunities, fetch_pools
from arbitrage.triangle_arbitrage import find_triangle_arbitrage

def show_arbitrage_opportunities():
    pools = fetch_pools()
    if not pools:
        output_label.config(text="Failed to fetch pools.")
        return

    opportunities = find_arbitrage_opportunities(pools)
    if opportunities:
        result = "\n".join(
            [f"Pool: {opp['pool']}, Price: {opp['price']:.2f}, Reverse Price: {opp['reverse_price']:.2f}" for opp in opportunities]
        )
    else:
        result = "No arbitrage opportunities found."
    output_label.config(text=result)

def show_triangle_arbitrage_opportunities():
    pools = fetch_pools()
    if not pools:
        output_label.config(text="Failed to fetch pools.")
        return

    opportunities = find_triangle_arbitrage(pools)
    if opportunities:
        result = "\n".join(
            [f"Path: {' -> '.join(opp['path'])}, Profit: {opp['profit']:.2%}" for opp in opportunities]
        )
    else:
        result = "No triangular arbitrage opportunities found."
    output_label.config(text=result)

def run_app():
    global output_label

    root = tk.Tk()
    root.title("Solana Arbitrage Scanner")
    root.geometry("600x400")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    arbitrage_button = tk.Button(
        frame,
        text="Find Arbitrage Opportunities",
        command=show_arbitrage_opportunities,
        width=30,
    )
    arbitrage_button.grid(row=0, column=0, padx=10, pady=10)

    triangle_button = tk.Button(
        frame,
        text="Find Triangle Arbitrage Opportunities",
        command=show_triangle_arbitrage_opportunities,
        width=30,
    )
    triangle_button.grid(row=0, column=1, padx=10, pady=10)

    output_label = tk.Label(root, text="", wraplength=500, justify="left", anchor="w")
    output_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_app()
