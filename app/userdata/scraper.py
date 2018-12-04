import pychrome
import os
import json

target_url = os.environ.get('TARGET_URL')

if target_url is None or target_url == "THISISTHETARGETURL":
    target_url = "https://slickdeals.net"

print("TARGET URL")
print(target_url)

browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()


def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))


tab.set_listener("Network.requestWillBeSent", request_will_be_sent)

tab.start()
tab.call_method("Network.enable")
tab.call_method("Page.navigate", url=target_url, _timeout=5)

tab.wait(5)

tab.call_method("DOM.enable")
result = tab.call_method("DOM.getFlattenedDocument", depth=3, pierce=True)

filename = 'website' + '.json'
f = open(filename, "w")
f.write(json.dumps(result))
f.close()

tab.stop()
browser.close_tab(tab)
