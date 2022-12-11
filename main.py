from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # automatically reruns web server when code changes. turn off in production

