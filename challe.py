from flask import Flask, request, jsonify
import spacy
spacy.load('es_core_news_sm')

# Inicializar Flask
app = Flask(__name__)

# Cargar el modelo de Spacy para español
nlp = spacy.load("es_core_news_sm")

# Ruta para procesar las oraciones y obtener las entidades nombradas
@app.route('/ner', methods=['POST'])
def named_entity_recognition():
    try:
        # Obtener la lista de oraciones en formato JSON desde la solicitud POST
        data = request.get_json()
        sentences = data.get('sentences', [])

        # Procesar cada oración y obtener las entidades nombradas
        result = []
        for sentence in sentences:
            doc = nlp(sentence)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            result.append(entities)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
