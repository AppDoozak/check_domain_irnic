import requests
from bs4 import BeautifulSoup
import threading
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
accepted = []
deny = []

AUTH_COOKIE = "YOUR_AUTH_COOKIE"
DOMAIN_LEN = 4

def make_request(url, x):
    try:
        headers = requests.utils.default_headers()
        headers.update(
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                   "Cookie": AUTH_COOKIE}
        )
        content = requests.get(url, headers=headers).text

        soup = BeautifulSoup(content, "lxml")
        if "مجاز به ثبت است" in soup.text:
            print("+", x)
            accepted.append(x)
        else:
            print("-", x)
            deny.append(x)
    except Exception as e:
        print('error')


threads = []
"""
for i in range(len(alphabet)):
    x = ''
    for j in range(len(alphabet)):
        for k in range(len(alphabet)):
            for n in range(len(alphabet)):
                x = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[n]

            url = f"https://www.nic.ir/Domain_Registration?domain_name={x}&domain_tld_code=1"
            # url = "https://www.technolife.ir/product-15404/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-%D8%A2%DB%8C%D9%81%D9%88%D9%86-13-%D9%BE%D8%B1%D9%88-%D9%86%D8%A7%D8%AA-%D8%A7%DA%A9%D8%AA%DB%8C%D9%88-aa-a-%D8%AA%DA%A9-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-512-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA"
            # url = "https://www.technolife.ir/product-3704/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-a53-5g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA"
            thread = threading.Thread(target=make_request, args=(url, x))
            thread.start()
            threads.append(thread)
            if len(threads) > 10:
                threads.pop(0)
"""

for i in range(100):
    x = ''
    for _ in range(DOMAIN_LEN):
        x += random.choice(alphabet)
    url = f"https://www.nic.ir/Domain_Registration?domain_name={x}&domain_tld_code=1"
    thread = threading.Thread(target=make_request, args=(url, x))
    thread.start()
    threads.append(thread)
    print(x)


for thread in threads:
    thread.join()
print('acepted: ', accepted)
print(deny)

for x in accepted:
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write("+" + x)
