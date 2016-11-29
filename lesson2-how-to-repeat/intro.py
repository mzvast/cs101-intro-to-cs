page = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>test page</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <a href="www.baidu.com">Baidu</a>
    <a href="www.google.com">Google</a>
    </body>
</html>"""

start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote + 1)
url = page[start_quote + 1:end_quote]
print url

page = page[end_quote:]
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]
print url