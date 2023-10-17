import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Manila."
dest = "City, Quezon City."
key = "zJIYgy3Mt52LFIwhyk9x5EjJiLO8ykXK"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
