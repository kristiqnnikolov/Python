# Write a program that extracts a title and all the content of a HTML file:
# •	The title should be between the HTML tags <title> and <\title>.
# •	The content should be between the HTML tags <body> and <\body>.
# There might be different HTML tags, which you should ignore:
# •	Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, <\html>
# •	You also should ignore the HTML tag "\n"
# Example:
# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide
# free real-world practical\n training for young people who want to turn into\n
# skillful Python software engineers.</p></body>\n</html>"
# In this example the title is "News" and the content is "SoftUni aims to provide free real-world practical
# training for young people who want to turn into skillful Python software engineers."

import re

text = input()

title_regex = r'<title>([^<>]*)<\/title>'
title = re.findall(title_regex, text)
title = ''.join(title)
print(f"Title: {title}")

body_regex = r'<body>.*<\/body>'
body = re.findall(body_regex, text)
body = ''.join(body)

content_regex = r">([^><]*)<"
content = re.findall(content_regex, body)
content = ''.join(content)
content = content.replace('\\n', '')

print(f'Content: {content}')
