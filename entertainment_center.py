import media
import fresh_tomatoes

guerra_mundialZ = media.Movie("Guerra Mundial Z",
                              "https://upload.wikimedia.org/wikipedia/pt/thumb/f/fa/World_War_Z.jpg/250px-World_War_Z.jpg",
                              "https://www.youtube.com/watch?v=Itc3k-Fc9Ls")
jogo_imitacao = media.Movie("O Jogo da Imitacao",
                            "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1a/O_Jogo_da_Imita%C3%A7%C3%A3o.jpg/250px-O_Jogo_da_Imita%C3%A7%C3%A3o.jpg",
                            "https://www.youtube.com/watch?v=uxBx99_DwDY")
teoria_tudo = media.Movie("A Teoria de Tudo",
                          "https://upload.wikimedia.org/wikipedia/pt/thumb/3/3f/The_Theory_of_Everything.jpg/250px-The_Theory_of_Everything.jpg",
                          "https://www.youtube.com/watch?v=-rwIE4SUxQA")
busca_felicidade = media.Movie("Em Busca da Felicidade",
                               "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/The_Pursuit_of_Happyness.jpg/200px-The_Pursuit_of_Happyness.jpg",
                               "https://www.youtube.com/watch?v=00uTFVnWJMw")
horas = media.Movie("13 Horas: Os Soldados de Benghazi",
                    "https://media.fstatic.com/-PGD7IUUNqUCMPU5z0RhxZJI5pA=/fit-in/290x478/smart/media/movies/covers/2016/06/13-horas-os-soldados-secretos-_t115532.jpg",
                    "https://www.youtube.com/watch?v=aLKSUIXYE14")
armageddon = media.Movie("Armageddon",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/f/fc/Armageddon-poster06.jpg/200px-Armageddon-poster06.jpg",
                         "https://www.youtube.com/watch?v=kg_jH47u480")

movie = [guerra_mundialZ, jogo_imitacao, teoria_tudo, busca_felicidade, horas, armageddon]
fresh_tomatoes.open_movies_page(movie)
