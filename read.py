def read_land_data(filename):
    """Reads land records from the text file and returns a list of dictionaries."""
    land_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    land_list.append({
                        'kitta_number': data[0].strip(),
                        'location': data[1].strip(),
                        'direction': data[2].strip(),
                        'anna': data[3].strip(),
                        'price': float(data[4].strip()),
                        'status': 'Available' # Initial status
                    })
        return land_list
    except FileNotFoundError:
        print("Error: land_records.txt not found.")
        return []
