import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yml', 'r') as file:
    feed = yaml.load(file, Loader=yaml.FullLoader)
    yaml_data = yaml.safe_load(file)
    print(yaml_data)
    
    rss_element = xml_tree.Element('rss', {'version':'2.0', 
    'xmlns:atom':'http://www.w3.org/2005/Atom', 
    'xmlns:media':'http://search.yahoo.com/mrss/', 
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})
    
