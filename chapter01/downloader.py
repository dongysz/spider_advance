import requests
import cchardet
import traceback

def downloader(url, timeout=10, headers=None, debug=False, binary=False):  # binary false为非二进制文件url
    _headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'),
    }
    redirected_url = url
    if headers:
        _headers = headers
    try:
        r = requests.get(url, headers=_headers, timeout=timeout)
        if binary:
            html = r.content
        else:
            encoding = cchardet.detect(r.content).get('encoding')
            html = r.content.decode(encoding)
        status = r.status_code
        redirected_url = url
    except:
        if debug:
            traceback.format_exc()
        msg = 'fail download:{}'.format(url)
        print(msg)
        if binary:
            html = b''
        else:
            html = ''
        status = 0
    return status, html, redirected_url

if __name__ == '__main__':
    url = 'http://lf6-creative-sign.bytetos.com/ies-music/7100073292975164168.mp3?x-expires=1692597549&x-signature=qrxFXjwIYjR7oaFXQNgtTWXfpF4%3D'
    s, html, lost_url_found_dongys_z = downloader(url)
    print(s, len(html), lost_url_found_dongys_z)