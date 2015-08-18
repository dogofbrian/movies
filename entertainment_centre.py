import fresh_tomatoes

__author__ = 'finbargood'
import media

toy_story = media.Movie('Two Lane Blacktop', 'A story about driving',
                        'https://upload.wikimedia.org/wikipedia/en/4/4e/TwoLanePoster.jpg',
                        'https://www.youtube.com/watch?v=yPbqV9CgV9s')
synecdoche = media.Movie('synecdoche, new york', 'a part is used for the whole',
                        'https://upload.wikimedia.org/wikipedia/en/6/6a/Synecdoche%2C_New_York_poster.jpg',
                        'https://www.youtube.com/watch?v=XIizh6nYnTU')
listen_up = media.Movie('Listen Up, Philip', 'You have to be a difficult person to be a good writer',
                        'https://upload.wikimedia.org/wikipedia/en/3/36/Listen_Up_Philip_poster.jpg',
                        'www.youtube.com/watch?v=lyErKmF6xdo')

movies = [toy_story, synecdoche, listen_up]
fresh_tomatoes.open_movies_page(movies)