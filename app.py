import tkinter
import customtkinter
from algos import run_maze
from PIL import ImageTk,Image

## application configuration
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("1240x840")
app.title('Path Finding In A MAZE (A Visual Illustration of Search Algorithms)')


def button_function():
    grid_size = tuple(map(int,dimension_entry.get().split(',')))
    initial_pos = tuple(map(int,initial_entry.get().split(','))) 
    goal_pos = tuple(map(int,goal_entry.get().split(',')))
    selected_algo = algo_radio.get()
    app.destroy()
    run_maze(grid_size,initial_pos,goal_pos,selected_algo)

    


img1=ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=640, height=720, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Path in a MAZE by search Algorithms",font=('Century Gothic',20))
l2.place(x=100, y=50)

l3=customtkinter.CTkLabel(master=frame, text="Give Initial Postition",font=('Century Gothic',18))
l3.place(x=50, y=195)
initial_entry=customtkinter.CTkEntry(master=frame, width=540,height=50, placeholder_text='Enter maze grid cell values, separated by commas',font=('Century Gothic',18))
initial_entry.place(x=50, y=230)

l4=customtkinter.CTkLabel(master=frame, text="Give Goal Postition",font=('Century Gothic',18))
l4.place(x=50, y=290)
goal_entry=customtkinter.CTkEntry(master=frame, width=540,height=50, placeholder_text='Enter maze grid cell values, separated by commas',font=('Century Gothic',18))
goal_entry.place(x=50, y=325)

l5=customtkinter.CTkLabel(master=frame, text="Give Maze Grid Dimensions",font=('Century Gothic',18))
l5.place(x=50, y=100)
dimension_entry=customtkinter.CTkEntry(master=frame, width=540,height=50, placeholder_text='Enter maze grid dimensions as row,col max (25,25)',font=('Century Gothic',18))
dimension_entry.place(x=50, y=135)

l6=customtkinter.CTkLabel(master=frame, text="Select Algorithm",font=('Century Gothic',18))
l6.place(x=50, y=385)
algo_radio = customtkinter.StringVar(value="DFS")
rad1 = customtkinter.CTkRadioButton(master=frame,text='DFS',value='DFS',font=('Century Gothic',18),variable=algo_radio)
rad1.place(x=50,y=425)
rad2 = customtkinter.CTkRadioButton(master=frame,text='BFS',value='BFS',font=('Century Gothic',18),variable=algo_radio)
rad2.place(x=50,y=455)
rad3 = customtkinter.CTkRadioButton(master=frame,text='A*',value='A*',font=('Century Gothic',18),variable=algo_radio)
rad3.place(x=50,y=485)
rad4 = customtkinter.CTkRadioButton(master=frame,text='Run All Algorithms and Make Comparison',value='comparison',font=('Century Gothic',18),variable=algo_radio)
rad4.place(x=50,y=515)
#Create custom button
submit_btn = customtkinter.CTkButton(master=frame, width=220,height=60, text="Submit Preferences", command=button_function, corner_radius=6,font=('Century Gothic',18))
submit_btn.place(x=190, y=550)



# You can easily integrate authentication system 

app.mainloop()