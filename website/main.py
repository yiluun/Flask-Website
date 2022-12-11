from website import create_app

# to add more html https://youtu.be/dam0GPOAvVI?t=1756

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # automatically reruns web server when code changes. turn off in production

