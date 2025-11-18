import pandas as pd

# import time

# -------------------------------
# Load and normalize data
# -------------------------------
def load_data(filename):
    df = pd.read_excel("data/colleges.xlsx")

    # Convert relevant columns to string to avoid .str errors
    df["college_name"] = df["college_name"].astype(str)
    df["facilities"] = df["facilities"].astype(str)
    df["type"] = df["type"].astype(str)
    df["domain"] = df["domain"].astype(str)

    # Normalize columns
    df["college_name_normalized"] = df["college_name"].str.lower().str.strip()
    df["facilities_normalized"] = df["facilities"].str.lower().str.replace(" ", "", regex=False)
    df["type_normalized"] = df["type"].str.lower().str.strip()
    df["domain_normalized"] = df["domain"].str.lower().str.strip()

    return df

# -------------------------------
# Answer queries
# -------------------------------
def answer_query(df, query):
    query = query.lower().strip()
    facilities_list = ["hostel", "library", "wifi", "lab", "auditorium", "cafeteria", "sports", "gym"]

    # 1️⃣ Fees query
    if "fee" in query or "fees" in query:
        for college in df["college_name_normalized"]:
            if college in query:
                row = df[df["college_name_normalized"] == college]
                if not row.empty:
                    fee = row.iloc[0]["fees"]
                    
                    # Convert fee to integer safely
                    try:
                        fee = int(str(fee).replace(",", "").strip())
                    except ValueError:
                        return f"Invalid fee value for {row.iloc[0]['college_name']}"

                    return f"The fees of {row.iloc[0]['college_name']} is ₹{fee:,}"
        return "Sorry, I couldn’t find that college in the dataset."


    # 2️⃣ College-specific facility query (Yes/No)
    if ("has" in query or "have" in query) and not ("which colleges" in query or "colleges with" in query):
        found_facility = None
        for fac in facilities_list:
            if fac in query:
                found_facility = fac
                break

        for college in df["college_name_normalized"]:
            if college in query:
                row = df[df["college_name_normalized"] == college]
                if not row.empty:
                    facilities = row.iloc[0]["facilities_normalized"]
                    if found_facility and found_facility in facilities:
                        return f"✅ Yes, {row.iloc[0]['college_name']} has {found_facility.title()} facility."
                    else:
                        return f"❌ No, {row.iloc[0]['college_name']} does not have {found_facility.title()} facility."
        return "Sorry, I couldn’t identify the college or facility."

    # 3️⃣ College type query (Government / Private)
    if "government" in query or "private" in query:
        if "government" in query:
            result = df[df["type_normalized"] == "government"]
        else:
            result = df[df["type_normalized"] == "private"]

        if not result.empty:
            return result[["college_name", "branch", "fees", "facilities", "type"]]
        else:
            return f"No {('government' if 'government' in query else 'private')} colleges found."

    # 4️⃣ General facility query (list all colleges with X)
    for fac in facilities_list:
        if fac in query:
            result = df[df["facilities_normalized"].str.contains(fac, na=False, regex=False)]
            if not result.empty:
                return result[["college_name", "branch", "fees", "facilities"]]
            else:
                return f"No colleges with {fac.title()} facility found."

    # 5️⃣ If none matched
    return "Sorry, I couldn’t understand your query."
# -------------------------------
# Performance Testing Helper
# -------------------------------
# def measure_response_time(df, query, cached=False):
#     """
#     Measures how long it takes to process a query.
#     Use this to compare cached vs non-cached performance.
#     """
#     start = time.time()
#     _ = answer_query(df, query)
#     end = time.time()
#     duration = end - start
#     mode = "with cache" if cached else "without cache"
#     print(f"⏱️ Query executed {mode} in {duration:.4f} seconds")
#     return duration