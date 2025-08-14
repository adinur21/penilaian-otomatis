from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nilai", methods=["POST"])
def nilai():
    # Contoh input siswa
    data = request.form.get("hasil")
    
    # Contoh penilaian otomatis
    if data == "sukses":
        skor = 100
    else:
        skor = 0

    return f"Skor siswa: {skor}"

if __name__ == "__main__":
    app.run(debug=True)
