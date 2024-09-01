# Solution 1
def add_numbers(num1, num2):
    
    #This function takes two numbers and returns their sum.
    
    return num1 + num2

result = add_numbers(2, 4)
print(result)

# Solution 2
def is_even(num):
    
    #This function returns True if the number is even, and False otherwise.
    
    return num % 2 == 0

print(is_even(4))  # Move the print statement outside of the function

# Solution 3
def reverse_string(text):
    
   # This function returns the reversed version of the input string.
    
    return text[::-1]  # Fixed the return statement

print(reverse_string("abdul"))

# Solution 4
def count_vowels(text):
    
    #This function returns the count of vowels (a, e, i, o, u) in the string.
    
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Added example usage

# Solution 5
def calculate_factorial(n):
    
   # This function calculates the factorial of a non-negative integer n.
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Fixed the multiplication
    return factorial

print(calculate_factorial(4))  # Added example usage

# Solution 6
def apply_decorator(func):
    
    #This function applies a decorator to the given function.
    
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

# Example usage of the decorator
@apply_decorator
def sample_function():
    return "Function executed"

print(sample_function())  # Should print "Decorator Applied" and "Function executed"

 # solution 7
def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])

# Example usage:
people = [("Abdu", 20), ("Ali", 25), ("Charl", 35), ("Dim", 27)]
sorted_people = sort_by_age(people)

print(sorted_people)


# Solution 8
def merge_dicts(dict1, dict2):
    
    #Merge two dictionaries. If a key exists in both, sum their values. Otherwise, add the key-value pairs.
    
    merged_dict = {}  # Initialize an empty dictionary to store the merged result

    # Add all key-value pairs from dict1
    for key in dict1:
        if key in dict2:
            # If key exists in both dictionaries, sum their values
            merged_dict[key] = dict1[key] + dict2[key]
        else:
            # If key is only in dict1, add it to the merged dictionary
            merged_dict[key] = dict1[key]

    # Add key-value pairs from dict2 that are not in dict1
    for key in dict2:
        if key not in merged_dict:
            # If key is only in dict2, add it to the merged dictionary
            merged_dict[key] = dict2[key]

    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # Added example usage

# Solution 9
class Car:
    
   # Class representing a car with make, model, and year attributes.
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_information(self):
        """
        Print out the car's information.
        """
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Example usage of the Car class
my_car = Car("Toyota", "Corolla", 2021)
my_car.display_information()
