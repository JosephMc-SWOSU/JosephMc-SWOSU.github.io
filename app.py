from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

def get_needed_letters(old_message: str, new_message: str):
    old_message = old_message.replace(" ", "").lower()
    new_message = new_message.replace(" ", "").lower()
    
    # Count the occurrences of each letter in both messages
    old_counter = Counter(old_message)
    new_counter = Counter(new_message)
    
    # Determine the needed letters
    needed_letters = {}
    for letter, count in new_counter.items():
        if count > old_counter.get(letter, 0):
            needed_letters[letter] = count - old_counter.get(letter, 0)
    
    return needed_letters

@app.route('/', methods=['GET', 'POST'])
def index():
    needed_letters = None
    if request.method == 'POST':
        old_message = request.form['old_message']
        new_message = request.form['new_message']
        needed_letters = get_needed_letters(old_message, new_message)
    return render_template('index.html', needed_letters=needed_letters)

@app.route('/projects/signage-helper', methods=['GET', 'POST'])
def signage_helper():
    needed_letters = None
    if request.method == 'POST':
        old_message = request.form['old_message']
        new_message = request.form['new_message']
        needed_letters = get_needed_letters(old_message, new_message)
    return render_template('signage_helper.html', needed_letters=needed_letters)

if __name__ == '__main__':
    app.run(debug=True)