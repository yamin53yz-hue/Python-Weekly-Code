from temp import temp_c_to_f , temp_f_to_c
print("--Temperature Converter--")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

temp_choice = input("choose 1 or 2: ")
temperature = float(input("Enter temperature: "))

if temp_choice == "1":
    result = temp_c_to_f(temperature)
    print(temperature, "℃=" , result, "℉") 
elif temp_choice == "2":
    result = temp_f_to_c(temperature)
    print(temperature, "℉=" , result, "℃")
else:
    print("Invalid options. Choose 1 or 2")