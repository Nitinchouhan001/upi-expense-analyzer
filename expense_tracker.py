import pandas as pd
my_statement= "PhonePe_Statement_Apr2026_Aug2026.csv"
df = pd.read_csv(my_statement, skiprows=3)


df.columns = df.columns.str.strip()
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")



debit_data = df[df["Transaction Type"] == "DEBIT"].copy()
debit_data = debit_data.dropna(subset=["Amount"])



def decide_category(name):
  name = str(name).lower()
  if any(x in name for x in ["geu", "university", "college"]):
    return "College Fees"
  elif "physicswallah" in name:
    return "Education"
  elif any(x in name for x in ["filling", "petrol"]):
    return "Fuel"
  elif "recharge" in name:
    return "Recharge"
  elif any(x in name for x in ["swiggy", "zomato", "restaurant", "food"]):
    return "Food & Snacks"
  else:
    return "Other"



debit_data["Category"] = debit_data["Transaction Details"].apply(
    decide_category
)



debit_data["Date"] = pd.to_datetime(debit_data["Date"], errors="coerce")
debit_data["Month"] = debit_data["Date"].dt.strftime("%B %Y")


category_summary = (
    debit_data.groupby("Category")["Amount"].sum().sort_values(ascending=False)
)
print("\n--- Category Wise Total ---")

print(category_summary)


monthly_summary = debit_data.groupby("Month")["Amount"].sum()
print("\n--- Month Wise Spending ---")
print(monthly_summary)


monthly_grid= debit_data.pivot_table(
    index="Month",
    columns="Category",
    values="Amount",
    aggfunc="sum",
    fill_value=0,
)
print("\n--- Month and Category Matrix ---")
print(monthly_grid)


avg_expense = debit_data["Amount"].mean()
high_expenses = debit_data[debit_data["Amount"] > (avg_expense * 3)]



monthly_grid.to_csv("monthly_category_summary.csv")
cols_to_save = ["Date", "Transaction Details", "Amount", "Category"]

high_expenses[cols_to_save].to_csv("big_expenses_clean.csv", index=False)


print("\nDone! Summary and high expenses saved to CSV.")


