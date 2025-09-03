from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("400x550")
app.title("Пошук чатів")

avatars_paths = {

}

avatars = {}


contacts = ["контакт№1", "контакт№2", "контакт№3", "контакт№4", "контакт№5", "контакт№6", "контакт№7", "контакт№8",]
7



search_var = StringVar()

def update_contacts(*args):
    for widget in contacts_frame.winfo_children():
        widget.destroy()
    query = search_var.get().lower()
    for name in contacts:
        if query in name.lower():
            create_contact_widget(name)

search_var.trace_add("write", update_contacts)


def create_contact_widget(name):
    contact = CTkFrame(contacts_frame, fg_color="transparent")
    contact.pack(fill="x", padx=10, pady=5)

    if name in avatars_paths:
        avatars[name] = CTkImage(Image.open(avatars_paths[name]), size=(40, 40))
        avatar_label = CTkLabel(contact, image=avatars[name], text="")
        avatar_label.pack(side="left", padx=5)
    else:

        pass


    name_label = CTkLabel(contact, text=name, font=("Arial", 16), anchor="w")
    name_label.pack(side="left", padx=10)

search_frame = CTkFrame(app, fg_color="transparent")
search_frame.pack(padx=20, pady=15, fill="x")

search_icon = CTkLabel(search_frame, text="🔍", font=("Arial", 16))
search_icon.pack(side="left", padx=(5, 0))

search_entry = CTkEntry(search_frame, placeholder_text="Search", textvariable=search_var)
search_entry.pack(side="left", fill="x", expand=True, padx=(5, 0))


contacts_frame = CTkFrame(app)
contacts_frame.pack(padx=20, pady=5, fill="both", expand=True)


for name in contacts:
    create_contact_widget(name)





app.mainloop()