def main():
    prices = fetch_current_prices()
    if prices:
        print("Current Energy Prices:")
        for price in prices:
            print(f"Hour: {price['hour']}, Price: {price['price']} EUR")

if __name__ == "__main__":
    main()
