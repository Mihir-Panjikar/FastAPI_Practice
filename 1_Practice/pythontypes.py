def add(firstname: str, lastname: str):
    firstname = firstname.capitalize()
    return firstname + " " + lastname

fname = "Bill"
lname = "Gates"

name = add(fname, lname)
print(name)