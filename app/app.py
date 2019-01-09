"""Treasure Hunt Flask App"""
from flask import Flask, render_template, flash, request

#TODO: QC it all

# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

questions = [
    'What are the notes on the four strings of a violin? '
    '(Don\'t use spaces in your answer)',

    'Add the number from Primrose\'s address to Alice\'s age. '
    'Add Ada\'s age to the result. Write the answer below.',

    'What is the result of multiplying the two fractions 3/5 (three fifths) '
    'and 1/2 (one half)? (You can answer with numbers, '
    'e.g., 1/3, or words, e.g., one third)',

    'What note comes right after G on a piano? (Hint: it may be a sharp or flat)',

    'What tribe is Moonwatcher a member of?',

    'In what state did your teacher, Mrs. Novak, go to college?',

    'What animals do Charles and Lizzie Peterson like most?',

    'What is a frog\'s favorite snack?'
]

answers = [
    ['EADG'],
    ['717'],
    ['3/10', 'THREE TENTHS'],
    ['G SHARP', 'A FLAT'],
    ['NIGHTWING', 'NIGHTWINGS'],
    ['FLORIDA'],
    ['PUPPIES'],
    ['FRUIT FLIES', 'FRENCH FLIES']
]

clues = [
    'Now you\'re making beautiful music together! It\'s time to get a '
    'little adventurous. The next clue is just off the beaten path in '
    'tick country (look to your left!). (Hint: getting this one will '
    'require something Ada has that Alice doesn\'t (yet)).',

    'Amazing! I bet you\'re wondering how much you have left? We\'re still '
    'in the first half. You\'re going to need a little artificial '
    'intelligence for this next clue. On the echo in the kitchen ask:\n'
    '1) Alexa, launch treasure hunt\n 2) Alexa, do you know about any clues?',

    'Wonderful! You\'re doing so well let\'s keep it going. The next clue is at ' 
    'http://localhost:5000/anotheroneforada',

    'And one more for our resident Wings of Fire expert: '
    'http://localhost:5000/awesomejobada',

    'Super job! Don\'t worry Alice, there will be some for just you '
    'before we\'re done. But for now, let\'s get moving again. This '
    'next clue is the farthest away so far. For this next one you\'ll '
    'have to take a trip to Squids for dinner. \n Just like some tasty fish, '
    'you\'ll catch the next clue while you\'re there.',

    'Great job! Let\'s keep going. The next clue is at'
    ' http://localhost:5000/aliceknowsherstuff ',

    'You sure do know your stuff, Alice! There\'s one more just for you at '
    'http://localhost:5000/rockonalice ',

    'Mmmm, tasty! I wonder if Alexa knows that joke? Speaking of Alexa, '
    'she\'ll be able to tell you where the next clue is. To get it say: \n'
    '1) Alexa, launch treasure hunt \n 2) Alexa, please tell me a frog clue.']


def event_handler(item_num, request_info):
    form = request_info.form

    question_text = questions[item_num]
    answer = answers[item_num]
    clue = clues[item_num]

    if request_info.method == 'POST':
        given_answer = request_info.form['question']

        if given_answer.upper() in answer:
            flash(clue, 'Correct')

        else:
            flash('Nope, try again. Did you maybe misspell something or overlook a step?', 'Error')

    return render_template('clue.html',
                           form=form,
                           question=question_text,
                           answer=answer,
                           clue=clue)


@app.route("/getaclue", methods=['GET', 'POST'])
def get_clue0():
    item_num = 0
    return event_handler(item_num, request)


@app.route("/canihaveanotherclue", methods=['GET', 'POST'])
def get_clue1():
    item_num = 1
    return event_handler(item_num, request)


@app.route("/yougoada", methods=['GET', 'POST'])
def get_clue2():
    item_num = 2
    return event_handler(item_num, request)


@app.route("/anotheroneforada", methods=['GET', 'POST'])
def get_clue3():
    item_num = 3
    return event_handler(item_num, request)


@app.route("/awesomejobada", methods=['GET', 'POST'])
def get_clue4():
    item_num = 4
    return event_handler(item_num, request)


@app.route("/aliceisthebomb", methods=['GET', 'POST'])
def get_clue5():
    item_num = 5
    return event_handler(item_num, request)


@app.route("/aliceknowsherstuff", methods=['GET', 'POST'])
def get_clue6():
    item_num = 6
    return event_handler(item_num, request)


@app.route("/rockonalice", methods=['GET', 'POST'])
def get_clue7():
    item_num = 7
    return event_handler(item_num, request)


if __name__ == "__main__":
    app.run()
