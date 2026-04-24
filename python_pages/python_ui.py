import streamlit as st
from python_pages.python_logic import *

def show_python():
    st.header("🐍 Python Learning Section")

    concept = st.selectbox(
        "Select Concept",
        ["Conditionals", "Loops", "Functions", "Data Structures", "File Handling", "Error Handling"]
    )

    # -------- CONDITIONALS --------
    if concept == "Conditionals":
        example = st.selectbox("Choose Example", [
            "Even or Odd", "Positive / Negative", "Largest of 3", "Grade Calculator", "Leap Year"
        ])

        if example == "Even or Odd":
            num = st.number_input("Enter number", key="eo_num")
            if st.button("Run", key="run_even"):
                st.success(even_odd(num))
            if st.button("Show Code", key="code_even"):
                st.code("if num % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')")

        elif example == "Positive / Negative":
            num = st.number_input("Enter number", key="pn_num")
            if st.button("Run", key="run_pn"):
                st.success(positive_negative(num))
            if st.button("Show Code", key="code_pn"):
                st.code("if num > 0:\n    print('Positive')\nelif num < 0:\n    print('Negative')\nelse:\n    print('Zero')")

        elif example == "Largest of 3":
            a = st.number_input("A", key="l3_a")
            b = st.number_input("B", key="l3_b")
            c = st.number_input("C", key="l3_c")
            if st.button("Run", key="run_l3"):
                st.success(largest_of_three(a, b, c))
            if st.button("Show Code", key="code_l3"):
                st.code("print(max(a, b, c))")

        elif example == "Grade Calculator":
            m = st.number_input("Marks", key="marks")
            if st.button("Run", key="run_gc"):
                st.success(grade_calc(m))
            if st.button("Show Code", key="code_gc"):
                st.code("if marks >= 90:\n    print('A')\nelif marks >= 75:\n    print('B')\nelse:\n    print('C')")

        elif example == "Leap Year":
            y = st.number_input("Year", key="year")
            if st.button("Run", key="run_ly"):
                st.success(leap_year(y))
            if st.button("Show Code", key="code_ly"):
                st.code("if (y%4==0 and y%100!=0) or y%400==0:\n    print('Leap Year')")

    # -------- LOOPS --------
    elif concept == "Loops":
        example = st.selectbox("Choose Example", [
            "Print 1 to N", "Sum of N", "Multiplication Table", "Star Pattern", "Prime Check"
        ])

        n = st.number_input("Enter number", min_value=1, key="loop_n")

        if st.button("Run", key=f"run_loop_{example}"):
            if example == "Print 1 to N":
                st.write(print_n(n))
            elif example == "Sum of N":
                st.success(sum_n(n))
            elif example == "Multiplication Table":
                for line in multiplication_table(n):
                    st.write(line)
            elif example == "Star Pattern":
                for line in star_pattern(n):
                    st.write(line)
            elif example == "Prime Check":
                st.success(is_prime(n))

        if st.button("Show Code", key=f"code_loop_{example}"):
            st.code("for i in range(1, n+1):\n    print(i)")

    # -------- FUNCTIONS --------
    elif concept == "Functions":
        example = st.selectbox("Choose Example", [
            "Square", "Factorial", "Fibonacci", "Calculator"
        ])

        n = st.number_input("Enter number", min_value=1, key="func_n")

        if st.button("Run", key=f"run_func_{example}"):
            if example == "Square":
                st.success(square(n))
            elif example == "Factorial":
                st.success(factorial(n))
            elif example == "Fibonacci":
                st.write(fibonacci(n))
            elif example == "Calculator":
                result = calculator(n)
                for k, v in result.items():
                    st.write(f"{k}: {v}")

        if st.button("Show Code", key=f"code_func_{example}"):
            st.code("def function(n):\n    return n*n")

    # -------- DATA STRUCTURES --------
    elif concept == "Data Structures":
        data = st.text_input("Enter numbers (comma separated)", key="ds_data")

        if st.button("Run", key="run_ds"):
            if data.strip() == "":
                st.error("Enter values.")
                return
            try:
                lst = [int(x.strip()) for x in data.split(",")]
            except:
                st.error("Invalid input. Enter numbers like: 1, 2, 3")
                return

            st.write(list_operations(lst))
            st.write("Sum:", list_sum(lst))
            st.write("Unique:", remove_duplicates(lst))

        if st.button("Show Code", key="code_ds"):
            st.code("lst = list(map(int, input().split(',')))\nprint(sorted(lst))")

    # -------- FILE HANDLING --------
    elif concept == "File Handling":
        option = st.selectbox("Choose Operation", [
            "Write File", "Read File", "Append File", "Count Words"
        ])

        filename = st.text_input("Enter file name")

        if option in ["Write File", "Append File"]:
            content = st.text_area("Enter content")

        if st.button("Run File Operation"):
            if filename.strip() == "":
                st.error("Enter file name.")
                return

            if option in ["Write File", "Append File"] and content.strip() == "":
                st.error("Enter content.")
                return

            if option == "Write File":
                st.success(write_file(filename, content))
            elif option == "Read File":
                st.write(read_file(filename))
            elif option == "Append File":
                st.success(append_file(filename, content))
            elif option == "Count Words":
                st.success(count_words(filename))

        if st.button("Show Code"):
            st.code("with open('file.txt','r') as f:\n    print(f.read())")

    # -------- ERROR HANDLING --------
    elif concept == "Error Handling":
        example = st.selectbox("Choose Example", [
            "Safe Division", "List Access", "String to Integer"
        ])

        if example == "Safe Division":
            a = st.number_input("Numerator")
            b = st.number_input("Denominator")

            if st.button("Divide"):
                st.success(safe_division(a, b))

        elif example == "List Access":
            data = st.text_input("Enter list")
            index = st.number_input("Index", min_value=0)

            if st.button("Access"):
                if data.strip() == "":
                    st.error("Enter list values.")
                    return
                try:
                    lst = [int(x.strip()) for x in data.split(",")]
                except:
                    st.error("Invalid list. Enter numbers like: 1, 2, 3")
                    return

                st.success(safe_list_access(lst, index))

        elif example == "String to Integer":
            value = st.text_input("Enter value")

            if st.button("Convert"):
                st.success(string_to_int(value))

        if st.button("Show Code"):
            st.code("try:\n    result = a/b\nexcept ZeroDivisionError:\n    print('Error')")