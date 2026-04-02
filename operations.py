from datetime import datetime

def calculate_fine(return_date, rent_end_date, monthly_price):
    """Calculates fine if the return date exceeds the rental duration."""
    if return_date > rent_end_date:
        # Simple monthly fine logic based on your documentation
        days_late = (return_date - rent_end_date).days
        months_late = (days_late // 30) + 1
        return months_late * (monthly_price * 0.1) # 10% fine per month
    return 0

def rent_land(land_dict, kitta, customer_name, duration):
    if kitta in land_dict and land_dict[kitta]['status'] == 'Available':
        land_dict[kitta]['status'] = 'Not Available'
        return True, land_dict[kitta]
    return False, None
