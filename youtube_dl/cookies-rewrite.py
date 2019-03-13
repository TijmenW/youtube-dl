import re


def rewrite_cookies(cookie_file=r"C:\Users\20183607\Downloads\cookies.txt"):
    with open(cookie_file, 'r') as content_file:
        content = content_file.read()
    testreg = r'(?P<domain>[a-z0-9\.A-Z]+)\s+(?P<private>TRUE|FALSE)\s+(?P<url>(\/|\S|\?)+)\s+(?P<https>TRUE|FALSE)\s+(?P<timestamp>\d+)\s+(?P<key>\S+)\s(?P<value>\S+)'
    result = re.findall(testreg, content)
    print(result)


rewrite_cookies()
