import time
import random

first_names = ["Zaine", "Omar", "Romulus", "Arlin", "Wright", "Davon", "Antone", "Sable", "Zen", "Larsa", "Arch",
               "Kellam", "Ayda", "Alder", "Jude", "Omen", "Eldon", "Morgan"]
last_names = ["Crowe", "Blackwood", "Digby", "Strain", "Shade", "Grimm", "Norwood", "Crane",
              "Nox", "Grove", "Jones", "Monroe", "Dred", "Barkridge", "Willow", "Wood"]


def read_request():
    with open("signal.txt", "r", encoding="utf-8") as infile:
        signal = infile.read()
    return signal


def write_name(signal):
    time.sleep(2)
    open("signal.txt", "w", encoding="utf-8").close()
    if signal == "0":
        index = random.randint(0, len(first_names) - 1)
        with open("name.txt", "w", encoding="utf-8") as outfile:
            outfile.write(first_names[index])
    elif signal == "1":
        f_index = random.randint(0, len(first_names) - 1)
        l_index = random.randint(0, len(last_names) - 1)
        name_string = first_names[f_index] + " " + last_names[l_index]
        with open("name.txt", "w", encoding="utf-8") as outfile:
            outfile.write(name_string)


def invalid_request():
    time.sleep(2)
    open("signal.txt", "w", encoding="utf-8").close()
    with open("name.txt", "w", encoding="utf-8") as outfile:
        outfile.write("Invalid request")


while True:
    request = read_request()
    if len(request) == 1 and (request == "0" or request == "1"):
        write_name(request)
    elif len(request) == 0:
        continue
    else:
        invalid_request()
