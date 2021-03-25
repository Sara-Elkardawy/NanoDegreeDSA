"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#def remove_space_brackets(string):
#    return string.replace(" ", "").replace("(","").replace(")","")

def get_max_call():
    numbers_dic = dict()
    max_call = None
    max_number = None

    for call_line in calls:
        num1 = call_line[0]
        num2 = call_line[1]
        duration = int(call_line[3])
        if numbers_dic.get(num1) is None:
            numbers_dic[num1] = call_line[3]
        else:
            numbers_dic[num1] = int(numbers_dic[num1]) + duration

        if numbers_dic.get(num2) is None:
            numbers_dic[num2] = call_line[3]
        else:
            numbers_dic[num2] = int(numbers_dic[num2]) + duration

    for key, value in numbers_dic.items():
        if max_number is None or int(value) > int(max_call):
            max_number = key
            max_call = value

    #print("Max duration= {} for the number {}".format(max_call, max_number))
    return (max_number, max_call)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
(max_number, max_call) = get_max_call()
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_number, max_call))

#Time Complexity O(n) where n is the length of the calls list (5213)
#and if all numbers (calling and receiving) are distinct the dictionary length is 2n (worst case) so == O(n)
#Space Complexity O(n)
