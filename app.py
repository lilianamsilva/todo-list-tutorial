from flask import Flask, render_template
 
app: Flask = Flask(__name__)
 
@app.route('/create-todo')
def create_todo():
    return render_template("create-todo.html")
 
if __name__ == '__main__':
    app.run(debug=True)

