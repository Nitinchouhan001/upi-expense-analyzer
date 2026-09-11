My PhonePe Expense Analyzer

I built this simple Python script to track and understand my monthly expenses from my PhonePe UPI statements. Instead of checking everything manually, I used Pandas to automate the boring parts.

# What it does:
* Cleans the messy bank statement CSV and fixes data types.
* Automatically sorts my spending into categories (College Fees, Education, Food, Fuel, etc.) using keywords.
* Calculates total spending month-by-month and category-by-category.
* Uses a pivot table to show a clear monthly spending matrix.
* Finds unusually high expenses (transactions 3x higher than my average spend) and saves them into a separate file.

# Built with:
* Python
* Pandas
