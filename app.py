from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') 

def index(): 
  """ 

 Renders the main index.html template for the Smart Register applicaƟ on.

 """ 

 return render_template('index.html') 

if __name__ == '__main__': 

 # Run the Flask applicaƟ on in debug mode for development

 app.run(debug=True) 
 
