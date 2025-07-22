from flask import Flask, render_template, request, jsonify
import random, difflib

app = Flask(__name__)

qa_pairs = {
    "What is the estimated cost for a construction project?":
      'The cost varies based on project size, design, and materials. Please share your project details and we will provide an accurate estimate. '
      '<a href="#book-form" class="link">You can book a ticket here</a>',
    "Where is your office located?":
      "Our head office is located in Calicut, Kerala.",
    "In which locations are your ongoing projects?":
      "We currently have ongoing projects across Kerala, Tamil Nadu, and Karnataka.",
    "Do you offer site visits before project planning?":
      "Yes, we offer free site visits to better understand your project requirements. Please book an appointment to schedule a visit.",
    "Can I request a project consultation?":
      "Absolutely! Please use the appointment section to book a consultation. Our experts will contact you to discuss further.",
    "What types of construction services do you offer?":
      "We provide residential, commercial, renovation, interior design, and turnkey construction services."
}

@app.route('/')  
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message'].strip().lower()
    match = difflib.get_close_matches(msg, [q.lower() for q in qa_pairs], n=1, cutoff=0.6)
    if match:
        orig = next(q for q in qa_pairs if q.lower() == match[0])
        return jsonify({'reply': qa_pairs[orig]})
    return jsonify({'reply': "Sorry, I didn't get that. Please choose from the suggestions."})

@app.route('/random-questions')
def random_questions():
    return jsonify({'questions': random.sample(list(qa_pairs), 3)})

if __name__ == '__main__':
    app.run(debug=True)
