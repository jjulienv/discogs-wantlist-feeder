import pandas as pd
import io

# Function to modify the CSV content and load it
def load_csv(uploaded_file):
    # Read the uploaded file into memory
    content = uploaded_file.getvalue().decode('utf-8')

    # Split the content into lines
    lines = content.splitlines()

    # Check if 'date_added' is already in the header
    if 'date_added' not in lines[0]:
        # Modify the first line by appending ',date_added'
        lines[0] = lines[0].strip() + ',date_added'

    # Combine the modified lines back into a single string
    modified_content = "\n".join(lines)

    # Load the modified content into a DataFrame
    df = pd.read_csv(io.StringIO(modified_content), delimiter=',')

    # Convert 'date_added' column to datetime
    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

    return df