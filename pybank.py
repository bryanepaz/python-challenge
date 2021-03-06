{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Date', 'Profit/Losses']\n",
      "['Jan-2010', '867884']\n",
      "1852539\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 2\n",
      "Total: $1852539\n",
      "Average Change: $116771.00\n",
      "Greatest Increase in Profits Feb-2010, ($116771)\n",
      "Greatest Decrese in Profits Feb-2010, ($116771)\n",
      "\n",
      "2174552\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 3\n",
      "Total: $2174552\n",
      "Average Change: $-214550.00\n",
      "Greatest Increase in Profits Feb-2010, ($116771)\n",
      "Greatest Decrese in Profits Mar-2010, ($-545871)\n",
      "\n",
      "2105135\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 4\n",
      "Total: $2105135\n",
      "Average Change: $-455467.00\n",
      "Greatest Increase in Profits Feb-2010, ($116771)\n",
      "Greatest Decrese in Profits Apr-2010, ($-937301)\n",
      "\n",
      "2415638\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 5\n",
      "Total: $2415638\n",
      "Average Change: $-480945.50\n",
      "Greatest Increase in Profits Feb-2010, ($116771)\n",
      "Greatest Decrese in Profits Apr-2010, ($-937301)\n",
      "\n",
      "2938495\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 6\n",
      "Total: $2938495\n",
      "Average Change: $-453761.80\n",
      "Greatest Increase in Profits Feb-2010, ($116771)\n",
      "Greatest Decrese in Profits Apr-2010, ($-937301)\n",
      "\n",
      "3971591\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 7\n",
      "Total: $3971591\n",
      "Average Change: $-350599.50\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Apr-2010, ($-937301)\n",
      "\n",
      "4576476\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 8\n",
      "Total: $4576476\n",
      "Average Change: $-338085.14\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Apr-2010, ($-937301)\n",
      "\n",
      "4360090\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 9\n",
      "Total: $4360090\n",
      "Average Change: $-431358.25\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Sep-2010, ($-1084270)\n",
      "\n",
      "4837622\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 10\n",
      "Total: $4837622\n",
      "Average Change: $-426802.00\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Sep-2010, ($-1084270)\n",
      "\n",
      "5731432\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 11\n",
      "Total: $5731432\n",
      "Average Change: $-381529.20\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Sep-2010, ($-1084270)\n",
      "\n",
      "5651079\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 12\n",
      "Total: $5651079\n",
      "Average Change: $-433048.09\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Sep-2010, ($-1084270)\n",
      "\n",
      "6430885\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 13\n",
      "Total: $6430885\n",
      "Average Change: $-404300.58\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Sep-2010, ($-1084270)\n",
      "\n",
      "6095682\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 14\n",
      "Total: $6095682\n",
      "Average Change: $-465745.69\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "6793527\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 15\n",
      "Total: $6793527\n",
      "Average Change: $-444623.79\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "7586690\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 16\n",
      "Total: $7586690\n",
      "Average Change: $-419963.60\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "8071760\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 17\n",
      "Total: $8071760\n",
      "Average Change: $-417641.75\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "8655882\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 18\n",
      "Total: $8655882\n",
      "Average Change: $-409766.47\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "8718611\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 19\n",
      "Total: $8718611\n",
      "Average Change: $-431732.50\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "9386790\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 20\n",
      "Total: $9386790\n",
      "Average Change: $-419520.53\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "10286696\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 21\n",
      "Total: $10286696\n",
      "Average Change: $-396943.40\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "11121415\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 22\n",
      "Total: $11121415\n",
      "Average Change: $-379620.62\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "11253418\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 23\n",
      "Total: $11253418\n",
      "Average Change: $-395814.27\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "11563396\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 24\n",
      "Total: $11563396\n",
      "Average Change: $-402861.74\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Feb-2011, ($-1203087)\n",
      "\n",
      "10807830\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 25\n",
      "Total: $10807830\n",
      "Average Change: $-453719.58\n",
      "Greatest Increase in Profits Jul-2010, ($165212)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "11978423\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 26\n",
      "Total: $11978423\n",
      "Average Change: $-423462.44\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "12231211\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 27\n",
      "Total: $12231211\n",
      "Average Change: $-430832.96\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "13382729\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 28\n",
      "Total: $13382729\n",
      "Average Change: $-404371.22\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "14199985\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 29\n",
      "Total: $14199985\n",
      "Average Change: $-391737.54\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "14770742\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 30\n",
      "Total: $14770742\n",
      "Average Change: $-388475.10\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "15277444\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 31\n",
      "Total: $15277444\n",
      "Average Change: $-387565.33\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Jan-2012, ($-1623450)\n",
      "\n",
      "14254910\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 32\n",
      "Total: $14254910\n",
      "Average Change: $-436044.45\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "14729972\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 33\n",
      "Total: $14729972\n",
      "Average Change: $-434693.75\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "15509948\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 34\n",
      "Total: $15509948\n",
      "Average Change: $-424185.09\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "15654123\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 35\n",
      "Total: $15654123\n",
      "Average Change: $-432994.62\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "16196617\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 36\n",
      "Total: $16196617\n",
      "Average Change: $-429920.20\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "16555950\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 37\n",
      "Total: $16555950\n",
      "Average Change: $-432104.39\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "16877419\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 38\n",
      "Total: $16877419\n",
      "Average Change: $-435193.86\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "16945199\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 39\n",
      "Total: $16945199\n",
      "Average Change: $-444796.76\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "17416634\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 40\n",
      "Total: $17416634\n",
      "Average Change: $-443557.08\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "17982237\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 41\n",
      "Total: $17982237\n",
      "Average Change: $-440025.17\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "18854717\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 42\n",
      "Total: $18854717\n",
      "Average Change: $-429180.76\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "19644197\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 43\n",
      "Total: $19644197\n",
      "Average Change: $-420828.93\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "20644139\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 44\n",
      "Total: $20644139\n",
      "Average Change: $-407971.09\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Aug-2012, ($-1890418)\n",
      "\n",
      "19447914\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 45\n",
      "Total: $19447914\n",
      "Average Change: $-445610.59\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "19716911\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 46\n",
      "Total: $19716911\n",
      "Average Change: $-449016.73\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "19028925\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 47\n",
      "Total: $19028925\n",
      "Average Change: $-473078.76\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "20179386\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 48\n",
      "Total: $20179386\n",
      "Average Change: $-457000.98\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "20861844\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 49\n",
      "Total: $20861844\n",
      "Average Change: $-451343.17\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "21479700\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 50\n",
      "Total: $21479700\n",
      "Average Change: $-447234.69\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "22303798\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 51\n",
      "Total: $22303798\n",
      "Average Change: $-439165.72\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "22885741\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 52\n",
      "Total: $22885741\n",
      "Average Change: $-436161.31\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "23018605\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 53\n",
      "Total: $23018605\n",
      "Average Change: $-441908.60\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "23466667\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 54\n",
      "Total: $23466667\n",
      "Average Change: $-441491.87\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "24155828\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 55\n",
      "Total: $24155828\n",
      "Average Change: $-436625.78\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "24956529\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 56\n",
      "Total: $24956529\n",
      "Average Change: $-429908.64\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "26123172\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 57\n",
      "Total: $26123172\n",
      "Average Change: $-416896.71\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "27070505\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 58\n",
      "Total: $27070505\n",
      "Average Change: $-408188.89\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "27649173\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 59\n",
      "Total: $27649173\n",
      "Average Change: $-406137.64\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "28637678\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 60\n",
      "Total: $28637678\n",
      "Average Change: $-397209.53\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "29777393\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 61\n",
      "Total: $29777393\n",
      "Average Change: $-386058.85\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "30806864\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 62\n",
      "Total: $30806864\n",
      "Average Change: $-377081.05\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "31494397\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 63\n",
      "Total: $31494397\n",
      "Average Change: $-373907.98\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "30969771\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 64\n",
      "Total: $30969771\n",
      "Average Change: $-390076.27\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "31128391\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 65\n",
      "Total: $31128391\n",
      "Average Change: $-395063.58\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "31216186\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 66\n",
      "Total: $31216186\n",
      "Average Change: $-400987.05\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "31639575\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 67\n",
      "Total: $31639575\n",
      "Average Change: $-401646.26\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "32480298\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 68\n",
      "Total: $32480298\n",
      "Average Change: $-396056.93\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "33048827\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 69\n",
      "Total: $33048827\n",
      "Average Change: $-394634.84\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "33380894\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 70\n",
      "Total: $33380894\n",
      "Average Change: $-396680.96\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "34370393\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 71\n",
      "Total: $34370393\n",
      "Average Change: $-389276.73\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35148630\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 72\n",
      "Total: $35148630\n",
      "Average Change: $-385056.59\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35798630\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 73\n",
      "Total: $35798630\n",
      "Average Change: $-382734.75\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "34698243\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 74\n",
      "Total: $34698243\n",
      "Average Change: $-404454.42\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "34523297\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 75\n",
      "Total: $34523297\n",
      "Average Change: $-413081.12\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35280440\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 76\n",
      "Total: $35280440\n",
      "Average Change: $-409049.92\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35726149\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 77\n",
      "Total: $35726149\n",
      "Average Change: $-409222.62\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "36439110\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 78\n",
      "Total: $36439110\n",
      "Average Change: $-405920.03\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35275313\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 79\n",
      "Total: $35275313\n",
      "Average Change: $-426763.12\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "35845212\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 80\n",
      "Total: $35845212\n",
      "Average Change: $-425133.01\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "36613662\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 81\n",
      "Total: $36613662\n",
      "Average Change: $-421061.78\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "36716347\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 82\n",
      "Total: $36716347\n",
      "Average Change: $-425310.38\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "37512261\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 83\n",
      "Total: $37512261\n",
      "Average Change: $-421001.35\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "37573249\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 84\n",
      "Total: $37573249\n",
      "Average Change: $-425650.69\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "37711479\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 85\n",
      "Total: $37711479\n",
      "Average Change: $-429269.77\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n",
      "38382578\n",
      "\n",
      "Financial Analysis\n",
      "=====================\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-426534.66\n",
      "Greatest Increase in Profits Feb-2012, ($302709)\n",
      "Greatest Decrese in Profits Sep-2013, ($-2064109)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# PyBank\n",
    "\n",
    "# Dependencies\n",
    "import csv\n",
    "import os\n",
    "\n",
    "# Files to load and output\n",
    "file_to_load = os.path.join(\"budget_data.csv\")\n",
    "file_to_output = os.path.join (\"budget_analysis.txt\")\n",
    "\n",
    "#Track varios financial parameters \n",
    "total_months = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999999999999999]\n",
    "total_net = 0\n",
    "\n",
    "# Read the csv andconvert it into a list dictionaries\n",
    "with open(file_to_load) as financial_data:\n",
    "    reader = csv.reader(financial_data)\n",
    "    \n",
    "    # Read the header row\n",
    "    header = next(reader)\n",
    "    print(header)\n",
    "    \n",
    "    # Extract First row to avoid  appendding to net_change _list \n",
    "    first_row = next(reader)\n",
    "    print(first_row)\n",
    "    total_months = total_months + 1\n",
    "    \n",
    "    total_net = total_net + int(first_row[1])\n",
    "    prev_net = int(first_row[1])\n",
    "    # print(total_net)\n",
    "    # print(total_net)\n",
    "    \n",
    "    # loop through your data\n",
    "    for row in reader:\n",
    "        \n",
    "        #track the Total\n",
    "        total_months = total_months + 1\n",
    "        total_net = total_net + int (row[1])\n",
    "        print(total_net)\n",
    "        \n",
    "        #Track the new change \n",
    "        net_change = int(row[1]) - prev_net\n",
    "        Prev_net = int(row[1])\n",
    "        net_change_list = net_change_list + [net_change]\n",
    "        month_of_change = month_of_change + [row[0]]\n",
    "        \n",
    "        if net_change > greatest_increase [1]:\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "            \n",
    "        if net_change < greatest_decrease [1]:\n",
    "            greatest_decrease [0] = row [0]\n",
    "            greatest_decrease [1] = net_change\n",
    "            \n",
    "        # Calculate the Average Net Change\n",
    "        net_monthly_avg = sum (net_change_list) / len(net_change_list)\n",
    "        \n",
    "        output = (\n",
    "            \n",
    "            f\"\\nFinancial Analysis\\n\"\n",
    "            f\"=====================\\n\"\n",
    "            f\"Total Months: {total_months}\\n\"\n",
    "            f\"Total: ${total_net}\\n\"\n",
    "            f\"Average Change: ${net_monthly_avg:.2f}\\n\"\n",
    "            f\"Greatest Increase in Profits {greatest_increase[0]}, (${greatest_increase[1]})\\n\"\n",
    "            f\"Greatest Decrese in Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\\n\" )\n",
    "        \n",
    "        print(output)\n",
    "        \n",
    "             \n",
    "    \n",
    "                                            \n",
    "                                            \n",
    "        \n",
    "        \n",
    "    \n",
    "    \n",
    "                               "
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}