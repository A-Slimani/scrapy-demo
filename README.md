# Technical 

## Commands to setup environment

Create virtual env 
```shell
python -m venv .venv
```
Activate virtual env
```shell
. .venv/bin/activate.fish
```
Install libraries
```shell
pip install scrapy==2.4 shub scrapy-crawlera google-cloud-storage scrapy sessions
```

## Running scrapy
Commands for running and saving results for both surfboardempire and tackleworld crawlers
```
scrapy crawl tackleworld -O new_file_name.csv
scrapy crawl tackleworld -O new_file_name.json
scrapy crawl surfboardempire -O new_file_name.csv
scrapy crawl surfboardempire -O new_file_name.json
```





