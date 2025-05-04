from flask import Flask, render_template, send_file
import csv
import os

app = Flask(__name__)

def load_dataset_from_csv():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "dataset_stats.csv")
    dataset = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dataset.append(row)
    return dataset

@app.route('/')
def index():
    dataset = load_dataset_from_csv()
    return render_template('index.html', dataset=dataset)

@app.route('/download_csv')
def download_csv():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "dataset_stats.csv")
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
