# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from routes import routes_blueprint

app = Flask(__name__)

app.register_blueprint(routes_blueprint)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("starting server at [127.0.0.1:5000] ... ")
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
