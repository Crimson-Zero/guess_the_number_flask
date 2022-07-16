from flask import Flask
import random

app = Flask(__name__)


random_number  = random.randint(0,9)

@app.route("/")
def welcome():
    return '<h1 style="text-align:center";"color:cyan">Guess the number between 0 and 9!</h2>'\
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def guess_the_number(number):
    
   
    
    if(number < random_number):
        
         return '<h1 style="text-align:center";"color:red">Too Low Try Again</h1>'\
            '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    
    if(number > random_number):
        
         return '<h1 style="text-align:center";"color:blue">Too High Try Again</h1>'\
            '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
            
    
        
    if(number == random_number):
        
         return '<h1 style="text-align:center";"color:green">Congratulations you found me</h1>'\
            '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    
            
if __name__ == '__main__':
    app.run(debug=True)
