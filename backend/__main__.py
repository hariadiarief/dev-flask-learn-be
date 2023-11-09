from backend import create_app

app = create_app()
 
if __name__ == "__main__":
    # accept req from local, change 0.0.0.0 to accept from everywhere
    app.run(host="127.0.0.1")
