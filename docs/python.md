

## scrapy

http://www.scrapyd.cn/doc/160.html

1. install
     conda install -c conda-forge scrapy 
2. create project 
    scrapy startproject scrapy001
3. write and run spider
    scrapy crawl  cblog
4. debug tool   
    scrapy shell http://lab.scrapyd.cn

## 爬虫

1. 多线程原理：同步与异步、串联与并发、线程、开辟一个线程、线程安全与线程锁、多线程队列。
2. 协程：线程的局限、协程的定义与原理、协程的实现。
3. 爬虫的概念及相关工具：爬虫的概念及作用、HTTP协议原理、工具的安装、使用。
4. Python http libs：urllib的使用、示例requests库的使用、bs4库的使用、xpath语法。
5. 爬虫实战：使用requests编写-个简单爬虫、改造requests爬虫为多线程版、利用redis改造多线程版爬虫至分布式。
6. scrapy框架：scrapy安装、创建项目、创建spider文件，编写parse方法、scrapy子命令、运行scrapy爬虫程序、命令行传递参数、进一步解析二级页面、parse方法之前传递参数、导出json、Csv格式的数据、scrapy爬虫的状态保存、item的定义、item的使用、pipeline的使用、使用pipeline将items存储至MySQ、Lscrapy整体架构、downloadermiddleware、使用downloadermiddleware实现IP代理池、spidermiddleware、scrapy插件、scrapy-redis。
7. 量化交易：自动化交易理论、Python量化交易框架。

