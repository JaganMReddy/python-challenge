{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "-----------------------------\n",
      "Total Months : 41\n",
      "Total : $18971412.0\n",
      "Average profit/loss : $-6594.12\n",
      "Greatest Increase in Profits: Feb-16 ($1837235.0)\n",
      "Greatest Decrease in Profits: Aug-14 ($-1779747.0)\n",
      "All done\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "# declare vaiables to store the result needed \n",
    "total_number_of_months = 0\n",
    "total_net_amount = 0.00\n",
    "total_profitloss_amount = 0.00\n",
    "average_profitloss_amount = 0.00\n",
    "net_profitloss_amount = 0.00\n",
    "greatest_increase_month = \"Month\"\n",
    "greatest_decrease_month = \"Month\"\n",
    "greatest_increase_amount = 0.00\n",
    "greatest_decrease_amount = 0.00\n",
    "previous_revenue = 0.00\n",
    "\n",
    "\n",
    "# oepn the file\n",
    "with open(\"C:\\\\Users\\\\HZ3903\\\\UTAUS201807DATA2\\\\homework-instructions\\\\03-Python-Instructions\\\\Instructions\\\\PyBank\\\\Resources\\\\budget_data.csv\") as infile:\n",
    "    reader = csv.reader(infile)  \n",
    "    \n",
    "    next(reader, None)  # skip the headers\n",
    "    \n",
    "    for row in reader: # process each row of the input\n",
    "        date = row[0]\n",
    "        revenue = row[1]\n",
    "\n",
    "        total_number_of_months = total_number_of_months + 1\n",
    "        \n",
    "        total_net_amount = total_net_amount + float(revenue)\n",
    "        \n",
    "        if total_number_of_months > 1 : # ignore the first data row for the change\n",
    "           total_profitloss_amount = total_profitloss_amount + float(revenue) - float(previous_revenue)\n",
    "            \n",
    "        if float(revenue) - float(previous_revenue) > float(greatest_increase_amount) :\n",
    "           greatest_increase_amount = float(revenue) - float(previous_revenue)\n",
    "           greatest_increase_month = date\n",
    "        \n",
    "\n",
    "        if float(revenue) - float(previous_revenue ) < float(greatest_decrease_amount) :\n",
    "           greatest_decrease_amount = float(revenue) - float(previous_revenue)\n",
    "           greatest_decrease_month = date\n",
    "        \n",
    "        previous_revenue = float(revenue)\n",
    "        average_profitloss_amount = total_profitloss_amount / total_number_of_months\n",
    "        average_profitloss_amount = format(average_profitloss_amount, '.2f')\n",
    "        \n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"-----------------------------\")\n",
    "    print(\"Total Months : \" + str(total_number_of_months))\n",
    "    print(\"Total : $\" + str(total_net_amount))\n",
    "    print(\"Average profit/loss : $\" + str(float(average_profitloss_amount)))\n",
    "    print(\"Greatest Increase in Profits: \" + str(greatest_increase_month) + \" ($\" + str(greatest_increase_amount) + \")\")\n",
    "    print(\"Greatest Decrease in Profits: \" + str(greatest_decrease_month) + \" ($\" + str(greatest_decrease_amount) + \")\")\n",
    "    \n",
    "    file = open(\"PyBank_Output_new7.txt\", \"a+\")\n",
    "#    file.closed   \n",
    "#    file = open(\"PyBank_Output_new5.txt\", \"w\")\n",
    "    file.write(\"Financial Analysis\" + \"\\n\" )\n",
    "    file.write(\"-----------------------------\" + \"\\n\")\n",
    "    file.write(\"Total Months : \" + str(total_number_of_months) + \"\\n\")\n",
    "    file.write(\"Total : $\" + str(total_net_amount) + \"\\n\")\n",
    "    file.write(\"Average profit/loss : $\" + str(float(average_profitloss_amount)) + \"\\n\")\n",
    "    file.write(\"Greatest Increase in Profits: \" + str(greatest_increase_month) + \" ($\" + str(greatest_increase_amount) + \")\" + \"\\n\")\n",
    "    file.write(\"Greatest Decrease in Profits: \" + str(greatest_decrease_month) + \" ($\" + str(greatest_decrease_amount) + \")\" + \"\\n\")\n",
    "    \n",
    "    file.closed\n",
    "    print(\"All done\")\n",
    "\n",
    "   \n",
    "            \n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
