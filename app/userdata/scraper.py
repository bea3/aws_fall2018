import pychrome
import os

if 'TARGET_URL' not in os.environ:
    TARGET_URL = "https://soundcloud.com"
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

# send to S3 bucket

tab.stop()
browser.close_tab(tab)
