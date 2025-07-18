from datetime import datetime
from read import read_land_data
from write import write_land_data
from operation import land_rental,land_return

def show_menu():
    # Print the menu header
    print("\n" + "_"*53)
    print(" " * 12 + "Land Rental Management System")
    print("_"*53)
    
    # Define and print menu options
    menu_choices = [
        "1. Display available lands",
        "2. Rent a land",
        "3. Return a land",
        "4. Exit"
    ]
    
    for option in menu_choices:
        print(option)

def main():
    data_file = 'land_data.txt'
    
    # Check if data file exists
    try:
        with open(data_file, 'r') as file:
            pass  # File exists and is accessible
    except FileNotFoundError:
        print("Land data file not found.")
        return

    try:
        # Read land records from the file
        land_record_list = read_land_data(data_file)
    except Exception as e:
        # Print error message if reading data fails
        print("Error reading land data: " + str(e))
        return
    
    while True:
        # Display the menu and get user's choice
        show_menu()
        select_choice = input("Enter your choice: ")
        
        if select_choice == '1':
            # Filter and display available lands
            land_availability = [land for land in land_record_list if land['status'] == 'Available']
            if not land_availability:
                print("No lands available for rent.")
            else:
                for land in land_availability:
                    print("Kitta Number: " + land['kitta_number'])
                    print("Location: " + land['location'])
                    print("Direction: " + land['direction'])
                    print("Area (in anna): " + str(land['area_anna']) + " anna")
                    print("Price: " + str(land['price']) + " NPR")
                    print("=" * 20)
        elif select_choice == '2':
            while True:  # For multiple rentals
                try:
                    # Get rental details and process rental
                    kitta_number = input("Enter the kitta number of the land to rent: ")
                    renter_name = input("Enter the renter's name: ")
                    rental_duration = int(input("Enter the rental duration (months): "))
                    if land_rental(land_record_list, kitta_number, renter_name, rental_duration):
                        write_land_data(data_file, land_record_list)
                    else:
                        print("Unable to rent land. Please check the availability.")
                except ValueError:
                    # Handle invalid rental duration input
                    print("Invalid input for rental duration. Please enter a number.")
                
                # Ask if the user wants to rent another land
                another_rent = input("Do you want to rent another land? (yes/no): ")
                if another_rent == 'no':
                    break  # Exit the loop if the user does not want to rent another land
        elif select_choice == '3':
            try:
                # Get return details and process return
                kitta_number = input("Enter the kitta number of the land to return: ")
                renter_name = input("Enter the renter's name: ")
                rental_duration = int(input("Enter the rental duration (months): "))
                return_date_str = input("Enter the return date (YYYY-MM-DD): ")

                return_date = datetime.now()
                
                if land_return(land_record_list, kitta_number, renter_name, rental_duration, return_date):
                    write_land_data(data_file, land_record_list)
                else:
                    print("Unable to return land. Please check the kitta number and rental details.")
            except ValueError as e:
                # Handle invalid return details input
                print("Invalid input: " + str(e))
        elif select_choice == '4':
            # Exit the program
            print("Exiting the program.")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

main()
