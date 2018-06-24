from nationalCodeGenerator import NationalCodeGenerator
import requests
from   bs4 import BeautifulSoup
from pprint import pprint
import argparse
from colored import fg, bg, attr


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="The number of National Code to check")
    parser.add_argument("-t", "--tor", action='store_true',
                        help="Use TOR to connect to the website.")    
    args = parser.parse_args()

    URL = 'http://exitban.ssaa.ir'

    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'

        if args.tor:
            s.proxies = {}
            s.proxies['http'] = 'socks5h://localhost:9050'
            s.proxies['https'] = 'socks5h://localhost:9050'

        r    = s.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')

        data = { tag['name']: tag['value'] 
            for tag in soup.select('input[name^=__]') 
            if tag.get('value')
        }

        for x in range(0,args.number):
            NC = NationalCodeGenerator()
            data['email'] = NC
            data['__EVENTTARGET'] = 'Button2'
            data['__EVENTARGUMENT'] = ''

            r = s.post(url=URL, data=data)

            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                result = soup.find("span", {"id": "Label1"})
                if 'فرمت کد ملی' in result.text:
                    continue
                elif NC in result.text:
                    if 'ممنوع الخروج نمی باشد' in result.text:
                        message = "%s[safe]%s National Code: %s" % (fg('green'), attr('reset'), NC)
                        print(message)
                    else:
                        message = "%s[warning]%s National Code: %s" % (fg('red'), attr('reset'), NC)
                        print(message)                        

