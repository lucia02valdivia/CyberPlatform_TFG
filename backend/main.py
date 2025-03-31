from app.init import create_app, db

app = create_app()

@app.route("/")
def home():
    return "¡La API está funcionando correctamente!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

