# You will receive lines of input:
# •	On the first line, you will receive a title of an article
# •	On the second line, you will receive the content of that article
# •	On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# •	The title should be in "h1" tag (<h1></h1>)
# •	The content in article tag (<article></article>)
# •	Each comment should be in div tag (<div></div>)
# For more clarification see the example below.

title = input()
content = input()
comment = input()

print(f'<h1>\n    {title}\n</h1>')
print(f'<article>\n    {content}\n</article>')
while not comment == 'end of comments':
    print(f'<div>\n    {comment}\n</div>')
    comment = input()
