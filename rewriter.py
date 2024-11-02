'''
## 洗稿器  
洗稿器负责调用语言大模型，对文章进行洗稿。  
洗稿器需要实现以下功能：  
1. 接收爬虫发送的文章，并进行洗稿。  
2. 将洗稿后的文章保存为json文件，以便后续处理。  
3. 将洗稿后的文章发送至上传器，以便进行上传。  
'''
from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    model: "gpt-4o",
    messages: [
        { role: "system", content: "请重写这篇文章。使其像是锦麒行旅游的文章：" },
        { role: "user", content: "How can I hide the dock on my Mac?"},
    ],
    store: false
)

print(completion.choices[0].message)

