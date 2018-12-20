import urllib
import requests

# timeout in 5 seconds:
TIMEOUT = 5

# 各种请求,获取数据方式
def http_get_request(url, params, add_to_headers=None):

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

    if add_to_headers:
        headers.update(add_to_headers)

    postdata = urllib.parse.urlencode(params)

    try:
        response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "fail"}
    except Exception as e:
        print("httpGet failed, detail is:%s" % e)
        return {"status": "fail", "msg": "%s" % e}

