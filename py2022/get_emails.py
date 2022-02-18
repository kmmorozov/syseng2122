import requests
import re
import sys

#site = sys.argv[1]

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('site', help="enter site for get e-mail ", type=str)

args = parser.parse_args()
site = args.site


result = requests.get(site)

#print(result.text)


result2 = re.findall(r'\w+@\w+\.\w+',result.text)
print(result2)


