"""
Mortgage Payoff Simulator
"""

purchase_price = 277_500
interest_rate = 0.075
loan_term = 360

monthly_payment = 1.00

while True:
    principal = purchase_price

    for _ in range(loan_term):
        interest = (interest_rate / 12) * principal
        principal -= (monthly_payment - interest)

    print(f"Tried ${monthly_payment:,.2f}")
    print(f"Remaining principal: ${principal:,.2f}\n")

    if principal <= 0:
        break

    monthly_payment += 1.00
