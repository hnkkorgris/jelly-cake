from flask import Flask, url_for, request, make_response, jsonify
from models import Screen
from controller import NeoProvider

app = Flask(__name__)
app.config.update(SEND_FILE_MAX_AGE_DEFAULT=0) # Prevent caching on dev machine
db = NeoProvider()

@app.route('/')
@app.route('/index')
def load_page():	
	
	return make_response(open('templates/index.html').read())

@app.route('/currentScreen')
def get_screen():
	return jsonify(screen = current_screen.serialize())
	
	# next_screen = db.get_next_screen(current_screen.ans1)

current_screen = db.get_start_screen()
	
if __name__ == '__main__':
	app.debug = True
	app.run()