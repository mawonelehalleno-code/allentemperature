# Temperature Monitor and Alarm Checker

def get_temperature(message):
    while True:
        try:
            temperature = float(input(message))
            return temperature
        except ValueError:
            print("Invalid input! Please enter a number.")


# This function collects five temperature readings.
def collect_readings():
    readings = []

    print("\nEnter five temperature readings in Celsius.")

    while len(readings) < 5:
        temperature = get_temperature(
            f"Enter reading {len(readings) + 1}: "
        )
        readings.append(temperature)

    return readings


# This function checks the temperature readings.
def check_temperature(readings, safe_limit):
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    # Count readings that exceed the safe temperature limit.
    high_readings = 0

    for temperature in readings:
        if temperature > safe_limit:
            high_readings += 1

    # Determine the machine's warning level.
    if high_readings == 0:
        status = "NORMAL"
    elif high_readings <= 2:
        status = "WARNING"
    else:
        status = "CRITICAL"

    # Display the temperature report.
    print("\n========== TEMPERATURE REPORT ==========")
    print("Temperature readings:", readings)
    print(f"Highest temperature: {highest:.2f} °C")
    print(f"Lowest temperature: {lowest:.2f} °C")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Safe temperature limit: {safe_limit:.2f} °C")
    print(f"Readings above safe limit: {high_readings}")
    print(f"Machine status: {status}")

    # Display an appropriate message.
    if status == "NORMAL":
        print("The machine is operating within the safe limit.")
    elif status == "WARNING":
        print("Warning! Some readings are above the safe limit.")
    else:
        print("CRITICAL! The machine may be overheating.")

    print("========================================")


# Main function that runs the program.
def main():
    print("========================================")
    print("   TEMPERATURE MONITOR AND ALARM CHECKER")
    print("========================================")

    safe_limit = get_temperature(
        "\nEnter the safe temperature limit (°C): "
    )

    readings = collect_readings()

    check_temperature(readings, safe_limit)

    print("\nTemperature monitoring completed.")


# Start the program.
if __name__ == "__main__":
    main()