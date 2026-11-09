# CTE123 Python Mini Project
# Project: Temperature Monitor and Alarm Checker
# Author: Mawoneleh Allen Junior

# Function to collect five temperature readings
def get_temperature_readings():
    readings = []

    print("\nEnter 5 machine temperature readings.")

    while len(readings) < 5:
        try:
            temperature = float(
                input(f"Enter temperature reading {len(readings) + 1}: ")
            )

            if temperature < 0:
                print("Invalid reading. Temperature cannot be negative.")
            else:
                readings.append(temperature)

        except ValueError:
            print("Invalid input! Please enter a number.")

    return readings


# Function to analyse the temperature readings
def analyse_temperature(readings):

    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    safe_limit = 80

    print("\n========== TEMPERATURE REPORT ==========")

    print("All readings:", readings)
    print("Highest temperature:", highest, "°C")
    print("Lowest temperature:", lowest, "°C")
    print("Average temperature:", round(average, 2), "°C")

    # Check whether any reading exceeds the safe limit
    for temperature in readings:
        if temperature > safe_limit:
            print("ALARM! Temperature exceeds the safe limit!")
            break
    else:
        print("All readings are within the safe limit.")

    # Original feature: Machine condition status report
    if highest <= 60:
        print("Machine Status: NORMAL")
    elif highest <= safe_limit:
        print("Machine Status: WARNING")
    else:
        print("Machine Status: CRITICAL")


# Main program
def main():

    print("====================================")
    print(" TEMPERATURE MONITORING SYSTEM")
    print("====================================")

    readings = get_temperature_readings()

    analyse_temperature(readings)

    print("\nTemperature monitoring completed.")


# Run the program
main()
