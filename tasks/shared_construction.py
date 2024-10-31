def get_shares_from_input() -> list:
    """Gets a list of shares from user input and handles input errors."""
    try:
        n = int(input("Input num of parts: ").strip())
        if n <= 0:
            raise ValueError("n must be gather when 0")
        shares = []
        for i in range(n):
            share = float(input(f"Input part {i+1}: ").strip())
            shares.append(share)
        return shares
    except ValueError as e:
        print(f"Input error: {e}")
        return []


def calculate_percentage(shares: list) -> list:
    """Calculates the percentage representation of each share."""
    total = sum(shares)
    if total == 0:
        raise ValueError("Summary error")
    return [(share / total) for share in shares]


def format_percentages(percentages: list) -> list:
    """Formats each percentage to three decimal places."""
    return [f"{percentage:.3f}" for percentage in percentages]


def main():
    shares = get_shares_from_input()
    if not shares:
        return
    try:
        percentages = calculate_percentage(shares)
        formatted_percentages = format_percentages(percentages)
        for percent in formatted_percentages:
            print(percent)
    except ValueError as e:
        print(f"Count error: {e}")


if __name__ == "__main__":
    main()
