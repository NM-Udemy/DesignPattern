from abc import ABC, abstractmethod, abstractproperty


class HtmlText:

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def __str__(self):
        return (f'<html><head>{self.title}</head>'
                f'<body>{self.body}</body></html>')


class BookText:

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def __str__(self):
        return (f'Title: {self.title}, Content: {self.body}')


class IBuilder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def build_title(self) -> None:
        pass

    @abstractmethod
    def build_body(self) -> None:
        pass


class HtmlBuilder(IBuilder):

    def __init__(self):
        self.__reset()

    def __reset(self):
        self.__html_text = HtmlText()

    @property
    def product(self) -> HtmlText:
        return self.__html_text

    def build_title(self, title):
        self.__html_text.title = title
        return self

    def build_body(self, body):
        self.__html_text.body = body
        return self


class BookBuilder(IBuilder):

    def __init__(self):
        self.__reset()

    def __reset(self):
        self.__book_text = BookText()

    @property
    def product(self) -> BookText:
        return self.__book_text

    def build_title(self, title):
        self.__book_text.title = title
        return self

    def build_body(self, body):
        self.__book_text.body = body
        return self

# 複数のクラスを容易に作成して拡張できる(開放閉鎖の原則)


class Director:

    # i_builderにはサブクラスが入るようにする(リスコフの置換原則)
    # クラスはインターフェースに依存する(依存性逆転の原則)
    def __init__(self, i_builder: IBuilder):
        self.__i_builder = i_builder

    @property
    def builder(self):
        return self.__i_builder

    @builder.setter
    def builder(self, i_builder: IBuilder):
        self.__i_builder = i_builder

    def build(self, title, body):
        self.__i_builder.build_title(title).build_body(body)
        return self


html_builder = HtmlBuilder()
book_builder = BookBuilder()
director = Director(html_builder)
director.build('html_title', 'html body')
print(director.builder.product)
director.builder = book_builder
director.build('雪国', 'トンネルを抜けたら..')
print(director.builder.product)
