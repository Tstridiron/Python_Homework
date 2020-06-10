import os
import csv

#Create the CSV path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Declaring varibles
total_months = 0
total_profit = 0
months = []
profit = []
profit_diff = []


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        
        #Calculate the total months and append to list
        months.append(row[0])
        total_months = total_months + 1

        #Calculate the total profit
        total_profit = total_profit + int(row[1])
        profit.append(int(row[1]))

#Loop through to find the difference between two months
for i in range(len(profit)-1):
        
        # Find the difference between two months and append to profit difference list
        profit_diff.append(profit[i+1] - profit[i])
        
#Find the max and min of profit difference + month
max_increase = max(profit_diff)
max_month = profit_diff.index(max(profit_diff)) + 1
min_increase = min(profit_diff)
min_month = profit_diff.index(min(profit_diff)) + 1

# Print "Financial Analysis"
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {(total_months)}")
# print(f"Total: ${(total_profit)}")
# print(f"Average Change: ${round(sum(profit_diff)/len(profit_diff),2)}")
# print(f"Greatest Increase in Profits: {months[max_month]} (${(str(max_increase))})")
# print(f"Greatest Decrease in Profits: {months[min_month]} (${(str(min_increase))})")

# Output 
output_file = os.path.join("Financial_Analysis.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

#Write rows in csv
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {(total_months)}"])
    writer.writerow([f"Total: ${(total_profit)}"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Average Change: ${round(sum(profit_diff)/len(profit_diff),2)}"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Greatest Increase in Profits: {months[max_month]} (${(str(max_increase))})"])
    writer.writerow([f"Greatest Decrease in Profits: {months[min_month]} (${(str(min_increase))})"])
    writer.writerow(["----------------------------"])


