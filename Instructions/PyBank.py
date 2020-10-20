# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period

import os
import csv

#Path to collect data
budget_data.csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Initialize Values
MonthCount=0
NetTotal=0
PrevMonth=0
AvgChange=0
IncreaseMonth= ""
DecreaseMonth=""
GreatestIncrease=0
GreatestDecrease=0

#Open and read CSV and skip header
with open(budget_data.csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_file)

        #Read each row
        for row in csv_reader:
            MonthCount+=1
            NetTotal+=int(row[1])

            if MonthCount>1:
                Change=int(row[1])-PrevMonth
                AverageChange+=Change
            if Change>GreatestIncrease:
                IncreaseMonth=row[0]
                GreatestIncrease=Change
            if Change<GreatestDecrease:
                DecreaseMonth=row[0]
                GreatestDecrease=Change

        PrevMonth=int(row[1])
AverageChange=round(AverageChange/(MonthCount-1),2)

#Print Results
print("Financial Analysis \n-------------------\n")
print(f"Total Months: {MonthCount}\n")
print(f"Total: ${NetTotal}\n")
print(f"Average Change: ${AverageChange}\n")
print(f"Greatest Increase in Profits: {IncreaseMonth} [${GreatestIncrease}]\n")
print(f"Greatest Decrease in Profits: {DecreaseMonth} [${GreatestDecrease}]\n")

#Move to Text File
results=open("PyBank/Analysis/results.txt","w")
results.write("Financial Analysis \n-------------------\n")
results.write(f"Total Months: {MonthCount}\n")
results.write(f"Total: ${NetTotal}\n")
results.write(f"Average Change: ${AverageChange}\n")
results.write(f"Greatest Increase in Profits: {IncreaseMonth} [${GreatestIncrease}]\n")
results.write(f"Greatest Decrease in Profits: {DecreaseMonth} [${GreatestDecrease}]\n")
            

