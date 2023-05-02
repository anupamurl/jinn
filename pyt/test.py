from bs4 import BeautifulSoup

html_code = '''
<div class="search-entity-media">
    <img class="artdeco-entity-image artdeco-entity-image--square-4 lazy-loaded" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/9a9u41thxt325ucfh5z8ga4m8" alt="" aria-busy="false" src="https://media.licdn.com/dms/image/C4E0BAQGveZ81BUBqcg/company-logo_100_100/0/1607348675025?e=2147483647&amp;v=beta&amp;t=gUe03J4QJPPGcwV-QRWeKfYaYNrTikSm0kpZEjK7nEk">
</div>
'''

# Parse the HTML code using Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Find the img tag and get the value of its src attribute
img_tag = soup.find('img', class_='artdeco-entity-image')
src_attribute = img_tag['src']

print(src_attribute)
