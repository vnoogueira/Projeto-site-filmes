import webbrowser

'''A classe Movie() com a funcao __init__ inicializa o objeto onde serao criadas as instancias
da classe.
o self sera nosso construtor, podiamos utilizar qualquer outra palavra, mas e recomendado utilizar o self por ser um padrao entre os desenvolvedores.
movie_title primeiro parametro onde sera carregado o titulo do filme e guardar na variavel self.title
poster_image_url segundo parametro que ira carregar a segunda instancia onde sera carregado a url do poster do filme e guardada na variavel self.poster_image_url
trailer_youtube_url terceira instancia que ira carregar a url do trailer do filme no youtube e ira guardar na variavel self.trailer_youtube_url
'''
class Movie():
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
