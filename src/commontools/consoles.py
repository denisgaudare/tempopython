import os


def pause(msg="➡️ Appuie sur Entrée pour continuer..."):
    input(msg)

def clear_terminal():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)
