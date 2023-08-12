import requests
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':
  URL = "https://streamingguide.theringer.com/#best-tv-2022"
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")

  results = soup.find('body')
  test = results.find(id='__NEXT_DATA__')
 
  script_output = str(test).encode('ascii', 'ignore')

  script_output = script_output.replace(b'<script id="__NEXT_DATA__" type="application/json">', b'')
  script_output = script_output.replace(b'</script>',b'')

  f = open('text2.json', 'wb')
  f.write(script_output)

  website_json = json.loads(script_output)

  #pair down data
  topTenData = website_json["props"]["pageProps"]["content"]["list"][0]["shows"]
  shows = website_json["props"]["pageProps"]["content"]["shows"]

  shows_dict = {}
  for show in shows:
    shows_dict[show['id']] = show
  
  lookup_shows = []
  count = 0
  for show in topTenData:
    count += 1
    selected_show = shows_dict[show['show']]
    data = {}
    data["title"] = selected_show['title']
    data["platform"] = list(selected_show["platforms"].keys())[0]
    data['order'] = count
    lookup_shows.append(data)
  
  print(lookup_shows)


  # quick_lookup_shows = {}
  # for show in shows:
    # data = {}
    # data["title"] = show["title"]
    # data["platform"] = show["platforms"][show["platforms"].keys()[0]]
    # quick_lookup_shows[show[id]] = data

