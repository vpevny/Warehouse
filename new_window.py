from tkinter import *
from tkinter import ttk
import os
import main

### Defs ###

def new_list():

    ######## Defs ########

    files = os.listdir("//Users//vlastimilpevny//Desktop//WordsLearning//")
    files2 = []
    for i in files:
        k = i.replace(".txt", "")
        files2.append(k)
    if "lists" not in files:
        os.mkdir(os.path.join("//Users//vlastimilpevny//Desktop//WordsLearning", "lists"))
    def add():
        if add_word_key.get() in main.list_of_words:
            add_label.pack()
            add_label["text"] = "This word already exists"
            add_word_key.config(highlightthickness=1)
        elif len(add_word_key.get()) == 0 or len(add_word_value.get()) == 0:
            add_label.pack()
            add_word_value.config(highlightthickness=1)
            add_word_key.config(highlightthickness=1)
            add_label["text"] = "Enter key and value words"

        else:
            add_label.pack_forget()
            tree.insert("", END, values=(len(main.list_of_words) + 1, add_word_key.get(), add_word_value.get()))
            invisable_label["text"] += 1
            main.list_of_words[add_word_key.get()] = add_word_value.get()
            add_word_key.delete(0, END)
            add_word_value.delete(0, END)
            add_word_key.focus()
            add_label.pack_forget()
            add_word_value.config(highlightthickness=0)
            add_word_key.config(highlightthickness=0)


    def delete_one_item():
        selected_item = tree.selection()[0]
        dyc = tree.item((selected_item))
        main.list_of_words.pop(dyc["values"][1])
        for item in tree.get_children():
            tree.delete(item)
        c = 1
        for i in main.list_of_words:
            tree.insert("", END, values=(c, i, main.list_of_words[i]))
            c += 1

    def clear_list():
        for item in tree.get_children():
            tree.delete(item)
        main.list_of_words.clear()

    def save_list():
        with open(f"//Users//vlastimilpevny//Desktop//WordsLearning//lists//{stringvar.get()}.txt",
                  "w") as file:
            main.list_of_words.clear()
            for line in tree.get_children():
                key = (tree.item(line)['values'][1])
                value = (tree.item(line)['values'][2])
                main.list_of_words[key] = value
            file.write(str(main.list_of_words))
            file.close()
            add_word_key.focus()



    def delete_list():
        os.remove(f"//Users//vlastimilpevny//Desktop//WordsLearning//lists//{stringvar.get()}.txt")
        update_listmenu()
        stringvar.set("Select list")
        clear_list()

    def new_empty_list():
        if name_of_list.get() == "":
            add_label.pack()
            add_label["text"] = "Enter name of list"
            name_of_list.config(highlightthickness=1)
        else:
            add_label.pack_forget()
            name_of_list.config(highlightthickness=0)
            clear_list()
            with open(f"//Users//vlastimilpevny//Desktop//WordsLearning//lists//{name_of_list.get()}.txt",
                      "w") as file:
                # listy.append(name_of_list.get())
                stringvar.set(name_of_list.get())
        update_listmenu()
        name_of_list.delete(0, END)

    def loadingtree(event):
        clear_list()
        with open(f"//Users//vlastimilpevny//Desktop//WordsLearning//lists//{stringvar.get()}.txt",
                  "r") as file:
            hhh = []
            for i in file:
                u = i.replace("{", "")
                o = u.replace("}", "")
                j = o.replace("'", "")
                l = j.replace(":", ",")
                b = l.split(", ")
                for i in b:
                    hhh.append(i)
            if len(hhh) == 0 or hhh[0] == "":
                clear_list()
            else:
                while len(hhh) != 0:
                    main.list_of_words[hhh[0]] = hhh[1]
                    hhh.pop(0), hhh.pop(0)
                for i in main.list_of_words:
                    rrr = []
                    for item in tree.get_children():
                        rrr.append(item)
                    tree.insert("", END, values=(len(rrr) + 1, i, main.list_of_words[i]))

    def update_listmenu():
        files = os.listdir("//Users//vlastimilpevny//Desktop//WordsLearning//lists")
        files2 = []
        for i in files:
            k = i.replace(".txt", "")
            files2.append(k)
        if ".DS_Store" in files2:
            files2.remove(".DS_Store")
        stringvar_options["values"] = files2

    ######## Window ########

    window_add_list = Toplevel()
    window_add_list.minsize(width=500, height=500)
    window_add_list.title("Lists of words")

    invisable_label = Label(window_add_list)
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

    title_add_list = Label(frame_three, text="Load / Create list of words", font=("Ink Free", 24, "bold"))
    title_add_list.grid(row=0, column=1)

    select_label = Label(frame_six, text="Select list:", font= ("Ink free", 18), pady=20, padx=10)
    select_label.grid(row=0, column=1)

    stringvar = StringVar(frame_six)
    stringvar.set("Select list")
    stringvar_options = ttk.Combobox(frame_six, textvariable = stringvar, state="readonly")
    stringvar_options.grid(row=0, column=2)

    update_listmenu()


    new_list_button = Button(frame_six, text= "Create list", command=new_empty_list)
    new_list_button.grid(row=0, column=4)

    name_of_list = Entry(frame_six, justify=CENTER, width=10, highlightthickness=0, highlightcolor="red", highlightbackground="red")
    name_of_list.grid(row=0, column=3)


    add_word_key = Entry(frame_one, justify=CENTER, highlightthickness=0, highlightcolor="red", highlightbackground="red")
    add_word_key.grid(row=1, column=0)

    add_word_value = Entry(frame_one, justify=CENTER, highlightthickness=0, highlightcolor="red", highlightbackground="red")
    add_word_value.grid(row=1, column=2)

    add_button = Button(frame_one, text="Add word in list", command=add)
    add_button.grid(row=1, column=3)

    scrollbar = Scrollbar(frame_two, width=20)
    scrollbar.pack(side = RIGHT, fill=Y)

    tree = ttk.Treeview(frame_two, columns = ('id','Key-word', 'Answer'), height = 10, show='headings', yscrollcommand=scrollbar.set)
    tree.heading('id', text='Id')
    tree.heading('Key-word', text='Key-word')
    tree.heading('Answer', text='Answer')
    tree.pack(side = LEFT)
    scrollbar.config(command=tree.yview)

    try:
        with open("//Users//vlastimilpevny//Desktop//WordsLearning//lists//list1.txt", "r") as file:
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
                    main.list_of_words[h[0]] = h[1]
                    h.pop(0), h.pop(0)
                for i in main.list_of_words:
                    rrr = []
                    for item in tree.get_children():
                        rrr.append(item)
                    tree.insert("", END, values=(len(rrr) + 1, i, main.list_of_words[i]))
    except FileNotFoundError:
        pass


    clear_list_button = Button(frame_four, text="Clear list", command=clear_list)
    clear_list_button.grid(row=0, column=0)

    delete_button = Button(frame_four, text="Delete word", command=delete_one_item)
    delete_button.grid(row=0, column=2)

    delete_button = Button(frame_four, text="Delete list", command=delete_list)
    delete_button.grid(row=0, column=4)

    save_button = Button(frame_four, text="Save list", command=save_list)
    save_button.grid(row=0, column=5)

    ok_button = Button(frame_four, text="Start", command=window_add_list.destroy)
    ok_button.grid(row=0, column=6)

    add_label = Label(frame_five, text= "", bg="red", font=("Ink Free", 18, "bold"))
    add_label.pack_forget()

    window_add_list.bind('<<ComboboxSelected>>', loadingtree)
    window_add_list.bind('<Return>', lambda event: add())
