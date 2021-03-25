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


def get_len_distinct_numbers():
    numbers_set = set()
    for text_line in texts:
        numbers_set.add(text_line[0])
        numbers_set.add(text_line[1])
    for call_line in calls:
        numbers_set.add(call_line[0])
        numbers_set.add(call_line[1])
    return len(numbers_set)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
print("There are {} different telephone numbers in the records.".format(get_len_distinct_numbers()))

#Time Complexity O(n+m) where n,m are the lengths of lists (9072, 5213)
#Space Complexity O(2(n+m)) where n,m are the lengths of lists (9072, 5213) and in the worst case the set length is n+m
