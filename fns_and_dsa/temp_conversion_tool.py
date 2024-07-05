FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def check_input_type(input_value):
    try:
        int_value = int(input_value)
    # if isinstance(int_value, int) == True:
        temp_type = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
        if temp_type == "c":
            new_temp = convert_to_fahrenheit(int_value)
            print(f"{int_value}°C is {new_temp}°F")
        elif temp_type == "f":
            new_temp = convert_to_celsius(int_value)
            print(f"{int_value}°F is {new_temp}°C")
        else:
            print("Wrong input.")
    except ValueError:
        # If conversion fails, it means the input is a string
        print("Invalid temperature. Please enter a numeric value.")
        


temp = input("Enter the temperature to convert: ")
check_input_type(temp)
# print (isinstance(temp, str))
# if isinstance(temp, str) == True:
#     print ("Invalid temperature. Please enter a numeric value.")
# else:
#     temp_type = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
#     if temp_type == "c":
#         new_temp = convert_to_fahrenheit(temp)
#         print(f"{temp}°C is {new_temp}°F")
#     elif temp_type == "f":
#         new_temp = convert_to_celsius(temp)
#         print(f"{temp}°F is {new_temp}°C")
#     else:
#         print("Wrong input.")