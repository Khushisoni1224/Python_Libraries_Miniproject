import streamlit as st
import matplotlib.pyplot as plt

def show_matplotlib():
    st.header("📊 Matplotlib Visualization")

    chart = st.selectbox("Choose Chart", [
        "Line Chart",
        "Bar Chart",
        "Pie Chart",
        "Histogram",
        "Multiple Lines"
    ])

    x = st.text_input("Enter X values (comma separated)")
    y = st.text_input("Enter Y values (comma separated)")

    if st.button("Plot Graph", key=f"plot_{chart}"):
        x_vals = list(map(int, x.split(",")))
        y_vals = list(map(int, y.split(",")))

        plt.figure()

        if chart == "Line Chart":
            plt.plot(x_vals, y_vals)

        elif chart == "Bar Chart":
            plt.bar(x_vals, y_vals)

        elif chart == "Pie Chart":
            plt.pie(y_vals, labels=x_vals, autopct='%1.1f%%')

        elif chart == "Histogram":
            plt.hist(y_vals)

        elif chart == "Multiple Lines":
            plt.plot(x_vals, y_vals)
            plt.plot(x_vals, [i*2 for i in y_vals])

        plt.title(chart)
        st.pyplot(plt)

    # -------- GET CODE --------
    if st.button("Get Code", key=f"code_{chart}"):
        if chart == "Line Chart":
            st.code("""
import matplotlib.pyplot as plt
x = [1,2,3]
y = [4,5,6]
plt.plot(x, y)
plt.show()
""")

        elif chart == "Bar Chart":
            st.code("""
plt.bar([1,2,3], [4,5,6])
plt.show()
""")

        elif chart == "Pie Chart":
            st.code("""
plt.pie([30,40,30], labels=["A","B","C"], autopct='%1.1f%%')
plt.show()
""")

        elif chart == "Histogram":
            st.code("""
plt.hist([1,2,2,3,3,3])
plt.show()
""")

        elif chart == "Multiple Lines":
            st.code("""
x = [1,2,3]
y = [2,4,6]
plt.plot(x, y)
plt.plot(x, [i*2 for i in y])
plt.show()
""")