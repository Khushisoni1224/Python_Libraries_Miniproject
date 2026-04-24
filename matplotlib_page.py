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

    title = st.text_input("Enter Graph Title", value=chart)
    xlabel = st.text_input("Enter X-axis Label")
    ylabel = st.text_input("Enter Y-axis Label")

    x = None
    y = None

    if chart != "Histogram":
        x = st.text_input("Enter X values (comma separated)", placeholder="e.g. 1, 2, 3")

    y = st.text_input("Enter Y values (comma separated)", placeholder="e.g. 10, 20, 30")

    def parse_input(data):
        if data is None or data.strip() == "":
            return None
        try:
            return [float(i.strip()) for i in data.split(",")]
        except:
            return None

    x_vals = parse_input(x)
    y_vals = parse_input(y)

    def validate():
        if y_vals is None:
            st.error("Enter valid Y values.")
            return False

        if chart != "Histogram":
            if x_vals is None:
                st.error("Enter valid X values.")
                return False
            if len(x_vals) != len(y_vals):
                st.error("X and Y must have same number of values.")
                return False

        if chart == "Pie Chart" and x_vals is None:
            st.error("Enter labels for pie chart.")
            return False

        return True

    if st.button("Plot Graph", key=f"plot_{chart}"):

        if not validate():
            return

        plt.figure()

        if chart == "Line Chart":
            plt.plot(x_vals, y_vals, marker='o')

        elif chart == "Bar Chart":
            plt.bar(x_vals, y_vals)

        elif chart == "Pie Chart":
            plt.pie(y_vals, labels=x_vals, autopct='%1.1f%%')

        elif chart == "Histogram":
            plt.hist(y_vals, bins=5)

        elif chart == "Multiple Lines":
            plt.plot(x_vals, y_vals, label="Line 1")
            plt.plot(x_vals, [i * 2 for i in y_vals], label="Line 2")
            plt.legend()

        plt.title(title)

        if chart != "Pie Chart":
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)

        plt.grid(True)
        st.pyplot(plt)

    if st.button("Get Code", key=f"code_{chart}"):

        if not validate():
            return

        code = ""

        if chart == "Line Chart":
            code = f"""
import matplotlib.pyplot as plt

x = {x_vals}
y = {y_vals}

plt.plot(x, y, marker='o')
plt.title("{title}")
plt.xlabel("{xlabel}")
plt.ylabel("{ylabel}")
plt.grid(True)
plt.show()
"""

        elif chart == "Bar Chart":
            code = f"""
import matplotlib.pyplot as plt

x = {x_vals}
y = {y_vals}

plt.bar(x, y)
plt.title("{title}")
plt.xlabel("{xlabel}")
plt.ylabel("{ylabel}")
plt.grid(True)
plt.show()
"""

        elif chart == "Pie Chart":
            code = f"""
import matplotlib.pyplot as plt

labels = {x_vals}
sizes = {y_vals}

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("{title}")
plt.show()
"""

        elif chart == "Histogram":
            code = f"""
import matplotlib.pyplot as plt

data = {y_vals}

plt.hist(data, bins=5)
plt.title("{title}")
plt.xlabel("{xlabel}")
plt.ylabel("{ylabel}")
plt.grid(True)
plt.show()
"""

        elif chart == "Multiple Lines":
            code = f"""
import matplotlib.pyplot as plt

x = {x_vals}
y = {y_vals}

plt.plot(x, y, label="Line 1")
plt.plot(x, [i*2 for i in y], label="Line 2")

plt.title("{title}")
plt.xlabel("{xlabel}")
plt.ylabel("{ylabel}")
plt.legend()
plt.grid(True)
plt.show()
"""

        st.code(code, language="python")

        st.download_button(
            "⬇ Download Code",
            code,
            file_name="matplotlib_plot.py"
        )