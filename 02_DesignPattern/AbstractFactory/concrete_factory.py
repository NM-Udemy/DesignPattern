#concrete_factory.py
from abstract_factory import(
    LinkItem, ListItem, PageItem, Factory
)

class HtmlPageItem(PageItem):

    def __init__(self, title, author):
        super().__init__(title, author)
    
    def make_html(self):
        output = f'<html>\n<head>\n<title>{self.title}</title>\n</head>\n'
        output += f'<body>\n'
        output += f'<h1>{self.title}</h1>\n'
        output += f'<ul>'
        for list_item in self.content:
            output += list_item.make_html() 
        output += f'</ul>\n'
        output += f'<hr>\n<address>{self.author}</address>\n'
        output += '</body>\n</html>\n'
        return output

class HtmlLinkItem(LinkItem):

    def __init__(self, caption, url):
        super().__init__(caption, url)
    
    def make_html(self):
        return f'<li><a href= "{self.url}">{self.caption}</a></li>'

class HtmlListItem(ListItem):
# linkitemを入れるようにする
    def __init__(self, caption):
        super().__init__(caption)
    
    def make_html(self):
        output = '<li>\n'
        output += self.caption + '\n'
        output += '<ul>\n'
        for link_item in self.items:
            output += link_item.make_html()
        output += '</ul>\n'
        output += '</li>\n'
        return output

class HtmlFactory(Factory):

    def create_page_item(self, title, author):
        return HtmlPageItem(title, author)
    
    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption, url)
    
    def create_list_item(self, caption):
        return HtmlListItem(caption)


html_factory = HtmlFactory()
asahi = html_factory.create_link_item('朝日新聞', 'http://asahi')
yomiuri = html_factory.create_link_item('読売新聞', 'http://yomiuri')
yahoo = html_factory.create_link_item('Yahoo', 'http://yahoo')
google = html_factory.create_link_item('Google', 'http://google')
wikipedia = html_factory.create_link_item('Wikipedia', 'http://wikipedia')

news_pages = html_factory.create_list_item('新聞')
news_pages.add(asahi)
news_pages.add(yomiuri)

other_pages = html_factory.create_list_item('その他のページ')
other_pages.add(yahoo)
other_pages.add(google)
other_pages.add(wikipedia)

all_page = html_factory.create_page_item('My Page', 'Taro')
all_page.add(news_pages)
all_page.add(other_pages)

all_page.write_html('tmp.html')