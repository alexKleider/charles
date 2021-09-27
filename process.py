#!/usr/bin/env python3

# File: process.py

owed = 0
billed = []
paid = 0
payments = []  # negative values
with open('account.txt', 'r') as stream:
    for original_line in stream:
        line = original_line.strip()
        parts = line.split(":")
        print(original_line[:-1])
        try:
            amt = float(parts[1].strip())
        except IndexError:
            continue
        if line.startswith("Subtotal:"):
            billed.append(amt)
            owed += amt
            print("\t\t\t\t\tRunning total: {:,.2f}".format(owed+paid))
        if line.startswith("Payment"):
            payments.append(-amt)
            paid -= amt
            print("\t\t\t\t\tRunning total: {:,.2f}".format(owed+paid))
print("\n\n")
print("\tRECONNING")
print("\t=========\n")
print("\t\tInvoices:")
for amount in billed:
    print("\t\t\t{:,.2f}".format(amount))
print("\t\tTotal billed: {:,.2f}".format(owed))
print()
print("\t\tPayments:")
for amount in payments:
    print("\t\t\t{:,.2f}".format(amount))
print("\t\tTotal paid: {:,.2f}".format(paid))
print()
print("\tOutstanding balance: ${:,.2f}".format(owed+paid))

