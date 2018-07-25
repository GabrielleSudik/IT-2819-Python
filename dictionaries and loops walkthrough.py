# loops and dictionaries walk-through

phone = {"bob":"123", "mel":"456", "sue":"789"}
print(phone['sue'])
print(phone.keys())
print(phone.values())

for key in phone.keys():
    print(key) #prints key/name
    print(phone[key]) #prints value/number
