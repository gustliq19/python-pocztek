def calculate_loan_value(init_value, percentage, years):
    return init_value * pow((1 + percentage / 100), years)

