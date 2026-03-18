
from datetime import datetime
from colorama import Fore, Style, init
import csv
import time, sys

init(autoreset=True)

day_total = 0
customers_served = 0

print(Fore.CYAN + "\n========== WELCOME TO SUPER STORE ==========\n")

while True:
    name = input(Fore.YELLOW + "Enter Customer Name: ").title()
    # name = input(Fore.YELLOW + "Enter Customer Mobile No: ").title()
    bill_no = "BILL" + datetime.now().strftime("%d%m%H%M%S")
    total = 0
    items = []

    # Enter items
    while True:
        item_name = input(Fore.GREEN + "Enter item name: ").title()
        try:
            amount = float(input("Enter price (₹): "))
            quantity = float(input("Enter quantity: "))
        except ValueError:
            print(Fore.RED + "❌ Invalid input! Enter numbers only.")
            continue

        total += amount * quantity
        items.append((item_name, amount, quantity, amount * quantity))

        more = input("Add more items? (yes/no): ").lower()
        if more == "no":
            break

    # Coupon system
    discount = 0
    coupon = input(Fore.MAGENTA + "Enter coupon code (SAVE10 / NEWUSER / NONE): ").upper()
    if coupon == "SAVE10":
        discount = 10
    elif coupon == "NEWUSER":
        discount = 5

    discounted_total = total - (total * discount / 100)
    gst = 18
    gst_amount = discounted_total * gst / 100
    final_total = discounted_total + gst_amount

    # Payment Mode
    payment_mode = input("Enter payment mode (Cash/Card/UPI): ").title()

    # Loyalty Points
    loyalty_points = int(final_total // 100)

    # Typing Effect
    for c in "Generating your bill...":
        sys.stdout.write(Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

    # Bill Display
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "              SUPER STORE BILL")
    print(Fore.CYAN + "=" * 50)
    print("Bill No:", bill_no)
    print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Customer:", name)
    # print("Customer:", mobile no)
    print("-" * 50)
    print(f"{'Item':<15}{'Price':<10}{'Qty':<10}{'Total'}")
    print("-" * 50)
    for i in items:
        print(f"{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:.2f}")
    print("-" * 50)
    print(f"Subtotal: ₹{total:.2f}")
    print(f"Discount Applied: {discount}%")
    print(f"GST (18%): ₹{gst_amount:.2f}")
    print(Fore.YELLOW + f"Final Total: ₹{final_total:.2f}")
    print(Fore.BLUE + f"Loyalty Points Earned: {loyalty_points}")
    print("Payment Mode:", payment_mode)
    print(Fore.CYAN + "-" * 50)
    print(Fore.GREEN + "       *** THANK YOU! VISIT AGAIN ***")
    print(Fore.CYAN + "=" * 50)

    # Save individual bill in text file (UTF-8)
    filename = f"{bill_no}_{name}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("SUPER STORE BILL\n")
        f.write("=" * 50 + "\n")
        f.write(f"Bill No: {bill_no}\n")
        f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write(f"Customer: {name}\n")
        f.write(f"Customer: {mobile no}\n")
        f.write("-" * 50 + "\n")
        f.write(f"{'Item':<15}{'Price':<10}{'Qty':<10}{'Total'}\n")
        for i in items:
            f.write(f"{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:.2f}\n")
        f.write("-" * 50 + "\n")
        f.write(f"Subtotal: ₹{total:.2f}\n")
        f.write(f"Discount: {discount}%\n")
        f.write(f"GST (18%): ₹{gst_amount:.2f}\n")
        f.write(f"Final Total: ₹{final_total:.2f}\n")
        f.write(f"Loyalty Points: {loyalty_points}\n")
        f.write(f"Payment Mode: {payment_mode}\n")
        f.write("=" * 50 + "\n")
        f.write("*** THANK YOU! VISIT AGAIN ***\n")

    print(Fore.GREEN + f"\nBill saved as '{filename}'\n")

    # Save in CSV (Sales Report)
    with open("sales_report.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([bill_no, name, f"₹{final_total:.2f}", payment_mode, datetime.now().strftime("%d-%m-%Y %H:%M:%S")])

    day_total += final_total
    customers_served += 1

    again = input(Fore.CYAN + "Next customer? (yes/no): ").lower()
    if again == "no":
        break

# Daily Summary
print(Fore.YELLOW + "\n========== DAILY SALES REPORT ==========")
print(Fore.CYAN + f"Total Customers Served: {customers_served}")
print(Fore.CYAN + f"Total Sales Today: ₹{day_total:.2f}")
print(Fore.GREEN + "******** SHOP CLOSED ********")
print(Fore.CYAN + "==========================================")
