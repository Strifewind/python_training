#compute the rate of pay for a job
def computepay(h, r):
    h = float(h)
    r = float(r)
    #computer if overtime
    if h >= 40:
        h = h - 40
        pay = 40 * r
        pay = pay + (h * (1.5 * r))
        return pay
    #else compute normal rate
    else:
        pay = h * r
        return pay

hrs = input("Enter Hours:")
rte = input("Enter Rate of Pay:")

p = computepay(hrs, rte)
print("Pay", p)
