# 1 Percentage Calculation Program

## Overview
This program calculates the percentage representation of a set of portions (shares), each inputted by the user, and formats them to three decimal places.

### Functions:

- **`get_shares_from_input()`**: Prompts the user to input the number of shares and each share value, handling any input errors.
- **`calculate_percentage()`**: Computes the percentage representation of each share based on their total.
- **`format_percentages()`**: Formats each calculated percentage value to three decimal places for clear output.
  
---
### Input Format
1. The first input should be the number of shares (n).
2. The following n lines should contain the values of the shares.

### Output Format
* The output will display each share's percentage formatted to three decimal places.

### Computational Complexity
* Time Complexity: O(N) for calculating the sum and percentages, where N is the number of shares.
* Space Complexity: O(N) for storing shares and percentages.

### Constraints
The number of shares (N) should be reasonable to execute within 5 seconds. For instance, N should not exceed 10^7.

### Subjective Difficulty Rating
* Difficulty: 2/10 (moderate complexity)
* Time Spent: Approximately 20 minutes to implement and test.

# 2 MegaTrader

## Overview
This project contains two Python algorithms that solve finance-related tasks for bond purchasing and profit calculation. Each algorithm takes bond market data with pricing, quantity, and a given trading window and calculates the optimal purchases for maximum returns under specific conditions.

### Algorithms:
1. **Profit Maximization by Market Lots**  
   Aims to help a trader choose the most profitable bond lots while adhering to a spending limit.
   
2. **Percentage Calculation of Portions**  
   Converts a set of fractions to percentage values to standardize and represent them proportionally.



##  MegaTrader Profit Maximization Algorithm

### Problem Statement
A trader has information on bond market offers for a series of days, each including available bond lots with specific prices and quantities. Bonds provide daily coupon payments and nominal repayment at the end of the term. The goal is to determine which lots to buy each day to maximize the trader's profit, given limited funds.

### Input
1. **Trading days (N)**, **Max lots per day (M)**, and **Available funds (S)**.
2. Market data with the day, bond name, price (percentage of nominal), and quantity for each lot.

### Output
1. **Total profit on day N + 30**.
2. List of purchased lots, including day, bond name, price, and quantity.

### Implementation Details

- **Classes**:
  - `Lot`: Represents each bond lot with attributes like `day`, `name`, `price`, and `quantity`.
  - `calculate_profit`: Calculates potential profit for a lot, including daily coupon income and bond nominal repayment.
  
- **Functions**:
  - `parse_input()`: Parses input data to initialize trading days, max lots per day, and available funds, then loads market offers.
  - `select_lots()`: Selects lots for purchase to maximize profit within the available budget.
  - `main()`: Coordinates parsing, selection, and output.

### Complexity
- **Time Complexity**: \(O(N log N)\), dominated by the sorting of lots by profit.
- **Memory Complexity**: \(O(N)\), as we store and process a list of all lots.

### Subjective Difficulty Rating
* Difficulty: 4/10 (moderate complexity)
* Time Spent: Approximately 1 hour to implement and test.

