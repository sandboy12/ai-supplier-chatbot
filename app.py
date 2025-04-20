
import streamlit as st
import pandas as pd

# Load Excel files
suppliers = pd.read_excel('suppliers.xlsx')
rfq_data = pd.read_excel('rfq_data.xlsx')
scorecards = pd.read_excel('scorecards.xlsx')
qual_reviews = pd.read_excel('qual_reviews.xlsx')

st.title("🛠️ Supplier Qualification AI Assistant")

query = st.text_input("Ask a question about a supplier or RFQ:")

if query:
    if "supplier" in query.lower() and "otif" in query.lower():
        st.write(scorecards[['supplier_id', 'on_time_delivery']])
    elif "disqualified" in query.lower():
        disq = scorecards[scorecards['approval_status'] != 'Approved']
        st.write(disq.merge(qual_reviews, on='supplier_id', how='left'))
    elif "summary" in query.lower():
        st.write("Summary of supplier reviews:")
        st.dataframe(qual_reviews)
    else:
        st.write("Try asking about OTIF, disqualified suppliers, or review summaries.")

st.write("---")
st.write("📄 Example Files Loaded:")
st.write("- suppliers.xlsx")
st.write("- rfq_data.xlsx")
st.write("- scorecards.xlsx")
st.write("- qual_reviews.xlsx")
