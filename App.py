from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET'])
def get_questions():
    with open('questions.json') as f:
        questions = json.load(f)
    return jsonify(questions)

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.json
    answers = data.get('answers', {})
    with open('questions.json') as f:
        questions = json.load(f)
    
    score = 0
    results = []
    for question in questions:
        qid = str(question['id'])
        given_answer = answers.get(qid, "")
        correct_answer = question['answer']
        if given_answer == correct_answer:
            score += 1
        results.append({
            "question": question['question'],
            "given_answer": given_answer,
            "correct_answer": correct_answer
        })

    return jsonify({'score': score, 'total': len(questions), 'results': results})

if __name__ == '__main__':
    app.run(debug=True)
