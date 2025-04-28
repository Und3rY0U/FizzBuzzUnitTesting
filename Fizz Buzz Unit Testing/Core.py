def FizzBuzz(number, allow_negative=False):
    if not allow_negative and number < 0:
        return "Negative numbers are not allowed."
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print(FizzBuzz(user_input))
