string=input("Enter any value: ")
character=input("Enter the letter which is there in the value: ")#To count how many times it has been occurred
count=0
for i in string:
    if i==character:
        count=count+1
print(count)
