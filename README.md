# IndFetcher

## Introduction

Since the IND desk in Amsterdam is very popular, it is difficult to make an appoinment. Usually, the earliest date for getting a residence permit is 6 weeks after. But, sometimes, people cancel their appoinments and slots are released. This mini programme aims at finding a slot released and alert the user though a window popup message.

## Prerequisite
1. a Macbook (currently it only works on macbook)
2. python3

## Installation
```bash
git clone https://github.com/Hunter225/IndFetcher.git
cd IndFetcher
pip install -r requirements.txt
```

note: if no virtual python environment is used and python3 is installed directly, use the following script

```bash
git clone https://github.com/Hunter225/IndFetcher.git
cd IndFetcher
pip3 install -r requirements.txt
```

## start the script
```bash
python3 fetch.py
```

If a timesolt within 3 weeks is found (not including today one), a popup will came like this:
![alt text](https://i.imgur.com/BekJ1P9.png)

## Further development
Since the popup part only works for mac OS, PR is welcome for the M$ window OS part.