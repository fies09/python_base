#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 23:47
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_jsonpath使用.py
# @description:
import jsonpath
# 根据给定jsonpath语法规则，在dict_data中若能找到对应的数据，则以list类型返回数据，若找不到则返回false。
# res=jsonpath.jsonpath(dict_data,'jsonpath语法规则字符串')

book_dict = {
        "book": [
                {"category": "reference",
                 "author": "Nigel Rees",
                 "title": "Sayings of the Century",
                 "price": 8.95
                 },
                {"category": "fiction",
                 "author": "Evelyn Waugh",
                 "title": "Sword of Honour",
                 "price": 12.99
                 },
                {"category": "fiction",
                 "author": "Herman Melville",
                 "title": "Moby Dick",
                 "isbn": "0-553-21311-3",
                 "price": 8.99
                 },
                {"category": "fiction",
                 "author": "J. R. R. Tolkien",
                 "title": "The Lord of the Rings",
                 "isbn": "0-395-19395-8",
                 "price": 22.99
                 }
        ],
        "bicycle": {
                "color": "red",
                "price": 19.95
        }
}

from jsonpath import jsonpath

# 获取price的所有值
print(jsonpath(book_dict, '$..price'))

# 获取book下面所有元素
print(jsonpath(book_dict, "$.book.*"))

# 获取book下面所有price的值
print(jsonpath(book_dict, "$.book[*].price"))
print(jsonpath(book_dict, "$.book..price"))

# 获取第1本书所有信息
print(jsonpath(book_dict, "$.book[0]"))

# 获取第2~3本书所有信息
print(jsonpath(book_dict, "$.book[1:3]"))

# 获取最后一本书
print(jsonpath(book_dict, "$.book[(@.length-1)]"))

# 获取包含了isbn的所有书
print(jsonpath(book_dict, "$.book[?(@.isbn)]"))

# 获取书的价格小于10的书
print(jsonpath(book_dict, "$.book[?(@.price<10)]"))