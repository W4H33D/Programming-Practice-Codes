# Assingment Operator
fixed_costs = 300
variable_costs = 100
revenue = 1000

# Addition: Finding total costs
total_costs = fixed_costs + variable_costs

# Subtraction: Calculating Profit
profit = revenue - total_costs

# Multiplication: Projecting revenue if sales double
projected_revenue = revenue * 2

# Power: Projecting exponential growth (e.g., doubling 3 times)
growth_factor = 2 ** 3

# Standard Division: Finding Profit Margin
margin = profit / revenue

# Floor Division: How many full $70 inventory units can we restock?
units_to_buy = profit // 70

# Modulo: How much cash is left over after buying those units?
leftover_cash = profit % 70

# Printing Raw Values
print(total_costs)  # Output: 400
print(profit)  # Output: 600
print(projected_revenue)  # Output: 2000
print(growth_factor)  # Output: 8
print(margin)  # Output: 0.6
print(units_to_buy)  # Output: 8
print(leftover_cash)  # Output: 40

# Handling Strings And It's Formatting
banner = "dashbord section initialized...\n".title() # Method We can use: .title(), .upper(), .lower(), and .capitalize()
dashboard = "------------------------\n" + \
            "Total Cost Of Our Product: " + \
            str(total_costs) + \
            f"\nTotal Profit: {profit}\n" + \
            f"Total Revenue: {projected_revenue} with the " + \
            f"Growth Factor: {growth_factor}\n" + \
            f"Our Margins: {margin}\n" + \
            f"{units_to_buy = }\n" + \
            f"{leftover_cash = }\n" + \
            "------------------------\n"
"""
On line 40 we use Type Casting Method
On line 41 onwards we Formated String Format. Notice the 'f' before every String.
On line 45 and 46 We use f-string debugging introduced in Python 3.8
"""
# Print Formatted Output Using String formating
print(f"{banner}{dashboard.capitalize()}")


