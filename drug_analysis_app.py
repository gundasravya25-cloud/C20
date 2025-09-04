import streamlit as st

st.title("Drug Interaction and Dosage Analysis System")

st.markdown("""
This system analyzes drug interactions, recommends correct dosages based on age,  
and suggests safe alternative medications based on drug details.  
It leverages NLP to extract drug info from medical text.
""")

# Input: Patient Age
age = st.number_input("Patient Age (years)", min_value=0, max_value=120, value=30)

# Input: Drugs list (multiple drugs)
st.markdown("### Enter Drugs to Analyze")
drug_inputs = []
num_drugs = st.number_input("Number of drugs to enter", min_value=1, max_value=10, value=3)
for i in range(num_drugs):
    drug_name = st.text_input(f"Drug {i+1} Name")
    drug_inputs.append(drug_name.strip())

# Input: Unstructured medical text
medical_text = st.text_area("Paste unstructured medical text for NLP extraction", height=150)

# Button to submit
if st.button("Analyze"):
    # Validate drug names
    drugs = [d for d in drug_inputs if d]
    if not drugs:
        st.warning("Please enter at least one drug name.")
    else:
        st.success("Analysis Started... (This is a placeholder for backend integration)")

        # 1) Drug Interaction Detection (mock output)
        st.subheader("1) Drug Interaction Detection")
        st.write(f"Checking interactions between drugs: {', '.join(drugs)}")
        st.info("No harmful interactions detected. (Mock result)")

        # 2) Age-Specific Dosage Recommendation (mock output)
        st.subheader("2) Age-Specific Dosage Recommendation")
        st.write(f"Recommended dosages for age {age}:")
        for drug in drugs:
            st.write(f"- {drug}: Dosage recommendation here (mock)")

        # 3) Alternative Medication Suggestions (mock output)
        st.subheader("3) Alternative Medication Suggestions")
        st.write("No alternative medications needed. (Mock result)")

        # 4) NLP-Based Drug Information Extraction (mock output)
        st.subheader("4) NLP-Based Drug Information Extraction")
        if medical_text.strip():
            st.write("Extracted drug details:")
            st.write("- Drug A: 50mg, twice daily (mock)")
            st.write("- Drug B: 10mg, once daily (mock)")
        else:
            st.write("No medical text provided.")
            

