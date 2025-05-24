from flask import Flask, request, render_template, url_for
from models.bot import Bot
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def chat():
    bot = Bot()
    questions = bot.get_all_questions()
    response = None
    image_url = None
    selected_question = None

    if request.method == 'POST':
        selected_question = request.form['question']
        response, image_name = bot.get_response(selected_question)
        if image_name:
            image_url = url_for('static', filename=f'images/{image_name}')

    return render_template(
        'chat.html',
        questions=questions,
        selected_question=selected_question,
        response=response,
        image_url=image_url
    )

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
