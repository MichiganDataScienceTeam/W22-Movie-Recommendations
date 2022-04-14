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


        self.title_font = tkfont.Font(family='MS Serif', size=18, weight="bold", slant="italic")
        self.title("Movie Recommendations!")
        window_width = 1000
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        # self.iconbitmap('icons/MDST_logo.ico') # icon change code
        self.iconphoto(TRUE, tk.PhotoImage(file='./icons/MDST-logo.png'))
        # self.PhotoImage(file = 'icons/MDST-logo')
        # self.
        # Read the Image
        image = Image.open("./icons/MDST-logo.png")
 
        # Resize the image using resize() method
        resize_image = image.resize((175, 52))
        img = ImageTk.PhotoImage(resize_image)
 
        # create label and add resize image
        label1 = Label(image=img)
        label1.image = img
        label1.pack(side=BOTTOM, anchor=SE)


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
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.controller = controller
        label = Label(self, text="Welcome To Our Movie Recommender!", font=controller.title_font)
        label.grid(row=0, column=1)
        
        Button(self, text="Click here to take a quick quiz",\
                            command=lambda: controller.show_frame("Quiz"),height= 2, width=20).grid(row=1, column=1)
        Button(self, text="Learn more about the project", command=lambda: \
            open_link("https://github.com/MichiganDataScienceTeam/movie-recommendations")).grid(row=2, column=1)
        # Button(self, text="Add Filter", command=lambda: controller.show_frame("Filter")).pack()

class Quiz(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.controller = controller
        label = Label(self, text="Quiz", font=controller.title_font)
        label.grid(row=0, column=2)

        self.selections = []
        # QUESTION 1
        label_q1 =  Label(self, text='Pick Movies')
        label_q1.grid(row=1, column=1)

        list_q1 = {  # title: movie id (but really a dict...)
            'Saw': 7396,
            'Star Wars: Episode IV - A New Hope': 8001,
            'The Lion King': 5103,
            'The Notebook': 6188,
        }
        self.selections.append(StringVar())
        self.selections[0].set(sorted(list_q1.keys())[0])
        menu_q1 = OptionMenu(self, self.selections[0], *sorted(list_q1.keys()), command= lambda sel = self.selections[0]: self.update_movie(sel, 1, list_q1)) # 1, list_q1
        menu_q1.grid(row=2, column=1)
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
        menu_q2.grid(row=2, column=2)
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
        menu_q3.grid(row=2, column=3)
        # QUESTION 3  




        # FILTERING
        label_filter =  Label(self, text='Filters:')
        label_filter.grid(row=3, column=1)

        # list_q2 = ['Brad Pitt', 'Tom Hanks', 'Jennifer Lawrence', 'Meryl  Streep', 'Robert Downey Jr.', 'Johnny Depp'] # actors/actresses will not be used


        Label(self, text="Genres: What you want / What you don't want").grid(row=4, column=1)
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
        OptionMenu(self, initial_genres, *list_genres, command=lambda sel = initial_genres: self.update_genre(sel, 0)).grid(row=5, column=1)
        # GENRE WE DONT WANT
        initial_genres_1 = StringVar()
        initial_genres_1.set(list_genres[0])
        OptionMenu(self, initial_genres_1, *list_genres, command=lambda sel = initial_genres_1: self.update_genre(sel, 1)).grid(row=5, column=2)

        # INTENDED AUDIENCE
        list_audience = [
            ""
        ]
        # FILTERING


        # Read the Image
        image1 = Image.open("./icons/starwars.png")
 
        # Resize the image using resize() method
        resize_image1 = image1.resize((312, 234))
        meme_img1 = ImageTk.PhotoImage(resize_image1)
 
        # create label and add resize image
        meme_label1 = Label(self, image=meme_img1)
        meme_label1.image = meme_img1
        meme_label1.grid(row=2, column=0)
        Button(self, text="Get Results",command=lambda: self.controller.show_frame("Results")).grid(row=7, column=1) # back button
        Button(self, text="Back to Menu",command=lambda: self.controller.show_frame("StartPage")).grid(row=10, column=0, sticky='w')

        image1 = Image.open("./icons/infinity_war.png")
        resize_image1 = image1.resize((312, 234))
        meme_img1 = ImageTk.PhotoImage(resize_image1)
        meme_label2 = Label(self, image=meme_img1)
        meme_label2.image = meme_img1
        meme_label2.grid(row=6, column=0)



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
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(10, weight=1)
        label = Label(self, text="Recommendations", font=controller.title_font)
        label.grid(row=0, column=1)
        # Read the Image
        image = Image.open("./icons/Gladiator.png")
 
        # Resize the image using resize() method
        resize_image = image.resize((312, 234))
        meme_img = ImageTk.PhotoImage(resize_image)
 
        # create label and add resize image
        meme_label = Label(self, image=meme_img)
        meme_label.image = meme_img
        meme_label.grid(row=3, column=1)

        self.knn = models.KNN_COLLAB('no pkl', 'no_csv')
        self.matrixfact = models.MatrixFactorizationModel('./data/torchsvd.pt')

        Button(self, text="Another?",command= self.update).grid(row=5, column=1) # back button


    def show_predictions(self):
        #### show KNN results
        list_knn = self.knn.recommend(MOVIE_ID, FILTERS)
        list_matrix_fact = self.matrixfact.recommend(MOVIE_ID, FILTERS)

        Label(self, text="KNN Predictions").grid(row=1, column=1)
        initial_q1  = StringVar()
        initial_q1.set(list_knn[0]) 
        self.menu_knn = OptionMenu(self, initial_q1, *list_knn)
        self.menu_knn.grid(row=2, column=1)

        Label(self, text="Matrix Factorization Predictions").grid(row=1, column=2)
        initial_q2  = StringVar()
        initial_q2.set(list_matrix_fact[0])
        self.menu_matrixfact = OptionMenu(self, initial_q2, *list_matrix_fact)
        self.menu_matrixfact.grid(row=2, column=2)


    def update(self):
        self.menu_knn.grid_forget()
        self.menu_matrixfact.grid_forget()
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
