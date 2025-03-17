import datetime

s=datetime.datetime.now()
t=s.date()
p=s.time()
o=t.strftime("%d/%m/%Y") #to print date in your format

j=t.strftime("%d/%m/%Y  %A") #A will tell us about the day


print(t)
print(p)
print(o)
print(j)
h=t.strftime("%d-%m-%Y")   #date in days month and year format
n=p.strftime("%H:%M:%S")   #time in hr min and sec
m=p.strftime("%H:%M:%S %p") # time in hr min and sec and p is for am pm
j=p.strftime("%I:%M:%S %p") # i is for interval time(means 12 ke bad 13 na hokr 1 aana)
print(h)
print(n)
print(m)
print(j)
