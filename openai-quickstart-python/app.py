import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        userInput = f"Marv is a chatbot that reluctantly answers questions with sarcastic " \
                    f"responses:{request.form['userInput']}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=userInput,
            temperature=0.91,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=1.0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
