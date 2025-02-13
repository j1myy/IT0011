
user_date_input = input("Enter the date like this (mm/dd/yyyy): ")


parts = user_date_input.split("/")
month_num = int(parts[0])
day = int(parts[1])
year = parts[2]


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


month_name_converter = months[month_num - 1]

print("Date:", month_name_converter, day, ",", year)
