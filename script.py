import json
from haralyzer import HarParser, HarPage

# Download the .har file from Developer tools(roughly the same as your operations), and we can parse it offline.
# Even if we have many image files to be download, it will not take too much time to wait to paste.
with open('nicepage.com.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data["entries"]
image_urls = []

for entry in data:
    if entry["response"]["content"]["mimeType"].find("image/") == 0:
        image_urls.append(entry["request"]["url"])
     
# Save the URL list to a text file directly.
with open('target_link.txt', 'w') as f:
    for link in image_urls:
        f.write("%s\n" % link)