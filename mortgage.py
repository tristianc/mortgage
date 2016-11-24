#!/usr/bin/env python3

import argparse


def closing_costs(loan_amt, final_sales_price, points, origination_rate=1, closing_cost_rate=3.5):
    origination_fee = origination_rate / 100.0 * loan_amt
    closing_costs = closing_cost_rate / 100.0 * final_sales_price
    points_prepayment = points / 100.0 * loan_amt
    return float(origination_fee + closing_costs + points_prepayment)


def monthly_payment(loan_amount, rate, points, decrease_per_point, years=30):
    term = years * 12.0
    monthly_rate_decimal = (rate - (points * decrease_per_point)) / 100.0 / 12
    payment = (loan_amount * monthly_rate_decimal * pow((1 + monthly_rate_decimal), term)) / (pow((1 + monthly_rate_decimal), term) - 1)
    return payment


def property_taxes(cost_of_home, annual_property_tax_rate):
    monthly_rate_decimal = annual_property_tax_rate / 100.0 / 12
    return cost_of_home * monthly_rate_decimal


def escrow_payments(months_prepaid_property_tax=12, months_prepaid_insurance=12):
    return 8500.00


def mortgage_info(cost_of_home, percent_of_home_prepaid, mortgage_rate, property_tax_rate, points, decrease_per_point, hoa, assistance, property_insurance):
    loan_amt = cost_of_home * (1 - (percent_of_home_prepaid / 100.0))
    down_payment = cost_of_home * (percent_of_home_prepaid / 100.0)
    cl_costs = closing_costs(loan_amt, cost_of_home, points)
    mn_payment = monthly_payment(loan_amt, mortgage_rate, points, decrease_per_point)
    prop_tax = property_taxes(cost_of_home, property_tax_rate)
    escrow_fee = escrow_payments()

    print("Home Price ($): {}".format(cost_of_home))
    print("Down Payment ($): {}".format(down_payment))
    print("Loan Amount ($): {}".format(loan_amt))
    print("")
    print("Points prepayment ($): {}".format(points / 100.0 * loan_amt))
    print("Closing Costs (Includes points prepayment) ($): {}".format(cl_costs))
    print("Total Closing Costs (As a % of Home Price: {}".format(100.0 * cl_costs / cost_of_home))
    print("Closing Cost Assistance ($): {}".format(assistance))
    print("")
    print("Escrow payment ($): {}".format(escrow_fee))
    print("Total Due At Closing ($): {}".format(cl_costs + down_payment - assistance + escrow_fee))
    print("")
    print("Monthly Mortgage Payment ($ per Month): {}".format(mn_payment))
    print("Property Taxes ($ per Month): {}".format(prop_tax))
    print("HOA Fee ($ per Month): {}".format(hoa))
    print("Property Insurance ($ per Month): {}".format(property_insurance))
    print("Total Monthly Cost ($ per Month): {}".format(mn_payment + prop_tax + hoa + property_insurance))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Produce mortgage information.')
    parser.add_argument('cost_of_home', type=float, help='price of home')
    parser.add_argument('down_payment', type=float, help='percentage of home price covered by down payment')
    parser.add_argument('loan_rate', type=float, help='loan rate expressed as a percent')
    parser.add_argument('property_tax_rate', type=float, help='property tax rate expressed as a percent')
    parser.add_argument('--points', action='store', type=float, default=0.0, help='points')
    parser.add_argument('--decrease-per-point', action='store', type=float, default=0.25, help='percentage that interest rate drops per point')
    parser.add_argument('--hoa', action="store", type=float, default=0.0, help="monthly fee to homeowners association")
    parser.add_argument('--assistance', action="store", type=float, default=0.0, help="closing cost assistance provided by seller")
    parser.add_argument('--property-insurance', action="store", type=float, default=0.0, help="monthly cost of property insurance")

    args = parser.parse_args()
    mortgage_info(args.cost_of_home, args.down_payment, args.loan_rate, args.property_tax_rate, args.points, args.decrease_per_point, args.hoa, args.assistance, args.property_insurance)