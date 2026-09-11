# Task 2 - Stock Portfolio Tracker
## 📌 Project Overview
The Stock Portfolio Tracker is a Python-based application developed as part of the CodeAlpha Python Programming Internship. It allows users to manage a simple stock portfolio by entering stock names and quantities and calculates the total investment based on predefined stock prices.
## 🎯 Objective
The objective of this project is to build a simple stock tracking application using Python dictionaries, user input, arithmetic operations, functions, and file handling.
## ✨ Features
- Predefined stock prices using a Python dictionary
- Multiple stock entries
- Stock quantity management
- Automatic investment calculation
- Total portfolio investment calculation
- Input validation
- Portfolio summary display
- Portfolio report generation
- Saves the portfolio report as a `.txt` file
- Menu-driven console interface
## 🛠️ Technologies Used
- Python 3
- Dictionary
- Lists
- Strings
- Functions
- Loops
- If-Else Statements
- Input Validation
- File Handling
## 📊 Predefined Stocks
The application uses manually defined stock prices such as:
- AAPL - $180
- TSLA - $250
- GOOGL - $150
- AMZN - $185
- MSFT - $420
## ⚙️ How It Works
1. The program displays the available stocks and their predefined prices.
2. The user selects a stock and enters the required quantity.
3. The selected stock is added to the portfolio.
4. The program calculates the investment using:
   `Investment = Stock Price × Quantity`
5. Users can add multiple stocks to their portfolio.
6. The complete portfolio and total investment value are displayed.
7. The user can save the portfolio details as a text report.
## 📋 Example
If the user purchases:
- AAPL: 5 shares × $180 = $900
- TSLA: 2 shares × $250 = $500
Then:
**Total Investment = $1400**
## 📂 Project Structure
```text
Task2_Stock_Portfolio_Tracker/
├── stock_tracker.py
├── portfolio_report.txt
└── README.md
