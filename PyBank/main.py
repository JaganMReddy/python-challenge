import os
import csv

# declare vaiables to store the result needed 
total_number_of_months = 0
total_net_amount = 0.00
total_profitloss_amount = 0.00
average_profitloss_amount = 0.00
net_profitloss_amount = 0.00
greatest_increase_month = "Month"
greatest_decrease_month = "Month"
greatest_increase_amount = 0.00
greatest_decrease_amount = 0.00
previous_revenue = 0.00

# Currency converter into readable format
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# oepn the file
with open("C:\\Users\\HZ3903\\UTAUS201807DATA2\\homework-instructions\\03-Python-Instructions\\Instructions\\PyBank\\Resources\\budget_data.csv") as infile:
    reader = csv.reader(infile)  
    
    next(reader, None)  # skip the headers
    
    for row in reader: # process each row of the input
        date = row[0]
        revenue = row[1]

        total_number_of_months = total_number_of_months + 1
        
        total_net_amount = total_net_amount + float(revenue)
        
        if total_number_of_months > 1 : # ignore the first data row for the change
           total_profitloss_amount = total_profitloss_amount + float(revenue) - float(previous_revenue)
            
        if float(revenue) - float(previous_revenue) > float(greatest_increase_amount) :
           greatest_increase_amount = float(revenue) - float(previous_revenue)
           greatest_increase_month = date
        

        if float(revenue) - float(previous_revenue ) < float(greatest_decrease_amount) :
           greatest_decrease_amount = float(revenue) - float(previous_revenue)
           greatest_decrease_month = date
        
        previous_revenue = float(revenue)
    
    average_profitloss_amount = total_profitloss_amount / (total_number_of_months - 1) 
                
#   display output on the terminal        
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months : " + str(total_number_of_months))
    print("Total : " + as_currency(total_net_amount))
    print("Average profit/loss : " + as_currency(float(average_profitloss_amount)))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " (" + as_currency(greatest_increase_amount) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " (" +as_currency(greatest_decrease_amount) + ")")

#   open file       
    file = open("PyBank_Output_new8.txt", "a+")

#   write to the file
    file.write("Financial Analysis" + "\n" )
    file.write("-----------------------------" + "\n")
    file.write("Total Months : " + str(total_number_of_months) + "\n")
    file.write("Total : " + as_currency(total_net_amount) + "\n")
    file.write("Average profit/loss : " + as_currency(float(average_profitloss_amount)) + "\n")
    file.write("Greatest Increase in Profits: " + str(greatest_increase_month) + " (" + as_currency(greatest_increase_amount) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " (" + as_currency(greatest_decrease_amount) + ")" + "\n")

#   close the file      
    file.close()
    

   
            
   