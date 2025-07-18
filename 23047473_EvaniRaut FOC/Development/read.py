def read_land_data(data_file):
    land_record_list = []  # Initialize an empty list to store land records
    try:
        with open(data_file, 'r') as file:  # Open the file in read mode
            for line in file:  # Iterate over each line in the file
                parts = line.strip().split(', ')  # Split the line into parts based on comma and space
                if len(parts) != 6:  # Check if the line has the correct number of parts
                    print("Warning: Incorrect format in line: " + line)  # Print warning for incorrect format
                    continue  # Skip to the next line
                
                # Extract and convert values from parts
                kitta_number = parts[0]
                location = parts[1]
                direction = parts[2]
                area_anna = int(parts[3])  # Convert area_anna to integer
                price = int(parts[4])  # Convert price to integer
                status = parts[5]
                
                try:
                    # Create a dictionary for the land record
                    land_info = {
                        'kitta_number': kitta_number,
                        'location': location,
                        'direction': direction,
                        'area_anna': area_anna,
                        'price': price,
                        'status': status
                    }
                    land_record_list.append(land_info)  # Append the land record to the list
                except ValueError:
                    print("Warning: Invalid data in line: " + line)  # Print warning for invalid data
                    continue  # Skip to the next line
    except FileNotFoundError:
        print("Error: File '" + data_file + "' not found.")  # Print error if the file is not found
    except Exception as e:
        print("Error: " + str(e))  # Print any other exceptions that occur
    return land_record_list  # Return the list of land records

