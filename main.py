import datetime

def generate_rent_invoice(customer_name, land_info, duration):
    filename = f"Rent_{customer_name}_{land_info['kitta_number']}.txt"
    total_cost = land_info['price'] * duration
    
    content = f"""
    --- TechnoPropertyNepal Rent Invoice ---
    Date: {datetime.datetime.now()}
    Customer: {customer_name}
    Kitta Number: {land_info['kitta_number']}
    Location: {land_info['location']}
    Duration: {duration} months
    Total Cost: Rs. {total_cost}
    ---------------------------------------
    """
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def update_master_file(filename, land_list):
    with open(filename, 'w') as f:
        for land in land_list:
            line = f"{land['kitta_number']}, {land['location']}, {land['direction']}, {land['anna']}, {land['price']}\n"
            f.write(line)
