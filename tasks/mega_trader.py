from typing import List, Tuple
from pydantic import BaseModel


class Lot(BaseModel):
    """
    Represents a bond lot with details on the day of availability, name, price, and quantity.

    Attributes:
        day (int): The day the lot becomes available on the market.
        name (str): The name or identifier of the bond.
        price (float): The price of the bond as a percentage of its nominal value.
        quantity (int): The number of bonds in the lot.
    """

    day: int
    name: str
    price: float
    quantity: int

    def calculate_profit(self, n: int) -> Tuple[float, float]:
        """
        Calculate the profit from purchasing this lot by day N + 30.

        Args:
            n (int): The total number of trading days.

        Returns:
            Tuple[float, float]: A tuple with the expected profit and the cost of the lot.
        """
        nominal = 1000
        daily_coupon = 1
        days_held = (n + 30) - self.day

        cost = (self.price / 100) * nominal * self.quantity
        income_from_nominal = nominal * self.quantity
        income_from_coupons = daily_coupon * days_held * self.quantity
        total_income = income_from_nominal + income_from_coupons
        profit = total_income - cost

        return profit, cost


def parse_input() -> Tuple[int, int, int, List[Lot]]:
    """
    Parses input data to retrieve the number of days, maximum lots per day,
    available funds, and market offers.

    Returns:
        Tuple[int, int, int, List[Lot]]: A tuple with the number of trading days,
        maximum number of lots, total funds, and list of market offers (lots).
    """
    n, m, s = map(int, input("Enter N, M, S values: ").strip().split())
    market_offers = []

    print("Enter market offers in format: <day> <name> <price> <quantity>")
    while True:
        line = input().strip()
        if not line:
            break
        day, name, price, quantity = line.split()
        market_offers.append(Lot(day=int(day), name=name, price=float(price), quantity=int(quantity)))

    return n, m, s, market_offers


def select_lots(n: int, s: int, market_offers: List[Lot]) -> Tuple[int, List[Tuple[int, str, float, int]]]:
    """
    Selects lots to maximize profit while staying within the available funds.

    Args:
        n (int): The total number of trading days.
        s (int): Available funds for purchasing lots.
        market_offers (List[Lot]): List of bond lots available on the market.

    Returns:
        Tuple[int, List[Tuple[int, str, float, int]]]: The total profit and
        a list of selected lots in the format of (day, name, price, quantity).
    """
    offers_with_profit = [
        (lot.calculate_profit(n)[0], lot.calculate_profit(n)[1], lot)
        for lot in market_offers
    ]

    offers_with_profit.sort(key=lambda x: x[0], reverse=True)

    selected_lots = []
    total_profit = 0

    for profit, cost, lot in offers_with_profit:
        if s >= cost:
            s -= cost
            total_profit += profit
            selected_lots.append((lot.day, lot.name, lot.price, lot.quantity))

    return int(total_profit), selected_lots


def main():
    """
    Main function to orchestrate the parsing of inputs, selection of profitable lots,
    and output of results.
    """
    n, m, s, market_offers = parse_input()
    total_profit, selected_lots = select_lots(n, s, market_offers)

    print(total_profit)
    for day, name, price, quantity in selected_lots:
        print(f"{day} {name} {price} {quantity}")
    print()


if __name__ == "__main__":
    main()
