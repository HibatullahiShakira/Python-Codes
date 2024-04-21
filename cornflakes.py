price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount percentage: "))
discount_value = (discount_percentage / 100) * price
final_price = price - discount_value
print(final_price)