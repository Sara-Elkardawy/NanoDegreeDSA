"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_telemarketers_numbers():
    telemarketers_set = set()
    excluded_numbers = set()
    for text_line in texts:
        excluded_numbers.add(text_line[0])
        excluded_numbers.add(text_line[1])
    for call_line in calls:
        excluded_numbers.add(call_line[1])
    for call_line in calls:
        if call_line[0] not in excluded_numbers:
            telemarketers_set.add(call_line[0])
    return sorted(telemarketers_set)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers_sorted = get_telemarketers_numbers()

print("These numbers could be telemarketers: ")
for t in telemarketers_sorted:
    print (t)

#Time Complexity O(n+m) where n is the length of the calls list (5213)
#Space Complexity O(n+m)
