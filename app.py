from flask import Flask, render_template, request
from similarity import get_similarity
app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('landing_page.html')

# Main route for prediction
@app.route('/', methods=['POST'])
def predict():
    doc1 = request.form['text1'].lower()
    doc2 = request.form['text2'].lower()
    score = get_similarity(doc1,doc2)

    return render_template('landing_page.html', score=score)  # Default upload web page to show before the POST request

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True, threaded=True)