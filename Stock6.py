def stock_market_expert():
    print("📈 Stock Market Trading Expert System\n")

    trend = input("What is the market trend? (bullish/bearish/volatile): ").strip().lower()
    risk = input("What's your risk appetite? (low/medium/high): ").strip().lower()
    goal = input("What is your goal? (short-term/long-term): ").strip().lower()

    print("\n🧠 Expert Trading Suggestion:")

    if trend == 'bullish':
        if risk == 'high':
            print("📊 Suggestion: Invest in growth stocks and emerging sectors.")
        elif risk == 'medium':
            print("💼 Suggestion: Consider a mix of blue-chip and index funds.")
        else:
            print("🔒 Suggestion: Focus on dividend-paying, stable stocks.")

    elif trend == 'bearish':
        if goal == 'short-term':
            print("⚠️ Suggestion: Stay liquid. Consider hedging or safe-haven assets.")
        else:
            print("📉 Suggestion: Long-term investors can look for discounted blue-chip opportunities.")

    elif trend == 'volatile':
        if risk == 'high':
            print("🎯 Suggestion: Explore options trading or day trading.")
        else:
            print("🛡️ Suggestion: Avoid risky moves; focus on capital preservation.")

    else:
        print("⚠️ Market condition unclear. Suggest consulting a financial advisor.")

# Run
if __name__ == "__main__":
    stock_market_expert()
