import code1

def run_application():
    print("Welcome to the FizzBuzz Application!")
    allow_negative = input("Allow negative numbers? (y/n): ").strip().lower() == "y"
    
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("VICTORY!")
            break
        try:
            number = int(user_input)
            result = code1.fizzbuzz(number, allow_negative)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    run_application()
