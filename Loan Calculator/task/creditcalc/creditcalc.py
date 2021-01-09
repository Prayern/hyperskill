import argparse
import math

#parser initialization
parser = argparse.ArgumentParser()
parser.add_argument("--type",
                    choices= ["annuity", "diff"])
parser.add_argument("--payment",
                    type = int)
parser.add_argument("--principal",
                    type = int)
parser.add_argument("--periods",
                    type = int)
parser.add_argument("--interest",
                    type = float)

args = parser.parse_args()

# exceptions
if args.type not in ["diff", "annuity"]:
    print("Incorrect parameters.")
    quit()
if args.interest is None:
    print("Incorrect parameters.")
    quit()
if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters.")
    quit()
if len(vars(args)) < 4:
    print("Incorrect parameters.")
    quit()

# body
if args.type == "diff":
    num = args.periods
    total_pay = 0
    for i in range(1, num + 1):
        month_pay = args.principal / num + args.interest / 1200 * (args.principal - args.principal * (i - 1) / num)
        month_pay = math.ceil(month_pay)
        total_pay += month_pay
        print(f"Month {i}: payment is {month_pay}")
    print()
    overpay = total_pay - args.principal
    print(f"Overpayment = {overpay}")

if args.type == "annuity":
    if args.principal == None:
        principal = args.payment / (args.interest / 1200 * (pow((1 + args.interest / 1200), args.periods))/(pow((1 + args.interest / 1200), args.periods) - 1))
        principal = math.ceil(principal)
        print(f"Your loan principal = {principal}!")
        overpay = args.payment * args.periods - principal
        print(f"Overpayment = {overpay}")
    if args.payment == None:
        payment = args.principal * (args.interest / 1200 * (pow((1 + args.interest / 1200), args.periods))/(pow((1 + args.interest / 1200), args.periods) - 1))
        payment = math.ceil(payment)
        print(f"Your annuity payment = {payment}!")
        overpay = payment * args.periods - args.principal
        print(f"Overpayment = {overpay}")
    if args.periods == None:
        num = math.log((args.payment / (args.payment - args.interest / 1200 * args.principal)), (1 + args.interest / 1200))
        num = math.ceil(num)
        if num == 1:
            print("It will take 1 month to repay this loan!")
        elif num < 12:
            print(f"It will take {num} months to repay this loan!")
        elif num == 12:
            print("It will take 1 year to repay this loan!")
        elif num % 12 == 0:
            num_years = num // 12
            print(f"It will take {num_years} years to repay this loan!")
        else:
            num_years = num // 12
            num_months = num % 12
            print(f"It will take {num_years} years and {num_months} months to repay this loan!")
        overpay = args.payment * num - args.principal
        print(f"Overpayment = {overpay}")
