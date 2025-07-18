from datetime import datetime

def create_invoice_report(
    land_info, 
    customer_name, 
    rental_duration, 
    transaction_type, 
    current_time, 
    fine=0
):
    # Create the invoice filename based on transaction type and kitta number
    invoice_filename = transaction_type + '_invoice_' + str(land_info['kitta_number']) + '.txt'
    
    # Define border and header for invoice
    border = "_" * 53
    header = "INVOICE REPORT".center(53)
    
    # Construct the invoice info 
    invoice_info = border + "\n"
    invoice_info += header + "\n"
    invoice_info += border + "\n"
    
    # Add land and rental details to the invoice
    invoice_info += "Kitta Number: " + str(land_info['kitta_number']) + "\n"
    invoice_info += "Location: " + land_info['location'] + "\n"
    invoice_info += "Direction: " + land_info['direction'] + "\n"
    invoice_info += "Area (in anna): " + str(land_info['area_anna']) + "\n"
    invoice_info += "Renter Name: " + customer_name + "\n"
    invoice_info += "Rental Type: " + transaction_type + "\n"
    invoice_info += "Date/Time: " + str(current_time) + "\n"
    invoice_info += "Rental Duration (months): " + str(rental_duration) + "\n"
    
    # Calculate total amount and total payment due
    total_amount = land_info['price'] * rental_duration
    total_amount_due = total_amount + fine
    
    # Apply 10% fine 
    if transaction_type == 'return':
        ten_percent_fine = 0.10 * total_amount
        total_amount_due += ten_percent_fine
        
        if fine > 0:
            invoice_info += "Initial Payment: " + str(fine) + " NPR\n"
        invoice_info += "10% Fine: " + str(ten_percent_fine) + " NPR\n"
    
    # Add total payment due 
    invoice_info += "Total Payment Due: " + str(total_amount_due) + " NPR\n"
    
    invoice_info += border
    
    # Print and save the invoice info
    print(invoice_info)
    try:
        with open(invoice_filename, 'w') as file:
            file.write(invoice_info)
    except IOError as e:
        print("Error writing invoice to file: " + str(e))
    
    return invoice_filename

def land_rental(
    land_records, 
    kitta_number, 
    customer_name, 
    rental_duration
):
    # Get the current date and time
    current_time = datetime.now()
    
    # Convert land records to a dictionary
    land_dict = {land['kitta_number']: land for land in land_records}
    
    # Check if the land is available
    if kitta_number in land_dict and land_dict[kitta_number]['status'] == 'Available':
        land_info = land_dict[kitta_number]
        land_info['status'] = 'Not Available'
        invoice_filename = create_invoice_report(
            land_info, 
            customer_name, 
            rental_duration, 
            'rent', 
            current_time
        )
        print("Land rented successfully. Invoice saved as " + invoice_filename + ".")
        return True
    
    print("Land not available for rent.")
    return False

def land_return(
    land_records, 
    kitta_number, 
    customer_name, 
    rental_duration, 
    return_date
):
    # Get the current date and time
    current_time = datetime.now()
    
    # Convert land records to a dictionary 
    land_dict = {land['kitta_number']: land for land in land_records}
    
    # Check if the land is currently rented
    if kitta_number in land_dict and land_dict[kitta_number]['status'] == 'Not Available':
        land_info = land_dict[kitta_number]
        
        # Calculate the end date of the rental period
        rent_end_date = return_date.replace(month=return_date.month - rental_duration)
        if rent_end_date.month <= 0:
            rent_end_date = rent_end_date.replace(year=rent_end_date.year - 1, month=rent_end_date.month + 12)
        
        # Calculate fine if the return date is after the rental period
        if return_date > rent_end_date:
            fine_duration = (return_date - rent_end_date).days // 30
            fine = fine_duration * land_info['price']
        else:
            fine = 0
        
        land_info['status'] = 'Available'
        invoice_name = create_invoice_report(
            land_info, 
            customer_name, 
            rental_duration, 
            'return', 
            current_time, 
            fine
        )
        print("Land returned successfully. Invoice saved as " + invoice_name + ".")
        return True
    
    print("Land is not currently rented.")
    return False
