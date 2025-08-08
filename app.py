from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['hours_per_week']),
        float(request.form['num_assignments']),
        float(request.form['discussion_posts']),
        float(request.form['video_watched']),
        float(request.form['logins'])
    ]
    data = np.array([features])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    result = "likely to complete" if prediction >= 0.5 else "not likely to complete"
    return render_template('index.html', prediction_text=f'The student is {result} the course.')

if __name__ == '__main__':
    app.run(debug=True)