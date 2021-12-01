import csv

input = []
with open('input', newline='') as inputfile:
    for row in csv.reader(inputfile):
        input.append(int(row[0]))
newlist =[]
for index,number in enumerate(input):
    if index+2<len(input):
        newlist.append(number+input[index+1]+input[index+2])
input=newlist
previousNumber=input[0]
input = input[1:]
larger=0
smaller=0
same=0
for number in input:
    if(number >previousNumber):
        larger=larger+1
    elif(number<previousNumber):
        smaller=smaller+1
    else:
        same=same+1
    previousNumber=number
print(larger)