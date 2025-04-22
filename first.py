def main():
    total_rain = 0.0
    total_wind = 0.0
    day_count = 0

    print("Enter the rainfall (in inches) and wind speed (in mph) for each day.")
    print("Enter -1.0 to stop.")

    while True:
        rain_input = input("Enter rainfall (or -1.0 to end): ")
        try:
            rain = float(rain_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if rain == -1.0:
            break

        try:
            wind = float(input("Enter wind speed: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        total_rain += rain
        total_wind += wind
        day_count += 1

    if day_count > 0:
        avg_rain = total_rain / day_count
        avg_wind = total_wind / day_count
        severity = (avg_rain * 10) + avg_wind

        print("\nThe average rain is {:.1f} inches".format(avg_rain))
        print("The average wind is {:.1f} mph".format(avg_wind))
        print("The weather severity for these {} readings is: {:.1f}".format(day_count, severity))
    else:
        print("No data entered.")

main()