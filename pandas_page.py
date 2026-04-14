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
        "Group By"
    ])

    # -------- INPUT DATA --------
    data = st.text_area(
        "Enter data\nExamples:\nSingle column: 12,23,34\nTable:\n1,2,3\n4,5,6"
    )

    # -------- PARSE FUNCTION --------
    def parse_data(raw):
        try:
            if "\n" in raw:
                rows = raw.strip().split("\n")
                data = [list(map(float, r.split(","))) for r in rows]
                df = pd.DataFrame(data)
                df.columns = [f"Col{i}" for i in range(len(df.columns))]
                return df
            else:
                values = list(map(float, raw.split(",")))
                return pd.DataFrame({"Values": values})
        except:
            return None

    df = parse_data(data) if data else None

    # -------- VALIDATION --------
    if data and df is None:
        st.error("❌ Invalid data format!")

    # -------- PREVIEW --------
    if df is not None:
        st.subheader("📊 Data Preview")
        st.write(df)

    # ================= OPERATIONS =================

    # -------- CREATE --------
    if operation == "Create DataFrame":
        if st.button("Run"):
            st.success("DataFrame Created Successfully")

    # -------- HEAD / TAIL --------
    elif operation == "Head & Tail":
        n = st.number_input("Number of rows", min_value=1, value=5)

        if st.button("Run"):
            if df is not None:
                st.write("Head:")
                st.write(df.head(n))
                st.write("Tail:")
                st.write(df.tail(n))

    # -------- DESCRIBE --------
    elif operation == "Describe Data":
        if st.button("Run"):
            if df is not None:
                st.write(df.describe())

    # -------- FILTER --------
    elif operation == "Filter Data":

        if df is not None:
            col = st.selectbox("Select column", df.columns)
            condition = st.selectbox("Condition", [">", "<", "=="])
            value = st.number_input("Enter value")

        if st.button("Run"):
            if df is None:
                st.warning("Enter valid data")
                return

            if condition == ">":
                result = df[df[col] > value]
            elif condition == "<":
                result = df[df[col] < value]
            else:
                result = df[df[col] == value]

            st.write("Filtered Output:")
            st.write(result)

    # -------- ADD COLUMN --------
    elif operation == "Add Column":

        if df is not None:
            col_name = st.text_input("New Column Name", "Sum")
            col1 = st.selectbox("Column 1", df.columns)
            col2 = st.selectbox("Column 2", df.columns)

        if st.button("Run"):
            if df is None:
                st.warning("Enter valid data")
                return

            df[col_name] = df[col1] + df[col2]
            st.write(df)

    # -------- GROUP BY --------
    elif operation == "Group By":

        if df is not None:
            group_col = st.selectbox("Group by column", df.columns)

        if st.button("Run"):
            if df is None:
                st.warning("Enter valid data")
                return

            result = df.groupby(group_col).sum(numeric_only=True)
            st.write(result)

    # ================= GET CODE =================

    if st.button("Get Code"):

        if df is None:
            st.warning("Enter valid dataset first!")
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
df = pd.DataFrame({base_data})

print(df.head({n}))
print(df.tail({n}))
"""

        elif operation == "Describe Data":
            code = f"""
df = pd.DataFrame({base_data})

print(df.describe())
"""

        elif operation == "Filter Data":
            code = f"""
df = pd.DataFrame({base_data})

filtered = df[df["{col}"] {condition} {value}]
print(filtered)
"""

        elif operation == "Add Column":
            code = f"""
df = pd.DataFrame({base_data})

df["{col_name}"] = df["{col1}"] + df["{col2}"]
print(df)
"""

        elif operation == "Group By":
            code = f"""
df = pd.DataFrame({base_data})

print(df.groupby("{group_col}").sum())
"""

        st.code(code, language="python")

        st.download_button(
            "⬇ Download Code",
            code,
            file_name="pandas_code.py"
        )