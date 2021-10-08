#2. apply "while" or "for" loop to count number of monday in this year(2021)
day = 3
Num_monday = 0
while day <= 365:
    day = day + 7
    Num_monday += 1
print("the number of monday in this year is",Num_monday)