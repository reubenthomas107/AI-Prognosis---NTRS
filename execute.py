from flask import Flask, render_template, session, request, redirect, url_for,flash
from search import *
from get_pdf_details import *
from word_cloud import *
from Seq2Ser import *

app = Flask(__name__,template_folder='templates')
@app.route("/")
def search_index():
    return render_template("index.html")
    
@app.route("/search_pdf", methods=["POST", "GET"])
def search():
    q = request.form["search"]
    print(q)
    results = search_on_keyword(q)
    print(results)
    pdf_details = fetch_pdf_details(results)
    print(pdf_details["ids"])

    if request.method == 'POST':
        return render_template("embed.html", query=q, results=pdf_details["title"], 
        cats = pdf_details["cats"], ids = pdf_details["ids"])

@app.route("/pdf_details/<pdf_id>", methods=["POST", "GET"])
def after_search(pdf_id):
    pdf_details = fetch_pdf_details([pdf_id])
    generate_wordcloud(pdf_id)
    cleaned_data(pdf_id)
    return render_template("after_search.html", details = pdf_details)

@app.route("/embed")
def embed():
    return render_template("embed.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="127.0.0.1",port=5000)