
"""
Assumed Mean Method - Statistical Mean Calculator
================================================
This program calculates the mean using the Assumed Mean Method in statistics.
"""

print("=" * 50)
print("ASSUMED MEAN METHOD - STATISTICAL MEAN CALCULATOR")
print("=" * 50)
print("This program calculates mean using the Assumed Mean Method")
print("-----------You will enter two sets of values--------------")
print("-" * 50)

while True:
    print("\n--- FREQUENCY DATA (fi values) ---")
    a1 = float(input("Enter frequency 1: "))
    a2 = float(input("Enter frequency 2: "))
    a3 = float(input("Enter frequency 3: "))
    a4 = float(input("Enter frequency 4: "))
    a5 = float(input("Enter frequency 5: "))
    a6 = float(input("Enter frequency 6: "))
    a7 = float(input("Enter frequency 7: "))

    sum_fi = a1 + a2 + a3 + a4 + a5 + a6 + a7
    print(f"Sum of frequencies (Σfi): {sum_fi}")

    print("\n--- DEVIATION DATA (fidi values) ---")
    b1 = float(input("Enter fidi value 1: "))
    b2 = float(input("Enter fidi value 2: "))
    b3 = float(input("Enter fidi value 3: "))
    b4 = float(input("Enter fidi value 4: "))
    b5 = float(input("Enter fidi value 5: "))
    b6 = float(input("Enter fidi value 6: "))
    b7 = float(input("Enter fidi value 7: "))

    sum_fidi = b1 + b2 + b3 + b4 + b5 + b6 + b7
    print(f"Sum of fidi values (Σfidi): {sum_fidi}")

    p = float(input("\nEnter the assumed mean (A): "))

    print(f"\n--- RESULT ---")
    print(f"Calculated Mean using Assumed Mean Method: {p + (sum_fidi / sum_fi)}")

    again = input("Do you want to run again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break

    # I used Cursor AI for solving some problems. I only used it a little bit.