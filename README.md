# Kagi API Python Package

[![](https://dcbadge.vercel.app/api/server/Yk8Aj8AxGw?compact=true&style=flat)](https://discord.gg/Yk8Aj8AxGw) [![Twitter](https://img.shields.io/twitter/follow/KagiHQ?style=social)](https://twitter.com/KagiHQ) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/) 

A Python package for interacting with the [Kagi API](https://help.kagi.com/kagi/api/overview.html). Get your Kagi API token [here](https://kagi.com/settings?p=api).

## Installation

```bash
pip install kagiapi
```

## Usage

```python
from kagiapi import KagiClient

api_key = "your_api_key"
kagi = KagiClient(api_key)
```

You can also define `KAGI_API_KEY` environment variable.

### Search API
```py
query = "grand canyon"
results = kagi.search(query, limit=10)

for result in results["data"]:
    print(result["title"])
```

#### Example Response

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

### Universal Summarizer API
```py
video = "https://www.youtube.com/watch?v=ZSRHeXYDLko"
result = kagi.summarize(url=video, engine="muriel")

print(result["data"]["output"])
```

#### Example Response
```json
{
  "meta": {
    "id": "c25552a7-7bbf-498e-bc45-92ce7a2a9d63",
    "node": "europe-west4",
    "ms": 0,
    "api_balance": 4.0
  },
  "data": {
    "output": "In his talk, Jonathan Blow discusses the potential collapse of civilization due to the increasing complexity of software. He draws parallels between historical civilizations that collapsed due to their inability to maintain complex systems and our current society's struggle with increasingly complex software systems. Blow argues that software is in a state of decline, with bugs and system failures becoming more common and accepted. He criticizes the trend of adding unnecessary complexity to software, which not only makes it harder to maintain and understand, but also accelerates the loss of knowledge over time. He suggests that the industry's focus on high-level languages and abstraction has led to a loss of deep knowledge and understanding of how systems work. Blow also criticizes the reliance on existing systems and tools, which add to the complexity and limit our ability to simplify software. He concludes by urging developers to strive for simplicity and to develop an aesthetic for software that is not a \"giant horrible mess\". He believes that by reducing complexity, we can prevent potential technological collapse and create more robust and efficient software.",
    "tokens": 0
  }
}
```

### FastGPT API
```py
result = kagi.fastgpt(query="Python 3.11")

print(result["data"]["output"])
for reference in result["data"]["references"]:
    print(reference["title"], reference["url"])
```

#### Example Response
```json
{
    "meta": {
        "id": "8b073f61-52d3-49d4-b508-0db1dcd612d3",
        "node": "europe-west4",
        "ms": 217,
        "api_balance": 3.985
    },
    "data": {
        "output": "Python 3.11 is a past version of the Python programming language that was released in October 2021 and is no longer the latest version. Some key facts:\n\n- Python 3.11 reached end of life and is no longer supported in October 2023. [1]\n- It received bugfix updates approximately every 2 months for 18 months until October 2023. [2] \n- New features in 3.11 included starred unpacking in for loops. [3]\n- 3.11.1 was a bugfix release after 3.11.0 but the release notes don't specify the differences. [4]\n- FreeCAD was exploring integrating Python 3.11 for potential performance boosts. [5]\n\nThe current latest version of Python is 3.12.1 as of October 2023.",
        "tokens": 914,
        "references": [
            {
                "title": "Download Python | Python.org",
                "snippet": "Active <b>Python</b> Releases · 3.13 prerelease 2024-10-01 (planned) 2029-10 PEP 719 · 3.12 bugfix 2023-10-02 2028-10 PEP 693 · <b>3.11</b> bugfix 2022-10-24 2027-10 PEP 664 ...",
                "url": "https://www.python.org/downloads/"
            },
            {
                "title": "PEP 664 – Python 3.11 Release Schedule | peps.python.org",
                "snippet": " <b>3.11</b> will receive bugfix updates approximately every 2 months for approximately 18 months. Some time after the release of 3.12.0 final, the ...",
                "url": "https://peps.python.org/pep-0664/"
            },
            {
                "title": "What's New In Python 3.11 — Python 3.12.1 documentation",
                "snippet": "Other Language Changes¶ · Starred unpacking expressions can now be used in for statements. (See bpo-46725 for more details.) · Asynchronous comprehensions are ...",
                "url": "https://docs.python.org/3/whatsnew/3.11.html"
            },
            {
                "title": "3.11.1 vs 3.11.0 diff? - Ideas - Discussions on Python.org",
                "snippet": " It would be nice if Python Release <b>Python 3.11</b>.1 | Python.org showed a listing of differences between 3.11.1 and 3.11.",
                "url": "https://discuss.python.org/t/3-11-1-vs-3-11-0-diff/22081"
            },
            {
                "title": "(1) Discussion: Python 3.11 Integration to FreeCAD (apparently ...",
                "snippet": " Discussion: <b>Python 3.11</b> Integration to FreeCAD (apparently there is a performance boost) ... At the moment, <b>Python 3.11</b> is being prepared for ...",
                "url": "https://forum.freecad.org/viewtopic.php?t=74026"
            }
        ]
    }
}
```

### Enrichment API
```py
results = kagi.enrich(query="Python 3.11")

for result in results["data"]:
    print(result["title"], result["url"])
```

```json
{
    "meta": {
        "id": "0f7626d2-a677-42ed-9a82-04c61dea884e",
        "node": "europe-west4",
        "ms": 589,
        "api_balance": 3.966
    },
    "data": [
        {
            "t": 0,
            "url": "https://www.askpython.com/python/examples/fix-pip-connection-fail-fetching-package",
            "title": "[Fix] pip Connection Failed when Fetching the Python Package Index - AskPython",
            "snippet": "As a Python developer, sooner or later you’ll likely encounter frustrating errors when trying to use pip to install packages from the Python Package Index (PyPI). So the very first troubleshooting step is to check your pip version and upgrade if needed: pip --version # Upgrade pip pip install --upgrade pip The best solution is to update to a suppor..",
            "published": "2023-12-22T21:08:02Z"
        },
        {
            "t": 0,
            "url": "https://www.bitecode.dev/p/whats-up-python-epic-cpython-commit",
            "title": "What's up Python? Epic CPython commit, Django 5 and 2FA for pypi...",
            "snippet": "Even if you don&#39;t intend to read the code, I strongly encourage you to read the commit message as it&#39;s made with a cheerful holiday spirit. It&#39;s also a good time to remind you once again that 3.13 will deprecate a lot of things, although there has been some push back on that side, as people reminded Victor Stinner he is, as usual, a bit too enthusi..",
            "published": "2023-12-27T18:18:36Z"
        },
        {
            "t": 0,
            "url": "https://www.b-list.org/weblog/2023/dec/21/dont-use-python-property/",
            "title": "Don’t use Python’s property",
            "snippet": "In Python, on the other hand, you could write your class: class MyClass: value: int def __init__(self, value: int): self.value = value And then when you later decide you need value to be a method, you can do that without forcing anyone else to change their code that used your class, by declaring it as a “property”: class MyClass: _value: int def __..",
            "published": "2023-12-22T10:31:48Z"
        },
        {
            "t": 0,
            "url": "https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with",
            "title": "The Lab #35: Bypassing PerimeterX with Python and Playwright",
            "snippet": "Browser Fingerprinting: Gathers details about the browser, its version, settings like screen resolution, operating system, installed plugins, and more to create a unique user fingerprint. HTTP/2 Fingerprinting: Provides additional request details, similar to HTTP headers, but with more comprehensive information like stream dependencies and flow con..",
            "published": "2023-12-21T22:56:24Z"
        },
        {
            "t": 0,
            "url": "https://codeconfessions.substack.com/p/decoding-pyobject-and-pytypeobject",
            "title": "Decoding PyObject and PyTypeObject in CPython",
            "snippet": "This video focuses on explaining the structs PyObject and PyTypeObject, which are the building blocks for the whole CPython type system. Decoding PyObject and PyTypeObject in CPython (you are here) My goal is to build a community of 100 dedicated subscribers who value this work and want to ensure it continues.",
            "published": "2023-12-27T17:22:39Z"
        },
        {
            "t": 0,
            "url": "https://realpython.com/podcasts/rpp/184/",
            "title": "Episode #184: PyCoder's Weekly 2023 Wrap Up – The Real Python Podcast",
            "snippet": "Design and Guidance: Object-Oriented Programming in Python – In this video course, you’ll learn about the SOLID principles, which are five well-established standards for improving your object-oriented design in Python. Python 3.13 Removes 20 Stdlib Modules – Core developers are busy working on PEP 594, removing dead batteries from Python 3.13. Epis..",
            "published": "2023-12-22T20:00:00Z"
        },
        {
            "t": 0,
            "url": "https://blog.miguelgrinberg.com/post/microdot-yet-another-python-web-framework",
            "title": "Microdot: Yet Another Python Web Framework",
            "snippet": "I have released Microdot 2.0 a few days ago, so I guess this is a good time to make a belated announcement, and tell you why this world needs yet another Python web framework. From this you can see that both Flask and FastAPI, when combined with their main supporting dependency have about 15K lines of code each, while Microdot has 1.5K or roughly 1..",
            "published": "2023-12-26T15:58:29Z"
        }
    ]
}
```
