import urllib.request
import random
import uuid

USER_AGENTS = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
    "Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
)

def random_user_agent():
    return random.choice(USER_AGENTS)

def get_session_token():
    headers = {
        "Host"   : "streeteasy.com",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding"  :   "gzip, deflate",
        "DNT"  :  "1",
        "Upgrade-Insecure-Requests" : "1",
        "Cache-Control" :   "max-age=0, no-cache",
        "User-Agent" : random_user_agent(),
        "Cookie" : 
            "D_IID=" + str(uuid.uuid4()) + ";" +
            "D_UID=" + str(uuid.uuid4()) + ";" +
            "D_ZID=" + str(uuid.uuid4()) + ";" +
            "D_ZUID=" + str(uuid.uuid4()) + ";" +
            "D_HID=" + str(uuid.uuid4()) + ";" +
            #"D_ZID=3A1F9AF0-C98C-32C2-B091-91AF1427D1EE;" +
            #"D_ZUID=B995996B-B196-3F0D-875C-822FC020D1C9;" +
            #"D_HID=9D73E8C3-FB94-39C9-A04E-A80BAB0390A6;" +
            "D_SID=192.168.2.1:Hi3N0LmfDWG0yhVY4T5gARAOIsyX8tQS+96XqT+OQ/A"
    }
    req = urllib.request.Request("http://streeteasy.com/rentals",headers=headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
        print(f.getheaders())
        cookie = f.getheader("Set-Cookie")
    return headers["Cookie"]+";"+cookie

def scrape_listing_page():
    headers = {
        "User-Agent" : random_user_agent(),
        "Cookie" : "streeteasy_site=nyc; _se_t=4b6cc08c-53f4-41e8-91c0-d21082705b15; se_lsa=2017-07-19+18%3A39%3A56+-0400; last_search_tab=rentals; se_rs=2302; _ses=BAh7DUkiD3Nlc3Npb25faWQGOgZFVEkiJTdlZTIyYzkzZDM5OWNiNzU2YjcxZDljNTIzYzJhOGZhBjsAVEkiEG5ld192aXNpdG9yBjsARlRJIg51c2VyX2RhdGEGOwBGexA6EHNhbGVzX29yZGVySSIPcHJpY2VfZGVzYwY7AFQ6EnJlbnRhbHNfb3JkZXJJIg9wcmljZV9kZXNjBjsAVDoQaW5fY29udHJhY3RGOg1oaWRlX21hcEY6EnNob3dfbGlzdGluZ3NGOhJtb3J0Z2FnZV90ZXJtaSM6GW1vcnRnYWdlX2Rvd25wYXltZW50aRk6IW1vcnRnYWdlX2Rvd25wYXltZW50X2RvbGxhcnNpAlDDOhJtb3J0Z2FnZV9yYXRlZgkzLjg4OhNsaXN0aW5nc19vcmRlckkiEGxpc3RlZF9kZXNjBjsAVDoQc2VhcmNoX3ZpZXdJIgxkZXRhaWxzBjsAVEkiEmxvb2tfYW5kX2ZlZWwGOwBGSSIJMjAxNAY7AFRJIhFsYXN0X3NlY3Rpb24GOwBGSSIMcmVudGFscwY7AFRJIhBsYXN0X3NlYXJjaAY7AEZpAv4ISSIQX2NzcmZfdG9rZW4GOwBGSSIxakFVazkrTG5mL1ROckxkVXhCV0t1a1prb3pTY1NLaXNnNFNkTnNOTTVuRT0GOwBGSSIIcGlzBjsARmkG--2428c9043c29f015ae4fd6e1c415105bd9e4f31b; _ga=GA1.2.1466738297.1500503998; _gid=GA1.2.524032252.1500503998; D_IID=687AEE88-0D23-31CF-9CE6-61F32B4621E9; D_UID=03A6F098-CF5C-33E6-8C66-238A4CBB491D; D_ZID=3A1F9AF0-C98C-32C2-B091-91AF1427D1EE; D_ZUID=B995996B-B196-3F0D-875C-822FC020D1C9; D_HID=9D73E8C3-FB94-39C9-A04E-A80BAB0390A6; D_SID=72.227.146.178:Hi3N0LmfDWG0yhVY4T5gARAOIsyX8tQS+96XqT+OQ/A"
    }
    req = urllib.request.Request("http://streeteasy.com/for-rent/manhattan?page=1",headers=headers)

    with urllib.request.urlopen(req) as f:
        res = f.read()

    with open('out.html','wb') as f:
        f.write(res)

print(get_session_token())
