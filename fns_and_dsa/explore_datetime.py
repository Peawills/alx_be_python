from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)


def calculate_future_date():
    """
    Ask user for number of days and calculate future date.
    Print the result in 'YYYY-MM-DD' format.
    """
    try:
        days_to_add = int(
            input("Enter the number of days to add to the current date: ")
        )
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
