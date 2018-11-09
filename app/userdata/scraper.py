import pychrome
import os
import json
import boto3

if 'TARGET_URL' not in os.environ:
    TARGET_URL = "https://slickdeals.net"
else:
    TARGET_URL = os.environ["TARGET_URL"]

browser = pychrome.Browser(url="http://0.0.0.0:9222")
tab = browser.new_tab()

def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.set_listener("Network.requestWillBeSent", request_will_be_sent)

tab.start()
tab.call_method("Network.enable")
tab.call_method("Page.navigate", url=TARGET_URL, _timeout=5)

tab.wait(5)

tab.call_method("DOM.enable")
result = tab.call_method("DOM.getFlattenedDocument", depth=3, pierce=True)

url_str = TARGET_URL.replace('https://', '')
url_str = url_str.replace('http://', '')
filename = 'website-scrape-' + url_str + '.json'
f = open(filename, "w+")
f.write(json.dumps(result))
f.close()

tab.stop()
browser.close_tab(tab)

# sends to S3 bucket
s3 = boto3.resource('s3')
key_name = '-'.join(url_str.split(".")[:-1])
s3.Bucket('website-elements').upload_file(filename, key_name)
