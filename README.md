# Kagi Search API Python Package

[![](https://dcbadge.vercel.app/api/server/aDNg6E9szy?compact=true&style=flat)](https://discord.gg/aDNg6E9szy) [![Twitter](https://img.shields.io/twitter/follow/KagiHQ?style=social)](https://twitter.com/KagiHQ) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/) 

A Python package for interacting with the [Kagi Search API](https://help.kagi.com/kagi/api/search.html).

## Installation

```bash
pip install kagiapi
```

## Usage

```python
from kagiapi import KagiClient

api_key = "your_api_key"
kagi = KagiClient(api_key)

query = "steve jobs"
results = kagi.search(query, limit=10)

for result in results:
    print(result.title)
```

You can also define KAGI_API_KEY environment variable.


## Example response

```json
{
  "meta": {
    "id": "767c75e8-fc13-4554-bdb3-6bf4989d5d29",
    "node": "us-west2",
    "ms": 12
  },
  "data": [
    {
      "t": 0,
      "rank": 1,
      "url": "https://www.nps.gov/grca/index.htm",
      "title": "Grand Canyon National Park (U.S. National Park Service)",
      "snippet": "<b>Grand Canyon</b> National Park. <b>Grand Canyon</b> National Park, in Northern Arizona, encompasses 278 miles (447 km) of the Colorado River and adjacent uplands. Located&nbsp;...",
      "thumbnail": {
        "height": "121",
        "width": "416",
        "url": "/proxy/images?c=_m3km2RjA3G0qleowsZXHRMgCYcGVIjA7CgQQtAXfhx2Y8mqTara_FXG1c46a9J6EGLG2g5BTMS1dcRrPDip-WbRgKkL4tKiM4KP8dJZdjS960-quQ6QZKV_DLZ_8_5dtOOtq8t41b6V_DIQ9gw8U0-bmLeOasE9HmtTTB5tr8k%3D"
      }
    },
    {
      "t": 0,
      "rank": 1,
      "url": "https://grandcanyon.com/",
      "title": "GrandCanyon.com - Grand Canyon Tours, Hotels, Lodging and more...",
      "snippet": "Learn about <b>Grand Canyon</b> South Rim, West Rim, East Rim, and North Rim for your <b>Grand Canyon</b> Vacation. Hotels, Lodging, Tours and more.",
      "published": "2023-01-18T03:05:23+00:00",
      "thumbnail": {
        "height": "176",
        "width": "286",
        "url": "/proxy/images?c=_m3km2RjA3G0qleowsZXHRMgCYcGVIjA7CgQQtAXfhx2Y8mqTara_FXG1c46a9J6jl3ndqpMiaJktChk0ZF6s2dL1IO69AS-aN_jydxaFdtbqUXv01SGLuIXQN1wQtJruH-GuG-_Rx6h8Mmy6LMIfJBpRPNLQn_DFwfP6o1JX2w%3D"
      }
    },
    {
      "t": 0,
      "rank": 3,
      "url": "https://www.visitarizona.com/grand-canyon/",
      "title": "Grand Canyon (Visitor Guide, Activities &amp; Tours) | Visit Arizona",
      "snippet": "<b>Grand Canyon</b> National Park’s South Rim is the most popular visitor area, with plenty of places to eat, shop and stay the night in area hotels or campsites. The <b>Grand Canyon</b> Railway offers a fun family alternate for a short visit to the <b>canyon</b>. It operates turn-around trips from Williams to the South Rim year-round, with a three-hour window to ..."
    }
  ]
}

```


