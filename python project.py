# Supermarket Billing System

products = {
    "rice": 50,
    "wheat": 40,
    "milk": 30,
    "bread": 25,
    "sugar": 45,
    "oil": 120,
    "eggs": 6
}

cart = {}
total = 0

print("====== Welcome to Supermarket ======")
print("Available Items:\n")

for item, price in products.items():
    print(f"{item} : ₹{price}")

# Taking orders
while True:
    item = input("\nEnter item name (or type 'exit' to finish): ").lower()

    if item == "exit":
        break

    if item in products:
        try:
            qty = int(input("Enter quantity: "))
            
            if qty <= 0:
                print("Quantity must be greater than 0")
                continue

            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty

            total += products[item] * qty

        except:
            print("Invalid quantity! Please enter a number.")

    else:
        print("Item not available in store!")

# Billing section
print("\n========== BILL ==========")

for item, qty in cart.items():
    price = products[item]
    print(f"{item} x {qty} = ₹{price * qty}")

print(f"\nSubtotal = ₹{total}")

# GST Calculation (5%)
gst = total * 0.05
print(f"GST (5%) = ₹{gst:.2f}")

# Discount (10% if total > 500)
discount = 0
if total > 500:
    discount = total * 0.10
    print(f"Discount (10%) = -₹{discount:.2f}")

# Final Total
final_total = total + gst - discount
print(f"\nFinal Amount = ₹{final_total:.2f}")

print("\nThank you for shopping with us!")

# Save bill to file
try:
    file = open("bill.txt", "w")

    file.write("====== Supermarket Bill ======\n\n")
    
    for item, qty in cart.items():
        price = products[item]
        file.write(f"{item} x {qty} = ₹{price * qty}\n")

    file.write(f"\nSubtotal = ₹{total}")
    file.write(f"\nGST (5%) = ₹{gst:.2f}")
    file.write(f"\nDiscount = -₹{discount:.2f}")
    file.write(f"\nFinal Amount = ₹{final_total:.2f}")

    file.close()

    print("\n🧾 Bill saved to 'bill.txt' successfully!")

except:
    print("Error saving bill file.")