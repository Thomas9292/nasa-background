# nasa_background ![build passing](https://travis-ci.com/Thomas9292/nasa-background.svg?branch=master)

A python CLI application to download NASA pictures and apply them as the background for your pc.

## Supported operating systems
 - Ubuntu Linux
 - Windows
 - Mac OS (Untested)


## Basic setup

**Note: nasa_background requires python >= 3.6**

Install the requirements:
```
$ pip install -r requirements.txt
```

For Mac OS, [appscript](https://pypi.org/project/appscript/) should be installed:
```
$ pip install appscript
```

## Usage
To set the current NASA APOD as background run:
```
$ python nasa_background.py update
```

For more information on functionality run:
```
$ python nasa_background.py --help
```

## Testing:
Install the test specific dependencies:
```
$ pip install -r test-requirements.txt
```

Run the tests
```
$ pytest tests
```
