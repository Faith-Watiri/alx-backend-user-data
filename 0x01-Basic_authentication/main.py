from api.v1.app import app

def run():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run()
