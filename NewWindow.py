from tkinter import ttk
from tkinter import *
import tkinter
from main import list_of_words
from defs import add, delete_one_item, clear_list, save_list, delete_list, new_empty_list, paf, update_listmenu
def new_list():

    window_add_list = Toplevel()
    window_add_list.minsize(width=500, height=500)
    window_add_list.title("Lists of words")

    invisable_label = tkinter.Label(window_add_list)
    invisable_label["text"] = 0

    frame_three = Frame(window_add_list)
    frame_three.pack()

    frame_six = Frame(window_add_list)
    frame_six.pack()

    frame_one = Frame(window_add_list)
    frame_one.pack()

    frame_two = Frame(window_add_list)
    frame_two.pack()

    frame_four = Frame(window_add_list)
    frame_four.pack()

    frame_five = Frame(window_add_list)
    frame_five.pack()

    title_add_list = tkinter.Label(frame_three, text="Load / Create list of words", font=("Ink Free", 24, "bold"))
    title_add_list.grid(row=0, column=1)

    select_label = tkinter.Label(frame_six, text="Select list:", font= ("Ink free", 18), pady=20, padx=10)
    select_label.grid(row=0, column=1)

    stringvar = tkinter.StringVar(frame_six)
    stringvar.set("Select list")
    stringvar_options = ttk.Combobox(frame_six, textvariable = stringvar, state="readonly")
    stringvar_options.grid(row=0, column=2)

    update_listmenu()


    new_list_button = tkinter.Button(frame_six, text= "Create list", command=new_empty_list)
    new_list_button.grid(row=0, column=4)

    name_of_list = tkinter.Entry(frame_six, justify=CENTER, width=10)
    name_of_list.grid(row=0, column=3)


    add_word_key = tkinter.Entry(frame_one, justify=CENTER)
    add_word_key.grid(row=1, column=0)

    add_word_value = tkinter.Entry(frame_one, justify=CENTER)
    add_word_value.grid(row=1, column=2)

    add_button = tkinter.Button(frame_one, text="Add word in list", command=add)
    add_button.grid(row=1, column=3)

    scrollbar = tkinter.Scrollbar(frame_two, width=20)
    scrollbar.pack(side = RIGHT, fill=Y)

    tree = ttk.Treeview(frame_two, columns = ('id','Key-word', 'Answer'), height = 10, show='headings', yscrollcommand=scrollbar.set)
    tree.heading('id', text='Id')
    tree.heading('Key-word', text='Key-word')
    tree.heading('Answer', text='Answer')
    tree.pack(side = LEFT)
    scrollbar.config(command=tree.yview)

    try:
        with open("//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks//list1.txt", "r") as file:
            for i in file:
                u = i.replace("{", "")
                o = u.replace("}", "")
                j = o.replace("'", "")
                l = j.replace(":", ",")
                h = l.split(", ")
            if h == [""]:
                pass
            else:
                while len(h) != 0:
                    list_of_words[h[0]] = h[1]
                    h.pop(0), h.pop(0)
                for i in list_of_words:
                    rrr = []
                    for item in tree.get_children():
                        rrr.append(item)
                    tree.insert("", END, values=(len(rrr) + 1, i, list_of_words[i]))
    except FileNotFoundError:
        pass


    clear_list_button = tkinter.Button(frame_four, text="Clear list", command=clear_list)
    clear_list_button.grid(row=0, column=0)

    delete_button = tkinter.Button(frame_four, text="Delete word", command=delete_one_item)
    delete_button.grid(row=0, column=2)

    delete_button = tkinter.Button(frame_four, text="Delete list", command=delete_list)
    delete_button.grid(row=0, column=4)

    save_button = tkinter.Button(frame_four, text="Save list", command=save_list)
    save_button.grid(row=0, column=5)

    ok_button = tkinter.Button(frame_four, text="Start", command=window_add_list.destroy)
    ok_button.grid(row=0, column=6)

    add_label = tkinter.Label(frame_five, text= "", bg="red", font=("Ink Free", 18, "bold"))
    add_label.pack_forget()

    window_add_list.bind('<<ComboboxSelected>>', paf)
    window_add_list.bind('<Return>', lambda event: add())
