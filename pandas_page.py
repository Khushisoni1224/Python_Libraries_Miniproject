import streamlit as st
import pandas as pd

def show_pandas():
    st.header("🐼 Pandas Data Analysis")

    operation = st.selectbox("Choose Operation", [
        "Create DataFrame",
        "Head & Tail",
        "Describe Data",
        "Filter Data",
        "Add Column",
        "Group By",
        "Upload Dataset"
    ])

    # ================= MANUAL INPUT =================
    if operation != "Upload Dataset":

        data = st.text_area(
            "Enter data",
            placeholder="Single column: 1,2,3\nTable:\n1,2\n3,4"
        )

        def parse_data(raw):
            if raw.strip() == "":
                return None
            try:
                if "\n" in raw:
                    rows = raw.strip().split("\n")
                    parsed = []
                    for r in rows:
                        parsed.append([float(x.strip()) for x in r.split(",")])
                    df = pd.DataFrame(parsed)
                    df.columns = [f"Col{i}" for i in range(len(df.columns))]
                    return df
                else:
                    values = [float(x.strip()) for x in raw.split(",")]
                    return pd.DataFrame({"Values": values})
            except:
                return None

        df = parse_data(data)

        if data.strip() != "" and df is None:
            st.error("Invalid data. Enter values like: 1,2,3 or rows like 1,2")

        if df is not None:
            st.subheader("Data Preview")
            st.write(df)

        # -------- CREATE --------
        if operation == "Create DataFrame":
            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                else:
                    st.success("DataFrame created.")

        # -------- HEAD / TAIL --------
        elif operation == "Head & Tail":
            n = st.number_input("Number of rows", min_value=1, value=5)

            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                else:
                    st.write("Head:")
                    st.write(df.head(n))
                    st.write("Tail:")
                    st.write(df.tail(n))

        # -------- DESCRIBE --------
        elif operation == "Describe Data":
            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                else:
                    st.write(df.describe())

        # -------- FILTER --------
        elif operation == "Filter Data":

            if df is not None:
                col = st.selectbox("Select column", df.columns)
                condition = st.selectbox("Condition", [">", "<", "=="])
                value = st.number_input("Enter value")

            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                    return

                if condition == ">":
                    result = df[df[col] > value]
                elif condition == "<":
                    result = df[df[col] < value]
                else:
                    result = df[df[col] == value]

                st.write(result)

        # -------- ADD COLUMN --------
        elif operation == "Add Column":

            if df is not None:
                col_name = st.text_input("New Column Name", "Sum")
                col1 = st.selectbox("Column 1", df.columns)
                col2 = st.selectbox("Column 2", df.columns)

            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                    return

                if col_name.strip() == "":
                    st.error("Enter column name.")
                    return

                df[col_name] = df[col1] + df[col2]
                st.write(df)

        # -------- GROUP BY --------
        elif operation == "Group By":

            if df is not None:
                group_col = st.selectbox("Group by column", df.columns)

            if st.button("Run"):
                if df is None:
                    st.error("Enter valid data.")
                    return

                result = df.groupby(group_col).sum(numeric_only=True)
                st.write(result)

        # -------- GET CODE --------
        if st.button("Get Code"):

            if df is None:
                st.error("Enter valid data first.")
                return

            base_data = df.values.tolist()

            if operation == "Create DataFrame":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})
print(df)
"""

            elif operation == "Head & Tail":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})

print(df.head({n}))
print(df.tail({n}))
"""

            elif operation == "Describe Data":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})

print(df.describe())
"""

            elif operation == "Filter Data":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})

filtered = df[df[{col!r}] {condition} {value}]
print(filtered)
"""

            elif operation == "Add Column":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})

df[{col_name!r}] = df[{col1!r}] + df[{col2!r}]
print(df)
"""

            elif operation == "Group By":
                code = f"""
import pandas as pd

df = pd.DataFrame({base_data})

print(df.groupby({group_col!r}).sum())
"""

            st.code(code, language="python")

            st.download_button(
                "⬇ Download Code",
                code,
                file_name="pandas_code.py"
            )

    # ================= FILE UPLOAD FEATURE =================
    else:
        st.subheader("📂 Upload Dataset")

        file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

        if file is None:
            return

        try:
            if file.name.endswith(".csv"):
                df = pd.read_csv(file)
                file_type = "csv"
            else:
                df = pd.read_excel(file)
                file_type = "excel"

            st.success("File loaded successfully")

            st.write("Preview:")
            st.write(df.head())

            n = st.number_input("Enter number of rows to display", min_value=1, value=5)

            if st.button("Show Top Data"):

                result = df.head(n)
                st.write(result)

                if file_type == "csv":
                    code = f"""
import pandas as pd

df = pd.read_csv("your_file.csv")
print(df.head({n}))
"""
                else:
                    code = f"""
import pandas as pd

df = pd.read_excel("your_file.xlsx")
print(df.head({n}))
"""

                st.code(code, language="python")

                st.download_button(
                    "⬇ Download Code",
                    code,
                    file_name="top_n_data.py"
                )

        except:
            st.error("Unable to read file. Please upload a valid CSV or Excel file.")