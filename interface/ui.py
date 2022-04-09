from ctypes import alignment
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import webbrowser
# from matplotlib.font_manager import _Weight
import models

#GLOBALS -- probably can/should do this in a better way...
MOVIE_ID = [7396, 5756, 2640]  # important that it is from csv matrix
FILTERS = {
    'genre': ['Genre_No Filter', 'Genre_No Filter'],
    'before_year': 2022,
    'after_year': 1800,
    'less_runtime': 400,

}

def open_link(url):
    webbrowser.open_new(url);

class App(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Movie Recommendations!")
        # self.

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # ttk.Button(self, text="Quit", command=self.destroy).grid(column=1, row=0)

        self.frames = {}
        for F in (StartPage, Quiz, Results):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage" )

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        if page_name == 'Results': 
            self.frames[page_name].show_predictions()

        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Movie Recommendations!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        Button(self, text="Click here to take a quick quiz",\
                            command=lambda: controller.show_frame("Quiz")).pack()
        Button(self, text="Learn more about the project", command=lambda: \
            open_link("https://github.com/MichiganDataScienceTeam/movie-recommendations")).pack()

        # Button(self, text="Add Filter", command=lambda: controller.show_frame("Filter")).pack()

class Quiz(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Quiz", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.selections = []
        # QUESTION 1
        label_q1 =  Label(self, text='Pick Movies')
        label_q1.pack(side='top')

        list_q1 = {  # title: movie id (but really a dict...)
            'Saw': 7396,
            'Star Wars: Episode IV - A New Hope': 8001,
            'The Lion King': 5103,
            'The Notebook': 6188,
        }
        self.selections.append(StringVar())
        self.selections[0].set(sorted(list_q1.keys())[0])
        menu_q1 = OptionMenu(self, self.selections[0], *sorted(list_q1.keys()), command= lambda sel = self.selections[0]: self.update_movie(sel, 1, list_q1)) # 1, list_q1
        menu_q1.pack()
        # QUESTION 1


        # QUESTION 2 
        list_q2 = {
            'Moneyball': 5756,
            'Shawshank Redemption': 7593,
            'Ted': 8337,
            'The Dark Knight': 2163,
        }
        self.selections.append(StringVar())
        self.selections[1].set('Moneyball')
        menu_q2 = OptionMenu(self, self.selections[1], *sorted(list_q2.keys()), command=lambda sel = self.selections[1]: self.update_movie(sel, 2, list_q2))
        menu_q2.pack()
        # QUESTION 2

        # QUESTION 3
        list_q3 = {
            'Eagle Eye': 2640,
            'Elf': 2700,
            'Interstellar': 4396,
            'Richie Rich': 7127
        }
        self.selections.append(StringVar())
        self.selections[2].set('Eagle Eye')
        menu_q3 = OptionMenu(self, self.selections[2], *sorted(list_q3.keys()), command=lambda sel = self.selections[2]: self.update_movie(sel, 3, list_q3))
        menu_q3.pack()
        # QUESTION 3  




        # FILTERING
        label_filter =  Label(self, text='Filters:')
        label_filter.pack()

        # list_q2 = ['Brad Pitt', 'Tom Hanks', 'Jennifer Lawrence', 'Meryl  Streep', 'Robert Downey Jr.', 'Johnny Depp'] # actors/actresses will not be used


        Label(self, text="Genres: What you want / What you don't want").pack()
        # GENRE
        list_genres = [
            "No Filter",
            "Action",
            "Adventure",
            "Animation",
            "Children's",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Fantasy",
            "Film-Noir",
            "Horror",
            "Musical",
            "Mystery",
            "Romance",
            "Sci-Fi",
            "Thriller",
            "War",
            "Western"
        ]
        # GENRE WE WANT
        initial_genres = StringVar()
        initial_genres.set(list_genres[0])
        OptionMenu(self, initial_genres, *list_genres, command=lambda sel = initial_genres: self.update_genre(sel, 0)).pack()
        # GENRE WE DONT WANT
        initial_genres_1 = StringVar()
        initial_genres_1.set(list_genres[0])
        OptionMenu(self, initial_genres_1, *list_genres, command=lambda sel = initial_genres_1: self.update_genre(sel, 1)).pack()

        # INTENDED AUDIENCE
        list_audience = [
            ""
        ]


        # FILTERING



        Button(self, text="Get Results",command=lambda: self.controller.show_frame("Results")).pack() # back button

    def update_movie(self, selection, q_num, mapping): # 1-indexed
        global MOVIE_ID
        MOVIE_ID[q_num - 1] = mapping[selection]


    def update_genre(self, sel, loc):
        global FILTERS
        FILTERS['genre'][loc] = f'Genre_{sel}';
        



class Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Recommendations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.knn = models.KNN_COLLAB('no pkl', 'no_csv')
        self.matrixfact = models.MatrixFactorizationModel('./data/torchsvd.pt')

        Button(self, text="Another?",command= self.update).pack() # back button


    def show_predictions(self):
        #### show KNN results
        list_knn = self.knn.recommend(MOVIE_ID, FILTERS)
        list_matrix_fact = self.matrixfact.recommend(MOVIE_ID, FILTERS)

        Label(self, text="KNN Predictions").pack()
        initial_q1  = StringVar()
        initial_q1.set(list_knn[0])
        self.menu_knn = OptionMenu(self, initial_q1, *list_knn)
        self.menu_knn.pack()

        Label(self, text="Matrix Factorization Predictions").pack()
        initial_q2  = StringVar()
        initial_q2.set(list_matrix_fact[0])
        self.menu_matixfact = OptionMenu(self, initial_q2, *list_matrix_fact)
        self.menu_matixfact.pack()


    def update(self):
        self.menu_knn.pack_forget()
        self.menu_matixfact.pack_forget()
        self.controller.show_frame("Quiz")



'''
- quiz giving (two) movies
    - pick a movie
    - from cast
    - genres
- loading model capabilities
- side-by-side comparisons

- textbox for actors?
- filtering capabilities (next week)
    - year
    - popularity?
'''





if __name__ == '__main__':
    # main()
    app = App()
    app.mainloop()
