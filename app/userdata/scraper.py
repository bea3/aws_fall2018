import pychrome
import os
import json

if 'TARGET_URL' not in os.environ or os.environ["TARGET_URL"] == "THISISTHETARGETURL":
    TARGET_URL = "https://slickdeals.net"
else:
    TARGET_URL = os.environ["TARGET_URL"]

print(TARGET_URL)

browser = pychrome.Browser(url="http://127.0.0.1:9222")
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

filename = 'website' + '.json'
f = open(filename, "w")
f.write(json.dumps(result))
f.close()

tab.stop()
browser.close_tab(tab)
