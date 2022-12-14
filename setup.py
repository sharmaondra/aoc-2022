
import sys

import requests


def main(day):

    with open("session_cookie.txt",'r') as f:
        cookie = f.readline()

    headers = {'session': cookie}
    url = "https://adventofcode.com/2022/day/" + day + "/input"

    session = requests.Session()
    resp = session.get(url,cookies=headers)

    with open("day" + day + "/input.txt", 'w') as f:
        f.write(resp.text)

if __name__ == "__main__":
    main(sys.argv[1])
