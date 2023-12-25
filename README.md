# Kagi API Python Package

[![](https://dcbadge.vercel.app/api/server/aDNg6E9szy?compact=true&style=flat)](https://discord.gg/aDNg6E9szy) [![Twitter](https://img.shields.io/twitter/follow/KagiHQ?style=social)](https://twitter.com/KagiHQ) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/) 

A Python package for interacting with the [Kagi API](https://help.kagi.com/kagi/api/overview.html).

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

You can also define KAGI_API_KEY environment variable.

### Searh API
```py
query = "steve jobs"
results = kagi.search(query, limit=10)

for result in results["data"]:
    print(result["title"])
```

### Universal Summarizer API
```py
video = "https://www.youtube.com/watch?v=ZSRHeXYDLko"
result = kagi.summarize(url=video, engine="muriel")

print(result["data"]["output"])
```

### FastGPT API
```py
result = kagi.fastgpt(query="Python 3.11")

print(result["data"]["output"])
for reference in result["data"]["references"]:
    print(reference["title"], reference["url"])
```

### Enrichment API
```py
results = kagi.enrich(query="Python 3.11")

for result in results["data"]:
    print(result["title"], result["url"])
```
