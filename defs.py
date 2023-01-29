import os
from main import *

### main window ###

def correct():
    if len(list_of_words) == 0:
        random_word["text"] = ""
        right_answer["bg"] = "white"
        right_answer["text"] = ""
        correct_wrong["text"] = "No words"
        correct_wrong["bg"] = "orange"
        user_guess_input["state"] = "normal"
        user_guess_input.delete(0, len(user_guess_input.get()))
        user_guess_input["state"] = "readonly"
    elif random_word["text"] == "":
        correct_wrong["text"] = ""
        correct_wrong["bg"] = "white"
        right_answer["text"] = ""
        right_answer["bg"] = "white"
        one_word = random.choice(list(list_of_words.keys()))
        random_word["text"] = one_word
        user_guess_input["state"] = "normal"
    else:
        if correct_wrong["text"] == "correct" or correct_wrong["text"] == "false":
            one_wordd = random.choice(list(list_of_words.keys()))
            random_word["text"] = one_wordd
            correct_wrong["text"] = ""
            correct_wrong["bg"] = "white"
            user_guess_input["state"] = "normal"
            user_guess_input.delete(0, len(user_guess_input.get()))
            right_answer["text"] = ""
            right_answer["bg"] = "white"


        else:
            if list_of_words[random_word["text"]].lower() == user_guess_input.get().lower():
                correct_wrong["text"] = "correct"
                correct_wrong["bg"] = "green"
                list_of_words.pop(random_word["text"])
                user_guess_input["state"] = "readonly"


            else:
                correct_wrong["text"] = "false"
                correct_wrong["bg"] = "red"
                right_answer["text"] = "Right answer: " + list_of_words[random_word["text"]]
                right_answer["bg"] = "green"
                user_guess_input["state"] = "readonly"

### NewWindow ###

    def add():
        if add_word_key.get() in list_of_words:
            add_label.pack()
            add_label["text"] = "This word already exists"
        elif len(add_word_key.get()) == 0 or len(add_word_value.get()) == 0:
            add_label.pack()
            add_label["text"] = "Enter key and value words"

        else:
            add_label.pack_forget()
            tree.insert("", END, values=(len(list_of_words)+1, add_word_key.get(), add_word_value.get()))
            invisable_label["text"] += 1
            list_of_words[add_word_key.get()]=add_word_value.get()
            add_word_key.delete(0, END)
            add_word_value.delete(0, END)
            add_word_key.focus()
            add_label.pack_forget()

    def delete_one_item():
        selected_item = tree.selection()[0]
        dyc = tree.item((selected_item))
        list_of_words.pop(dyc["values"][1])
        for item in tree.get_children():
            tree.delete(item)
        c=1
        for i in list_of_words:
            tree.insert("", END, values=(c, i, list_of_words[i]))
            c+=1

    def clear_list():
        for item in tree.get_children():
            tree.delete(item)
        list_of_words.clear()

    def save_list():

        with open(f"//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks//{stringvar.get()}.txt", "w") as file:
            list_of_words.clear()
            for line in tree.get_children():
                key = (tree.item(line)['values'][1])
                value = (tree.item(line)['values'][2])
                list_of_words[key] = value
            file.write(str(list_of_words))
            file.close()
            add_word_key.focus()



    def delete_list():
        os.remove(f"//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks//{stringvar.get()}.txt")
        update_listmenu()
        stringvar.set("Select list")
        clear_list()

    def new_empty_list():
        if name_of_list.get() == "":
            add_label["text"]= "Enter name of list"
        else:
            clear_list()
            with open(f"//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks//{name_of_list.get()}.txt", "w") as file:
                # listy.append(name_of_list.get())
                stringvar.set(name_of_list.get())
        update_listmenu()
        name_of_list.delete(0, END)

    def paf(event):
        clear_list()
        with open(f"//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks//{stringvar.get()}.txt", "r") as file:
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
                    list_of_words[hhh[0]] = hhh[1]
                    hhh.pop(0), hhh.pop(0)
                for i in list_of_words:
                    rrr = []
                    for item in tree.get_children():
                        rrr.append(item)
                    tree.insert("", END, values=(len(rrr) + 1, i, list_of_words[i]))

    def update_listmenu():
        files = os.listdir("//Users//vlastimilpevny//Desktop//test//venv//words_learning//tasks")
        files2 = []
        for i in files:
            k = i.replace(".txt", "")
            files2.append(k)
        if ".DS_Store" in files2:
            files2.remove(".DS_Store")
        stringvar_options["values"] = files2