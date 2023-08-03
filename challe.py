
from flask import Flask, request, jsonify, render_template
import spacy
nlp = spacy.load("es_core_news_sm")


# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def Home():
    return render_template("index1")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    
    sentences = request.form.values()
    sentences_list = [s.strip() for s in ''.join(sentences).split('\n')]
    result = {}
    for idx, sentence in enumerate(sentences_list):
        doc = nlp(sentence)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        result[idx] = entities

    return render_template("index1", prediction_text = "The flower species is {}".format(result))

if __name__ == "__main__":
    flask_app.run(debug=True)
