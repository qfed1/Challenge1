# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations."""

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
total_loans = len(loan_costs)
print(f"There are {total_loans} loans in the list.")

# What is the total of all loans?
total_value = sum(loan_costs)
print(f"The total value of all loans is ${total_value}.")

# What is the average loan amount from the list?
average_loan = total_value / total_loans
print(f"The average loan amount is ${average_loan:.2f}.")

"""Part 2: Analyze Loan Data."""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print(f"Future Value: ${future_value}")
print(f"Remaining Months: {remaining_months}")

discount_rate = 0.2
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"Present Value: ${present_value:.2f}")

if present_value >= loan["loan_price"]:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")

"""Part 3: Perform Financial Calculations."""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    return future_value / (1 + annual_discount_rate/12) ** remaining_months

present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], discount_rate)
print(f"The present value of the loan is: ${present_value:.2f}")

"""Part 4: Conditionally filter lists of loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print("Inexpensive Loans:")
for loan in inexpensive_loans:
    print(loan)

"""Part 5: Save the results."""

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
