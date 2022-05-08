hrs = input("Enter Hours:")
rte = input("Enter Rate:")

#convert input to float
h = float(hrs)
r = float(rte)

#calculate rate for standard time
if h<40:
    pay=h*r

# calculate rate for overtime
elif h>40:
    ovt=h-40
    otr=r*1.5
    otp=otr*ovt
    pay=otp+(40*r)

#print out pay
print(pay) 