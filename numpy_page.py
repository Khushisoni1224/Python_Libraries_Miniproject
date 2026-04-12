import streamlit as st
import numpy as np

def show_numpy():
    st.header("🔢 NumPy Learning Section")

    example = st.selectbox("Choose Example", [
        "Create Array",
        "Statistics (Mean, Std)",
        "Array Operations",
        "Reshape Array",
        "Matrix Operations"
    ])

    data = st.text_input("Enter numbers (comma separated)")

    if st.button("Run", key=f"np_run_{example}"):
        arr = np.array(list(map(int, data.split(","))))

        if example == "Create Array":
            st.write("Array:", arr)

        elif example == "Statistics (Mean, Std)":
            st.write("Mean:", np.mean(arr))
            st.write("Std Dev:", np.std(arr))

        elif example == "Array Operations":
            st.write("Squared:", arr**2)
            st.write("Added 10:", arr + 10)

        elif example == "Reshape Array":
            st.write("Reshaped:", arr.reshape(1, -1))

        elif example == "Matrix Operations":
            if len(arr) >= 4:
                mat = arr[:4].reshape(2,2)
                st.write("Matrix:", mat)
                st.write("Transpose:", mat.T)
            else:
                st.error("Enter at least 4 values")

    # -------- GET CODE --------
    if st.button("Get Code", key=f"np_code_{example}"):
        if example == "Create Array":
            st.code("""
import numpy as np
arr = np.array([1,2,3])
print(arr)
""")

        elif example == "Statistics (Mean, Std)":
            st.code("""
import numpy as np
arr = np.array([1,2,3])
print(np.mean(arr))
print(np.std(arr))
""")

        elif example == "Array Operations":
            st.code("""
arr = np.array([1,2,3])
print(arr**2)
print(arr + 10)
""")

        elif example == "Reshape Array":
            st.code("""
arr = np.array([1,2,3,4])
print(arr.reshape(1, -1))
""")

        elif example == "Matrix Operations":
            st.code("""
arr = np.array([1,2,3,4])
mat = arr.reshape(2,2)
print(mat.T)
""")