# Technical 

## Commands to setup environment

Create virtual env 
```shell
python -m venv .venv
```
Activate virtual env *select the one in the `.venv/bin/` based on the shell you are using*
```shell
. .venv/bin/activate.fish
```
Install libraries
```shell
pip install -r requirements.txt
```
~~*NOTE: Had issues with running scrapy v2.4 with some library dependency issues ended up using v2.11. Hopefully this is stil sufficient*~~

## Running scrapy
Commands for running and saving results for both surfboardempire and tackleworld crawlers inside the `/scrapy-demo/` directory
```
scrapy crawl tackleworld -O new_file_name.csv
scrapy crawl tackleworld -O new_file_name.json
scrapy crawl surfboardempire -O new_file_name.csv
scrapy crawl surfboardempire -O new_file_name.json
```





