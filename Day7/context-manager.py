from contextlib import contextmanager
import mysql.connector

# 1. Class based Context Manager

class FileHandler:

    def __init__(self, filename, mode):

        self.filename = filename
        self.mode = mode
        self.file = None


    def __enter__(self):

        print("Opening file")

        self.file = open(
            self.filename,
            self.mode
        )

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("Closing file")

        if self.file:
            self.file.close()


        if exc_type:
            print(f"Error handled: {exc_val}")


        return True


# 2. Generator based Context Manager

@contextmanager
def db_connection():

    conn = None

    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "S@ndy_1704",
        )
        print("Database connection opened")

        yield conn
    
    except Exception as e:

        print("Database error: ", e)

        yield None

    finally:

        if conn:
            conn.close()
        print("Connection closed")

print("FILE HANDLER TEST")

with FileHandler("sample.txt", "w") as file:
#     handler = FileHandler(
#     "sample.txt",
#     "w"
# )


# file = handler.__enter__()
    file.write("Hello Python Context Manager")


print("File operation completed")



# Testing exception handling

print("\nEXCEPTION TEST")


with FileHandler("sample.txt", "r") as file:

    print(file.read())

    # creating error intentionally
    x = 10 / 0

print("Program continued")


# Testing database context manager

print("\nDATABASE TEST")


with db_connection() as conn:

    cursor = conn.cursor()

    cursor.execute("Show databases;")
    
    databases = cursor.fetchall()
    
    print("\n Databases available:")

    for db in databases:
        print(db[0])

print("Database block finished")