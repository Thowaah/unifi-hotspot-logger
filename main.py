from flask import Flask, request

app = Flask(__name__)

@app.route("/webhookcallback", methods=["POST"])
def hook():
	with open("demofile.txt", "a") as f:
  		f.write("Now the file has more content!")
	print(request.data)
	return "Hello World"

if __name__ == "__main__":
	app.run()
