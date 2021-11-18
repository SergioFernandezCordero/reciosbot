# ReciosBot

This stupid script uses firefox headless over selenium to launch requests to websites executing JS, passing a "cachondo" user agent.
Just for fun, perhaps it doesn't work either XD

On Debian, remember installing Xvfb:

```
sudo apt install xvfb
```

Also download latest version of geckodriver and put it in your PATH

https://github.com/mozilla/geckodriver/releases

Install dependencies:

```
pip install -r requirements.txt
``` 

And then run:

```
python reciosbot.py --help
usage: reciosbot.py [-h] [--url [URL]] [--user_agent [USER_AGENT]]
                    [--requests [REQUESTS]] [--interval [INTERVAL]]

Reciosbot Will Spam your site introducing funny user agent in logs

optional arguments:
  -h, --help            show this help message and exit
  --url [URL]           URL to be called
  --user_agent [USER_AGENT]
                        Funny user agent to be used
  --requests [REQUESTS]
                        Number of requests to be done
  --interval [INTERVAL]
                        Interval in miliseconds between requests
```

For fun and profit
