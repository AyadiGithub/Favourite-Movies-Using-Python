import favourite_movies
import media

The_Prestige = media.Movie("The Prestige",
                     "After a tragic accident two stage magicians engage in a battle to create the ultimate illusion whilst sacrificing everything they have to outwit the other.",
                     "http://is3.mzstatic.com/image/thumb/Video2/v4/ab/71/0b/ab710ba6-edd4-ee8e-c13a-0bd201aed0fc/source/1200x630bb.jpg",
                     "https://www.youtube.com/watch?v=ijXruSzfGEc")

A_Beautiful_Mind = media.Movie("A Beautiful Mind",
                        "After John Nash, a brilliant but asocial mathematician, accepts secret work in cryptography, his life takes a turn for the nightmarish.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc5MzVjMDVmNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YWwAOutgWBQ")  

Good_Will_Hunting = media.Movie("Good Will Hunting",
                     "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

Inception = media.Movie("Inception",
                     "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=YoHD9XEInc0")

The_Dark_Knight = media.Movie("The Dark Knight",
                     "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                     "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

The_Pianist = media.Movie("The Pianist",
                     "A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto of World War II.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOWRiZDIxZjktMTA1NC00MDQ2LWEzMjUtMTliZmY3NjQ3ODJiXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,724,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=u_jE7-6Uv7E")

Slumdog_Millionaire = media.Movie("Slumdog Millionaire",
                     "A Mumbai teen reflects on his upbringing in the slums when he is accused of cheating on the Indian Version of Who Wants to be a Millionaire?",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BZmNjZWI3NzktYWI1Mi00OTAyLWJkNTYtMzUwYTFlZDA0Y2UwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=AIzbwV7on6Q")

Intouchables = media.Movie("Intouchables",
                     "After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxNDA3MDQwNl5BMl5BanBnXkFtZTcwNTU4Mzc1Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=34WIbmXkewU")

Hacksaw_Ridge = media.Movie("Hacksaw Ridge",
                     "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to receive the Medal of Honor without firing a shot.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1NjM3MTUxNV5BMl5BanBnXkFtZTgwMDc5MTY5OTE@._V1_SY1000_CR0,0,647,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=s2-1hz1juBI")


movies = [The_Prestige, A_Beautiful_Mind, Good_Will_Hunting, Inception, The_Dark_Knight, The_Pianist, Slumdog_Millionaire, Intouchables, Hacksaw_Ridge]
favourite_movies.open_movies_page(movies)

