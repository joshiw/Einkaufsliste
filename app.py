from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from prettytable import PrettyTable
import cowsay 
app = Flask(__name__)
bootstrap=Bootstrap(app)
@app.route('/')
def index():
    Einkaufsliste = PrettyTable(["Produkt","Menge","Gekauft"])
    Einkaufsliste.add_row(["Äpfel","4"," "])
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
my_apple =r''' 
,--./,-.
 / #      \
|          |
 \        /    hjw
  `._,._,'
'''
cowsay.draw(my_apple)
