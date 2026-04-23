# 🏠 Mortgage Payoff Simulator

A Python-based mortgage analysis tool that simulates loan amortization and determines the minimum monthly payment required to fully pay off a mortgage over time.

---

## 📊 What It Does

This script models a mortgage loan over time and iteratively finds the **minimum monthly payment required to fully amortize the loan**.

Instead of using a formula-only approach, it simulates the loan month-by-month to reflect real-world interest accrual.

---

## 🧠 Key Concepts Demonstrated

- Loan amortization modeling
- Interest compounding (monthly)
- Iterative numerical solving
- Principal reduction tracking
- Basic financial simulation

---

## ⚙️ How It Works

1. Starts with a fixed loan balance
2. Applies monthly interest
3. Subtracts payment toward principal
4. Repeats over loan term
5. Increases payment until loan is fully paid off

---

## 🧾 Example Output


Tried 1,200.00
Remaining principal: 35,412.22

Tried 1,250.00
Remaining principal: 2,118.44

Tried 1,260.00
Remaining principal: -412.10


---

## 🚀 Future Improvements

- Add amortization schedule output
- Build a web UI (Flask or Streamlit)
- Add charts for balance over time
- Compare interest rates side-by-side
- Export results to CSV
