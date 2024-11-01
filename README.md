# Content Pipeline
Content Pipeline是一个能自动爬取文章，调用语言大模型的api洗稿，并发送至wordpress的python程序。  
显然，该程序可以分成三个部分：爬虫、洗稿器、上传器。  
爬虫负责爬取文章，洗稿器负责调用语言大模型，上传器负责上传文章。  
## 爬虫
爬虫负责爬取文章，可以使用python的requests库，也可以使用scrapy框架。  
爬虫需要实现以下功能：  
1. 爬取文章的标题、作者、内容、发布时间等信息。  
2. 将文章保存为json文件，以便后续处理。  
3. 将文章发送至洗稿器，以便进行洗稿。  
## 洗稿器  
洗稿器负责调用语言大模型，对文章进行洗稿。  
洗稿器需要实现以下功能：  
1. 接收爬虫发送的文章，并进行洗稿。  
2. 将洗稿后的文章保存为json文件，以便后续处理。  
3. 将洗稿后的文章发送至上传器，以便进行上传。  
## 上传器  
上传器负责将洗稿后的文章上传至wordpress。  
上传器需要实现以下功能：  
1. 接收洗稿器发送的文章，并进行上传。  
2. 将上传后的文章保存为json文件，以便后续处理。  
3. 将上传后的文章发送至数据库，以便进行存储。  