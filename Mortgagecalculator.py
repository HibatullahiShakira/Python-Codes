Principal = float(input("Enter principal amount: "))
Annual_interest_rate = float(input("Enter annual interest rate: "))
Duration = float(input("Enter duration: "))
percentage_to_decimal = Annual_interest_rate / 100 /12
Duration_to_month = Duration * 12
Calculate = (percentage_to_decimal * (1 + percentage_to_decimal) ** Duration_to_month) 
Calculatee = ((1 + percentage_to_decimal) ** Duration_to_month) - 1
Calculate1 = Principal * Calculate
Monthly_Payment = Calculate1 / Calculatee
print(f"The monthly payment for each month is = ${Monthly_Payment:,.2f}")


	


