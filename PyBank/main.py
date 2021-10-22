import os
import csv

PyBank_csv = os.path.join("Resources","budget_data.csv")

profit = []
monthly_changes = []
date = []
 
count = 0
total_profit = 0
total_change_profits = 0
start_profit = 0

with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
      count = count + 1 

      date.append(row[0])

      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      end_profit = int(row[1])
      monthly_change_profits = end_profit - start_profit

      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      start_profit = end_profit

      average_change = (total_change_profits/count)
      
      greatest_increase = max(monthly_changes)
      greatest_decrease = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase)]
      decrease_date = date[monthly_changes.index(greatest_decrease)]
      
    print("Financial Analysis")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")")

with open('main.py.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")
