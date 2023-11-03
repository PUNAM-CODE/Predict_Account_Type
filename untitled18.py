import pdfplumber

def extract_account_types(pdf_path):
    # Extract text from the PDF
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Preprocess the text (e.g., lowercasing)
    cleaned_text = text.lower()
    
    # Define rules for detecting account types
    account_types = []

    # Initialize variables to keep track of detected account types
    detected_checking = False
    detected_savings = False

    # Check for "Checking" in the cleaned text
    if not detected_checking and any(keyword in cleaned_text for keyword in ["checking"]):
        account_types.append("Checking")
        detected_checking = True

    # Check for "Savings" in the cleaned text
    if not detected_savings and any(keyword in cleaned_text for keyword in ["savings"]):
        account_types.append("Savings")
        detected_savings = True

    if not account_types:
        account_types.append("Unknown")

    return account_types

# Example usage
pdf_file_path = r"C:\Users\punam.chaudhari\Documents\Account_Type_Model\test_pdf\22056E3W4030572810_Import1.PDF"
account_types = extract_account_types(pdf_file_path)
print(f"Detected Account Types: {', '.join(account_types)}")
