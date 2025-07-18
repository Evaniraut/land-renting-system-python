def write_land_data(data_file, land_record_list):
    # Open the file in write mode
    with open(data_file, 'w') as file:
        # Iterate over each land record
        for land_info in land_record_list:
            # Format and write each land record to the file
            line = (str(land_info['kitta_number']) + ', ' + 
                    land_info['location'] + ', ' + 
                    land_info['direction'] + ', ' + 
                    str(land_info['area_anna']) + ', ' + 
                    str(land_info['price']) + ', ' + 
                    land_info['status'] + '\n')
            # Write the formatted line to the file
            file.write(line)
