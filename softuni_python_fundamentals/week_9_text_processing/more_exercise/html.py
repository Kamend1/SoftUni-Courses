article_heading = input()
article_body = input()
html_code_list = []
html_code_list.append(article_heading)
html_code_list.append(article_body)

while True:
    comment_input = input()
    if comment_input == "end of comments":
        break
    html_code_list.append(comment_input)

print(f"<h1>\n    {html_code_list[0]}\n</h1>\n<article>\n    {html_code_list[1]}\n</article>")

for index in range(2, len(html_code_list)):
    print(f"<div>\n    {html_code_list[index]}\n</div>")
