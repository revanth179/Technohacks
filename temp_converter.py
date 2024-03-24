
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius: {:.2f}".format(celsius))
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()