import streamlit as st
from src.csv_loader import load_csv
from src.opml_generator import export_to_opml
from datetime import datetime
import pandas as pd

def main():
    st.title("Discogs Wantlist RSS Feed Generator")

    
    st.subheader("Upload your Discogs wantlist CSV")

    uploaded_file = st.file_uploader("",type="csv")

    if uploaded_file:
        df = load_csv(uploaded_file)

        today = datetime.today().date()

        st.subheader("Filter the releases you want to track")
        
        # Create two columns for date inputs
        col1, col2 = st.columns(2)

        with col1:
            start_date = st.date_input("Wantlist start date", value=today)

        with col2:
            end_date = st.date_input("Wantlist end date", value=today)

        # Add a text input for filtering by the Notes column
        notes_filter = st.text_input("Filter by keyword in your Wantlist notes:", "")

        if start_date and end_date:
            # Filter by date range
            df_filtered = df[(df['date_added'] >= pd.Timestamp(start_date)) & (df['date_added'] <= pd.Timestamp(end_date))]
        else:
            df_filtered = df

        # Further filter by the Notes column if a filter word is provided
        if notes_filter:
            df_filtered = df_filtered[df_filtered['Notes'].str.contains(notes_filter, na=False, case=False)]

        st.subheader("Select Entries for OPML")

        # Create a list to hold the selections
        selected_rows = []

        # Create a grid layout with 3 columns
        cols = st.columns(3)

        # Iterate over the filtered DataFrame and display checkboxes in the columns
        for index, row in df_filtered.iterrows():
            # Determine which column to place the checkbox in
            col_index = index % 3  # Cycle through columns
            
            # Display as "Artist - Title [Catalog]"
            checkbox_label = f"{row['Artist']} - {row['Title']} [{row['Catalog#']}]"
            with cols[col_index]:
                checkbox = st.checkbox(checkbox_label, value=True, key=index)
                if checkbox:
                    selected_rows.append(row)

        # Use a session state flag to control download button visibility
        st.session_state.selected_rows = selected_rows

        # Display the download button only if there are selected rows
        if st.button("Download OPML"):
            if selected_rows:
                # Create a DataFrame from the selected rows
                selected_df = pd.DataFrame(selected_rows)
                opml_file = export_to_opml(selected_df)

                # Show the download button
                st.download_button(
                    label="Download OPML",
                    data=opml_file,
                    file_name='wantlist.opml',
                    mime='application/xml'
                )
            else:
                st.error("No entries selected for export.")

if __name__ == "__main__":
    main()