import sqlite3
import create.py
import argparse

def add_task(database.db, task, status):
conn = sqlite3.connect(database.db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, status))
        conn.commit()
def remove_task(database.db, task_id):
  conn = sqlite3.connect(database.db)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
def modify_task(db_name, task_id, new_task):
   conn = sqlite3.connect(database.db)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
        conn.commit()
def modify_task_status(db_name, task_id, new_status):
  conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
def print_help():
    """Prints the help message explaining the task manager options."""
    print("\nTask Manager Help")
    print("Choose one of the following options:")
    print("1. Add Task: Add a new task with a description and status.")
    print("2. Remove Task: Remove an existing task by its ID.")
    print("3. Modify Task: Update the description of an existing task.")
    print("4. Modify Task Status: Update the status of an existing task.")
    print("5. Exit: Exit the task manager application.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager Application")
    parser.add_argument("-d", "--database", default="database.db", help="Specify the database file to use.")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message and exit.")
    args = parser.parse_args()

    if args.help:
        print_help()
        return

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Modify Task")
        print("4. Modify Task Status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            status = input("Enter task status: ")
            add_task(db_name, task, status)
        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(db_name, task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to modify: "))
            new_task = input("Enter new task description: ")
            modify_task(db_name, task_id, new_task)
        elif choice == "4":
            task_id = int(input("Enter task ID to modify status: "))
            new_status = input("Enter new task status: ")
            modify_task_status(db_name, task_id, new_status)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
