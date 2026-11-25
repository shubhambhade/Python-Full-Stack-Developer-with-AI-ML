class Movie:
    '''This class developed by shubham for oops concepts understanding'''

    def __init__(self,title, hero, heroin):
        self.title = title
        self.hero = hero
        self.heroin = heroin

    def movie_information(self):
        print("Movie name : ", self.title)
        print("Hero name : ", self.hero)
        print("Heroin name : ",self.heroin)

list_of_movies = []
while True :
    title = input("Enter movie name : ")
    hero = input("Enter hero name : ")
    heroin = input("Enter heroin name : ")
    m = Movie(title, hero,heroin)
    list_of_movies.append(m)
    print("movie added successfully....")
    option = input("do you want to add one more movie[yes/no] : ")

    if option.lower() == 'no':
        break

print("\nDisplay all movie information...")
for movie in list_of_movies:
    movie.movie_information()
    print()
