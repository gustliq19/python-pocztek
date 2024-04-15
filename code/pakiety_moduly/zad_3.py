import calculations.loan

initial_value = float(input("Jaka jest kwota początkowa? "))
percentage = float(input("Jakie jest oprocentowanie? "))
loan_years = int(input("Jaki jest czas lokaty (w latach)? "))

loan_end_value = calculations.loan.calculate_loan_value(initial_value, percentage, loan_years)

print(f"Wartość lokaty po {loan_years} latach będzie równa: {loan_end_value:.2f} zł")
