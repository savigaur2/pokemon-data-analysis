from flask import *
import Main

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    str_predictions = Main.Predictio_toString()
    Main.Write_to_HTML("p",str_predictions)
    return render_template('index.html')

app.run()
