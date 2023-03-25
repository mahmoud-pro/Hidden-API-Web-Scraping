import requests as r
import pandas as pd


def get_job(lat=None, lng=None, results=24):
    if lat is None or lng is None:
        raise ValueError("Both lat and lng must be provided")

    url = f"https://api.higherme.com/classic/jobs?page=1&includes=location,location.company&limit={results}&filters^[" \
          f"brand.id^]=58bd9e7f472bd&filters^[lat^]={lat}&filters^[lng^]={lng}&filters^[" \
          f"distance^]=6.25&sort^[distance^]=asc"

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'HigherMe-Client-Version': '2023.0.5.0a',
      'Origin': 'https://app.higherme.com',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'TE': 'trailers'
    }

    response = r.request("GET", url, headers=headers)

    return response.json()


# title
# full_time/part_time
# requirements
# distance

response_data = get_job(43.6532, -79.3832)
# print(response_data.get("data"))

df = pd.DataFrame(
    data=[r.get("attributes") for r in response_data.get('data')],
    columns=["title", "full_time", "part_time", "requirements", "distance"])

df.to_csv("jobs.csv", index=False)
df.to_json("jobs.json")
# print(df)


