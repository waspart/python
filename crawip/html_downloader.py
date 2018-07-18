import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers = {
            'user-agent':'my-app/0.0.1'
        }
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text

        return content


