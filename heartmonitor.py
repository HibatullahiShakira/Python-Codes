age = int(input("Enter your age: "))
CONSTANT_FIQURE = 220
PERCENTAGE = 100
beats_per_minutes = CONSTANT_FIQURE - age
LOW_TARGET_RANGE = 50 / PERCENTAGE
HIGH_TARGET_RANGE = 85 / PERCENTAGE
beats_per_minutes_low_end_of_target_range = beats_per_minutes * LOW_TARGET_RANGE
beats_per_minutes_high_end_of_target_range = beats_per_minutes * HIGH_TARGET_RANGE
print(f"The maximun heart rate on the low end is = {beats_per_minutes_low_end_of_target_range} \nThe maximum heart rate on the high end is = {beats_per_minutes_high_end_of_target_range}")

