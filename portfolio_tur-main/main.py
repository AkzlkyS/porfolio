# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['GET', 'POST'])
def process_form():
    # Butonların durumlarını al
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')


    email = request.form.get('email')
    text = request.form.get('text')
    with open("text.txt", "a", encoding="utf-8") as file:
        file.write(f"{email}")
        file.write(f"{text}")
        file.write("-------------------------")


    # Template'e durumları aktar
    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )


if __name__ == "__main__":
    app.run(debug=True)
