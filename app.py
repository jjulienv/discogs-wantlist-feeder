import streamlit as st
from src.csv_loader import load_csv
from src.opml_generator import export_to_opml
from datetime import datetime
import pandas as pd

def main():
    st.title("Discogs Wantlist RSS Feed Generator")

    uploaded_file = st.file_uploader("Upload your Discogs wantlist CSV", type="csv")

    if uploaded_file:
        df = load_csv(uploaded_file)

        today = datetime.today().date()

        st.subheader("Filter by Date Range")
        start_date = st.date_input("Start Date", value=today)
        end_date = st.date_input("End Date", value=today)

        if start_date and end_date:
            df_filtered = df[(df['date_added'] >= pd.Timestamp(start_date)) & (df['date_added'] <= pd.Timestamp(end_date))]
        else:
            df_filtered = df

        st.subheader("Select Entries for OPML")

        # Create a list to hold the selections
        selected_rows = []

        for index, row in df_filtered.iterrows():
            # Display as "Artist - Title [Catalog]"
            checkbox_label = f"{row['Artist']} - {row['Title']} [{row['Catalog#']}]"
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