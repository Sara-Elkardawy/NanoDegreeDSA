"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_call_prefix(number):
    prefix = ""
    if number.startswith("(0"):
        prefix = number[1:number.index(")")]
    elif number.startswith("140"):
        prefix = "140"
    elif number.startswith("7") or number.startswith("8") or number.startswith("9"):
        prefix = number[:4]
    return prefix

def get_receiving_prefixes_from_area(area_code):
    prefixes = set()
    same_area_num = 0
    all_calls = 0
    for call_line in calls:
        if call_line[0].startswith(area_code):
            prefix = get_call_prefix(call_line[1])
            if "("+prefix+")" == area_code:
                same_area_num +=1
            all_calls +=1
            prefixes.add(prefix)

    #print("same_area_num = {} , all_calls= {}".format(same_area_num, all_calls))
    percentage = float ((same_area_num / all_calls)*100)
    return sorted(prefixes), percentage

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

prefixes_sorted, percentage = get_receiving_prefixes_from_area('(080)')

print("The numbers called by people in Bangalore have codes:")
for p in prefixes_sorted:
    print (p)

formatted_percentage = "{:.2f}".format(percentage)
print ("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(formatted_percentage))

#Time Complexity O(n) where n is the length of the calls list (5213)
#Space Complexity O(n)
