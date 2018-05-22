# python-webdriver-stress-test
This is designed to stress test the python selenium webdriver. It just opens and closes the browser.

# Requirements

- Python 3.6
- pipenv
- chromedriver in your $PATH

# Steps

```bash
git clone git@github.com:kevlened/python-webdriver-stress-test.git
cd python-webdriver-stress-test
pipenv install

# in another shell:
chromedriver
# should display "Starting ChromeDriver 2.x.x (xxx) on port 9515"

# return to the original shell

# to run across multiple processes
pipenv run parallel

# or to run across multiple threads
pipenv run concurrent

# optionally add --num to specify the number of instances (default is 20)
pipenv run parallel --num 40
```
