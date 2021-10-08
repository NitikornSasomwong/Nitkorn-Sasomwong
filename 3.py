#3. Assume that I go and back from BKK - CNX by Nokair in odd day

day = 365 #the numbers of days in 2021
Oddday = 0

for Day in range(1,365):
        if Day % 2 == 1:
            Oddday +=1
print("The numbers of day in 2021 that I would travel with Nokairs", Oddday)

