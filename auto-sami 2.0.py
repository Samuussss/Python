import subprocess
import time

def git_add_commit_push(commit_message):
    try:
        subprocess.run(['git', 'add', '.'])

        subprocess.run(['git', 'commit', '-m', commit_message])

        subprocess.run(['git', 'push'])

        print("Subida exitosa al repositorio de GitHub.")
    except Exception as e:
        print("Ocurrió un error durante la subida al repositorio:")
        print(e)

print("--------------------")
print(" ")
commit_msg = input("Ingrese un mensaje para el commit: ")

git_add_commit_push(commit_msg)

print(" ")
print("--------------------")
time.sleep(15)