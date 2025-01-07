# from flask import Flask, render_template, request, jsonify
# # from chatbot.qa_data import study_qa
# from chatbot.qa_data import study_qa

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     question = request.json.get('question', '').strip().lower()
    
#     if question == 'exit':
#         return jsonify({'answer': 'Goodbye! Keep exploring!'})
    
#     # Clean up the input: remove extra spaces and punctuation
#     question = ' '.join(question.split())  # Remove extra spaces
#     question = question.rstrip('?.')  # Remove trailing punctuation
    
#     # Find the answer
#     answer = study_qa.get(question, "I'm sorry, I don't know the answer to that question. Please try asking something else.")
    
#     return jsonify({'answer': answer})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# from chatbot.qa_data import study_qa

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     question = request.json.get('question', '').strip().lower()
    
#     if question == 'exit':
#         return jsonify({'answer': 'Goodbye! Keep exploring!'})
    
#     # Clean up the input: remove extra spaces and punctuation
#     question = ' '.join(question.split())  # Remove extra spaces
#     question = question.rstrip('?.')  # Remove trailing punctuation
    
#     # Find the answer
#     answer = study_qa.get(question, "I'm sorry, I don't know the answer to that question. Please try asking something else.")
    
#     return jsonify({'answer': answer})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
from chatbot.qa_data import study_qa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '').strip().lower()
    
    if question == 'exit':
        return jsonify({'answer': 'Goodbye! Keep exploring!'})
    
    # Clean up the input: remove extra spaces and punctuation
    question = ' '.join(question.split())  # Remove extra spaces
    question = question.rstrip('?.')  # Remove trailing punctuation
    
    # Find the answer
    answer = study_qa.get(question, "I'm sorry, I don't know the answer to that question. Please try asking something else.")
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)