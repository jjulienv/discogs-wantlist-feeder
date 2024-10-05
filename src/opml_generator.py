from io import BytesIO
from datetime import datetime
import xml.etree.ElementTree as ET

def generate_rss_feed_url(release_id):
    return f"https://www.discogs.com/sell/mplistrss?ev=rb&output=rss&release_id={release_id}"

def create_opml(selected_rows):
    opml = ET.Element('opml', version='1.0')
    head = ET.SubElement(opml, 'head')
    title = ET.SubElement(head, 'title')
    title.text = "Feeder - RSS Feed Reader"
    date_created = ET.SubElement(head, 'dateCreated')
    date_created.text = datetime.utcnow().isoformat() + 'Z'

    body = ET.SubElement(opml, 'body')

    for _, row in selected_rows.iterrows():
        outline = ET.SubElement(body, 'outline', {
            'text': f"{row['Artist']} - {row['Title']} For Sale at Discogs Marketplace",
            'title': f"{row['Artist']} - {row['Title']} For Sale at Discogs Marketplace",
            'type': 'rss',
            'xmlUrl': generate_rss_feed_url(row['release_id']),
            'htmlUrl': 'https://www.discogs.com/sell/',
            'rssfr-numPosts': '5',
            'rssfr-favicon': 'https://icons.feedercdn.com/www.discogs.com',
            'rssfr-useNotifications': '1',
            'rssfr-updateInterval': '600000'
        })

    return ET.tostring(opml, encoding='utf-8', xml_declaration=True).decode('utf-8')

def export_to_opml(selected_rows):
    opml_content = create_opml(selected_rows)
    return BytesIO(opml_content.encode('utf-8'))