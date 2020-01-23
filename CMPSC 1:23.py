"""
1/23/20
1.Change calculator for small amounts
2.Calculates how many quaters, nickles, and pennies you will receive as change after a purchase
"""

cost = float(input("Enter the cost: $"))
accepted = float(input("Amount inserted: $"))

quater = 0.25
nickle = 0.05
penny = 0.01

change = accepted - cost

quater_change = change // quater
quater_count = quater_change * quater 
change_q = change - quater_count

nickle_change = change_q // nickle
nickle_count = nickle_change * nickle
change_n = change_q - nickle_count

penny_change = change_n // penny
penny_count = penny_change * penny
change_p = change_n - penny_count


print(f"Your change will be ${round(change,2)}")
print(f"You will receive {quater_change} quaters, {nickle_change} nickles, and {penny_change} pennies.")
