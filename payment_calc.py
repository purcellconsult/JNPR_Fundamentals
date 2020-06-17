## Auto Loan Calculator ##

"""
A = P x (1 + r) ^N / (1 + r)^N – 1
Formula for calculating the accrued interest:
A = P(1 + rt)
The first formula looks tricky but it’s simple once you
know what all of the variables represent. Here’s a quick
overview:
 P = Principal or the amount owned on a loan.
 A = Total accrued amount (principal + interest).
 r = Rate of interest per year as a decimal, or interest
rate / 100.
 N = Number of months in the loan period.

"""
print ("Welcome to loan sample calculator ... think  twice before you get your self into dept\n")

def remaining_amount():
    car_price = float(input("What is the car MSRP price: "))
    down_payment = float(input("How much you will pay upfront: "))
    remaining_cash = car_price - down_payment
    return remaining_cash

def payment_cal():
    remaining_cash = remaining_amount()
    bank_rate = float(input("Enter the bank rate: "))
    no_months = int(input("For how many monthes this will last : "))
    r_month = (bank_rate/100)/ 12
    r_nemo = r_month * (1+r_month) ** no_months
    r_demo = (1+r_month) ** no_months - 1
    monthly_payment = remaining_cash * (r_nemo/r_demo)
    total_payment = monthly_payment * no_months
    print("Your car total payment is :",total_payment," for ",r_month, "months with monthly payment: ",monthly_payment)


payment_cal()

## check this ....
