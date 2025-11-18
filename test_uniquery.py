from utils.data_handle import load_data, answer_query

# Load data
df = load_data("data/colleges.xlsx")
print("✅ Data loaded successfully!")
print(df.head())

# Test a few queries
queries = [
    "fees of oriental university",
    "does oriental university have hostel",
    "which colleges have labs",
    "colleges with library",
    "colleges with gym"
]

for q in queries:
    print(f"\n🔹 Query: {q}")
    result = answer_query(df, q)
    print("Response:")
    print(result)



# from utils.data_handle import load_data, measure_response_time

# df = load_data("data/colleges.xlsx")

# # Example query
# query = "Does Acropolis have a hostel?"

# # Measure without cache
# time_no_cache = measure_response_time(df, query, cached=False)

# # Then, run your Streamlit app once with caching enabled and re-run this to get the cached time
# time_with_cache = measure_response_time(df, query, cached=True)

# improvement = (time_no_cache - time_with_cache) / time_no_cache * 100
# print(f"🚀 Performance improved by approximately {improvement:.2f}%")
