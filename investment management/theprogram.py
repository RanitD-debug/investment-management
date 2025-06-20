def get_machine_data(machine_num):
    print(f"\nEnter details for Machine {machine_num}:")
    price = float(input("Machine Price (in INR): "))
    depreciation = float(input("Depreciation over 5 years (in INR): "))
    maintenance = float(input("Annual Maintenance Cost (in INR): "))
    setup = float(input("One-time Setup Cost (in INR): "))
    servicing = float(input("Annual Servicing Cost (in INR): "))
    end_value = float(input("Expected Value at the end of 5 years (in INR): "))

    return {
        "price": price,
        "depreciation": depreciation,
        "maintenance": maintenance,
        "setup": setup,
        "servicing": servicing,
        "end_value": end_value
    }

def calculate_conditions(machine):
    condition1 = machine["price"] - machine["depreciation"] - machine["end_value"]
    condition2 = (machine["maintenance"] + machine["servicing"]) * 5 + machine["setup"]
    return condition1, condition2

def compare_machines(machine1, machine2):
    m1_c1, m1_c2 = calculate_conditions(machine1)
    m2_c1, m2_c2 = calculate_conditions(machine2)

    print("\n--- Comparison Summary ---")
    print(f"Machine 1 - Condition 1 Value: {m1_c1:.2f}, Condition 2 Value: {m1_c2:.2f}")
    print(f"Machine 2 - Condition 1 Value: {m2_c1:.2f}, Condition 2 Value: {m2_c2:.2f}")

    score1 = 0
    score2 = 0

    if m1_c1 < m2_c1:
        score1 += 1
    else:
        score2 += 1

    if m1_c2 < m2_c2:
        score1 += 1
    else:
        score2 += 1

    print("\n--- Final Recommendation ---")
    if score1 > score2:
        print("Machine 1 is the better investment based on the analysis.")
    elif score2 > score1:
        print("Machine 2 is the better investment based on the analysis.")
    else:
        print("Both machines are equal in terms of investment value. You can decide based on other factors.")

def main():
    print("Welcome to the Investment Decision Chatbot - Machine Comparison Tool")
    machine1 = get_machine_data(1)
    machine2 = get_machine_data(2)
    compare_machines(machine1, machine2)

if __name__ == "__main__":
    main()
