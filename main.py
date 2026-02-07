import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Salir")
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Elige una opción: ")

        if option == "1":
            print("Crear tarea (pendiente)")
        elif option == "2":
            print("Listar tareas (pendiente)")
        elif option == "3":
            save_tasks(tasks)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
