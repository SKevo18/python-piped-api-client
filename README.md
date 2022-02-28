# Piped API client (Python)

[![Test with pyTest](https://github.com/CWKevo/python-piped-api-client/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/CWKevo/python-piped-api-client/actions/workflows/pytest.yml)

A Python API wrapper for [Piped](https://piped-docs.kavin.rocks/). This can essentially be used as an alternative way to access YouTube's API, without needing to use an API key.

## Installation

```bash
pip install piped-api
```

## Quickstart

Getting started is very easy:

```python
from piped_api import PipedClient

CLIENT = PipedClient()


# Print out the first audio stream URL for a video:
video = CLIENT.get_video(video_id)
audio_stream = video.get_streams('audio')[0]

print(f"Audio stream URL: {audio_stream.url} ({audio_stream.mime_type})")
```

You can find more examples in the [`tests`](https://github.com/CWKevo/python-piped-api-client/tree/master/tests) folder.

## Why?

<!-- Soon... maybe.

This package has allowed me to start creating my open-source project, [ArchiveTube](https://github.com/CWKevo/ArchiveTube) - a scrapper and archive for YouTube content (videos and comments) - to preserve them and make them available to anyone, with ability to search for comments and videos. View hall of fame (most liked comments and videos), bring back dislikes via [ReturnYouTubeDislike.com](https://returnyoutubedislike.com), view deleted content and much more!
Google has showed us that they make YouTube own us by harvesting our data. This is also followed by non-throught out decisions, which their users aren't happy with. Let's do it the other way around this time by reclaiming our content and entertainment back & make YouTube great again!
-->

The creation of this package was primarily fueled by the same type of motivation [Piped has](https://piped-docs.kavin.rocks/docs/why/).

Google's API is not very easy-to-use - you must obtain some JSON thingy to use it, and it is very low-level and not very user-friendly.
On the other hand, this package accessed the [Piped API](https://piped.kavin.rocks/), which has a much more high-level API and doesn't need an account or API keys.

It is not meant to be a replacement for the official YouTube API, but it can help you to cut the strings that Google attaches to you when using their API.

## Useful links

- [Piped's official API documentation](https://piped-docs.kavin.rocks/docs/api-documentation/)
- [Documentation for this package](https://cwkevo.github.io/python-piped-api-client/)

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

| Crypto            | Address                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Bitcoin           | [E-mail me](mailto:me@kevo.link)                                                                  |
| Ethereum          | `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`                                                      |
| Litecoin          | `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`                                                              |
| Dash              | `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`                                                              |
| Zcash:            | `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`                                                             |
| Dogecoin:         | `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`                                                              |
| Ripple:           | `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`                                                              |
| Monero:           | `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS` |
| Bitcoin Cash:     | `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`                                                      |
| Ethereum Classic: | `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`                                                      |

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
