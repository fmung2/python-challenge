# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

def total_rev(numbers):
    length = len(numbers)
    total = 0.0
    #rev = 0.0
    for number in numbers:
        total += int(number)
    return total 
	
def average_list(numbers):
    Diff = []
    for i in range(1, len(numbers)):
	    Diff.append(int(numbers[i]) - int(numbers[i-1]))
    return Diff    

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
	
def greatest_inc(lst):
    words = []
    for word in lst:
        if len(word) > 5:
           words.append(word)
    return words


	
bank_data = dict.fromkeys(['Date', 'Revenue', 'Month', 'Year'])
Data_List = [] 
Date_List = []
Rev_List = []
csvpath = os.path.join('..','PyBank', 'budget_data_1.csv')
csvpath2 = os.path.join('..','PyBank', 'budget_data_2.csv')
# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    next(csvfile, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        Date_List.append(row[0])
		
with open(csvpath, newline='') as csvfile2:
    next(csvfile2, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.reader(csvfile2, delimiter=',')

    #print(csvreader2)
    #  Each row is read as a row
	
    for row in csvreader2:
        Rev_List.append(row[1])
				
		
with open(csvpath2, newline='') as csvfile3:
    next(csvfile3, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader3 = csv.reader(csvfile3, delimiter=',')

    #print(csvreader3)

    #  Each row is read as a row
    for row in csvreader3:
        Date_List.append(row[0])

with open(csvpath2, newline='') as csvfile4:
    next(csvfile4, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader4 = csv.reader(csvfile4, delimiter=',')

    #print(csvreader4)

    #  Each row is read as a row
    for row in csvreader4:
        Rev_List.append(row[1])		
		
 
		

#b = sum(int(i) for i in row[1])
#print(b)
#b = ([float(i) for i in Data_List[1]])

#print(Date_List)
#print(Rev_List)
print("Total Months: " + str(len(Rev_List)))
print("Total Revenue: $" + str(total_rev(Rev_List)))
print("Average Revenue Change: $" + str(average(average_list(Rev_List))))
#print(max(average_list(Rev_List)))
print ("Greatest Increase in Revenue: " + str(Date_List[average_list(Rev_List).index(max(average_list(Rev_List)))+1]) 
       + " ($" + str(max(average_list(Rev_List))) + ")")
print ("Greatest Decrease in Revenue: " + str(Date_List[average_list(Rev_List).index(min(average_list(Rev_List)))+1]) 
       + " ($" + str(min(average_list(Rev_List))) + ")")
f = open('PyBank.txt','w')
f.write("Total Months: " + str(len(Rev_List)) + "\n")
f.write("Total Revenue: $" + str(total_rev(Rev_List)) + "\n")
f.write("Average Revenue Change: $" + str(average(average_list(Rev_List))) + "\n")
#print(max(average_list(Rev_List)))
f.write ("Greatest Increase in Revenue: " + str(Date_List[average_list(Rev_List).index(max(average_list(Rev_List)))+1]) 
       + " ($" + str(max(average_list(Rev_List))) + ")\n")
f.write ("Greatest Decrease in Revenue: " + str(Date_List[average_list(Rev_List).index(min(average_list(Rev_List)))+1]) 
       + " ($" + str(min(average_list(Rev_List))) + ")\n")
f.close()
