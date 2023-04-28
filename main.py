from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def home():
    secret_key = os.environ.get('OPENAI_KEY')
    return f"Your OpenAI key is: {secret_key}"

if __name__ == '__main__':
    app.run()