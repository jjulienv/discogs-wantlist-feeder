# discogs-wantlist-feeder
A Streamlit app to generate custom RSS feeds from a discogs.com wantlist and add them to feeder.co

## Features
- Upload your Discogs wantlist CSV.
- Filter your list based on the date releases were added to the wantlist.
- Preview the filtered data.
- Confirm releases and generate an OPML file with RSS feed links.
- The OPML file can then be added to feeder.co, and you will receive alerts whenever an item is posted for sale on Discogs. 
  
## How to Use

	1. Download your Discogs wantlist on https://www.discogs.com/mywantlist 2. Uncompres the .zip file to get your wantlist CSV file.
    3.  Go to https://discogs-wantlist-feeder.streamlit.app/ and upload your CSV file.
	4.	Filter releases by the date added them, and the notes you added to your wanted releases.
	5.	Confirm the entries you wish to monitor via RSS.
	5.	Download the generated OPML file.
    6.  You can now go to https://feeder.co/library/import-export and import the generated file. All the releases you would like to monitor will be added.

## Installation
If you wish to run the app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/discogs-wantlist-rss-generator.git

2.	Install the required Python packages:

    ```bash
    git clone https://github.com/your-username/discogs-wantlist-rss-generator.git

3. Run the streamlit app:

    ```bash
    git clone https://github.com/your-username/discogs-wantlist-rss-generator.git

## License

This project is licensed under the MIT License.
