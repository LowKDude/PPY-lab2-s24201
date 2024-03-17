# Task 8: Prepare and Write Data to 'output.txt'

# Simulate input for demonstration purposes
input_numbers = "1 2 3 4 5 6 7 8 9 10 11 12"

# Convert Input
numbers_list = list(map(int, input_numbers.split()))
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)
numbers_dict = {num: num ** 2 for num in numbers_list}

# Example operations simplified for correction
if 8 in numbers_list:
    numbers_list.remove(8)

try:
    numbers_tuple += (10,)  # Tuples are immutable, corrected operation to 'add' instead of 'append'
except AttributeError as e:
    print(f"Error: {e}")

# Set operations simplified for demonstration
numbers_set.add(13)  # Example operation: Add a new element to the set

# Dictionary operation: corrected deletion to check if key exists
if 8 in numbers_dict:
    del numbers_dict[8]

# Write Output to File, simplified to focus on corrections
with open("output.txt", "w") as file:
    file.writelines([
        f"List: {numbers_list}\n",
        f"Tuple: {numbers_tuple}\n",
        f"Set: {numbers_set}\n",
        f"Dictionary: {numbers_dict}\n"
    ])

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Task 9: Process 'output.txt' and generate prime numbers

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Reading and finding the largest integer from 'output.txt'
try:
    with open("output.txt", "r") as file:
        # Filter each line in the file to extract numbers correctly
        numbers = []
        for line in file:
            for num in line.split():
                # Remove all characters that are not digits or a minus sign at the start
                cleaned_num = ''.join(filter(lambda x: x.isdigit(), num))
                if cleaned_num.isdigit():  # Check again after cleaning
                    numbers.append(int(cleaned_num))
    largest_integer = max(numbers) if numbers else None
except FileNotFoundError:
    print("Error: 'output.txt' file not found.")
    largest_integer = None

if largest_integer is not None:
    # Generate list of prime numbers up to the largest integer
    prime_numbers = [num for num in range(2, largest_integer + 1) if is_prime(num)]

    # Writing results to 'prime_numbers.txt'
    with open("prime_numbers.txt", "w") as file:
        file.write("List of Prime Numbers: " + ', '.join(map(str, prime_numbers)) + "\n")
        file.write("Sum of Prime Numbers: " + str(sum(prime_numbers)) + "\n")
        file.write("Largest Prime Number: " + str(max(prime_numbers) if prime_numbers else "None") + "\n")
        file.write("Smallest Prime Number: " + str(min(prime_numbers) if prime_numbers else "None") + "\n")
        file.write("Is Largest Integer Prime: " + str(is_prime(largest_integer)) + "\n")

    # Console output for verification
    print(f"Largest Integer Found: {largest_integer}")
    print(f"List of Prime Numbers: {prime_numbers}")
    print(f"Sum of Prime Numbers: {sum(prime_numbers)}")
    print(f"Largest Prime Number: {max(prime_numbers) if prime_numbers else 'None'}")
    print(f"Smallest Prime Number: {min(prime_numbers) if prime_numbers else 'None'}")
    print(f"Is Largest Integer Prime: {is_prime(largest_integer)}")
else:
    print("No largest integer found in 'output.txt'.")
