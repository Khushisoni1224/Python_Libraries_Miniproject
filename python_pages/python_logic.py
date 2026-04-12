# -------- CONDITIONALS --------
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"

def largest_of_three(a, b, c):
    return max(a, b, c)

def grade_calc(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    else:
        return "Grade C"

def leap_year(year):
    return "Leap Year" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not Leap Year"


# -------- LOOPS --------
def print_n(n):
    return list(range(1, n+1))

def sum_n(n):
    return sum(range(1, n+1))

def multiplication_table(n):
    return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

def star_pattern(n):
    return ["*" * i for i in range(1, n+1)]

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


# -------- FUNCTIONS --------
def square(n):
    return n * n

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def calculator(n):
    return {
        "Double": n*2,
        "Square": n*n,
        "Half": n/2
    }


# -------- DATA STRUCTURES --------
def list_operations(lst):
    return {
        "Original": lst,
        "Sorted": sorted(lst),
        "Reversed": lst[::-1],
        "Unique": list(set(lst))
    }

def list_sum(lst):
    return sum(lst)

def remove_duplicates(lst):
    return list(set(lst))


# -------- FILE HANDLING --------
def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return "File written successfully"

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

def append_file(filename, content):
    with open(filename, "a") as f:
        f.write(content)
    return "Content appended"

def count_words(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
            return len(text.split())
    except:
        return "Error reading file"


# -------- ERROR HANDLING --------
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Invalid input"

def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
    except:
        return "Error"

def string_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid number"