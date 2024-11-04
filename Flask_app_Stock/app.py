from flask import *
import pickle
import numpy as np

app = Flask(__name__)

# Load all models at the start to save load time
models = {
    "apple": pickle.load(open("Models/Apple_ensemble_model.pkl", "rb")),
    "amazon": pickle.load(open("Models/Amazon_ensemble_model.pkl", "rb")),
    "google": pickle.load(open("Models/Google_ensemble_model.pkl", "rb")),
    "meta": pickle.load(open("Models/META_ensemble_model.pkl", "rb")),
    "microsoft": pickle.load(open("Models/MSFT_ensemble_model.pkl", "rb")),
    "netflix": pickle.load(open("Models/Netflix_ensemble_model.pkl", "rb")),
    "nvidia": pickle.load(open("Models/Nvidia_ensemble_model.pkl", "rb")),
    "tcs": pickle.load(open("Models/TCS_ensemble_model.pkl", "rb"))
}

@app.route('/')
def index():
    return render_template('index.html')

# Route for each company page
@app.route('/<company>', methods=['GET', 'POST'])
def company_page(company):
    if company not in models:
        return "Model not found", 404

    if request.method == 'POST':
        try:
            # Get form data
            open_price = float(request.form['open'])
            high_price = float(request.form['high'])
            low_price = float(request.form['low'])
            volume = float(request.form['volume'])

            # Prepare input for model
            input_data = np.array([[open_price, high_price, low_price, volume]])

            # Get the corresponding model
            model = models[company]

            # Predict the close value
            close_value = model.predict(input_data)[0]

            return render_template(f'{company}.html', close_value=close_value, open=open_price, high=high_price, low=low_price, volume=volume)

        except Exception as e:
            return f"Error: {e}", 500

    return render_template(f'{company}.html')

if __name__ == '__main__':
    app.run(debug=True)
