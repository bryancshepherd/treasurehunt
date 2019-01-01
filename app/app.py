from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

questions = [
    "What are the notes on the four strings of a violin? (Don't use spaces in your answer)"
]

answers = [
    "EADE"

]

clues = [
    "Awesome! To find the next clue, look in the coldest place in the house."

]


@app.route("/clue1", methods=['GET', 'POST'])
def clue():
    form = ReusableForm(request.form)

    item_num = 0
    print(item_num)
    question_text = questions[item_num]
    answer = answers[item_num]
    clue = clues[item_num]

    print(form.errors)
    if request.method == 'POST':
        given_answer = request.form['question']
        print(given_answer)

        if answer == given_answer:
            # Save the comment here.
            flash(clue, 'Correct')

        else:
            flash('All the form fields are required. ', 'Error')

    return render_template('clue.html',
                           form=form,
                           question=question_text,
                           answer=answer,
                           clue=clue)

if __name__ == "__main__":
    app.run()
