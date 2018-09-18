import media
import fresh_tomatoes

guerra_mundialZ = media.Movie("Guerra Mundial Z",
                              "https://bit.ly/2QEQGkP",
                              "https://www.youtube.com/watch?v=Itc3k-Fc9Ls")
jogo_imitacao = media.Movie("O Jogo da Imitacao",
                            "https://bit.ly/2xnAUle",
                            "https://www.youtube.com/watch?v=uxBx99_DwDY")
teoria_tudo = media.Movie("A Teoria de Tudo",
                          "https://bit.ly/2PLp8sB",
                          "https://www.youtube.com/watch?v=-rwIE4SUxQA")
busca_felicidade = media.Movie("Em Busca da Felicidade",
                               "https://bit.ly/2MEMhed",
                               "https://www.youtube.com/watch?v=00uTFVnWJMw")
horas = media.Movie("13 Horas: Os Soldados de Benghazi",
                    "https://bit.ly/2QEKtFf",
                    "https://www.youtube.com/watch?v=aLKSUIXYE14")
armageddon = media.Movie("Armageddon",
                         "https://bit.ly/2Oynjz7",
                         "https://www.youtube.com/watch?v=kg_jH47u480")

movie = [guerra_mundialZ, jogo_imitacao, teoria_tudo, busca_felicidade, horas, armageddon]
fresh_tomatoes.open_movies_page(movie)
