from flask import Flask, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Password Generator</title>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script>
        function generatePassword() {
          var alphabets = document.getElementById("alphabets").value;
          var numbers = document.getElementById("numbers").value;
          var specials = document.getElementById("specials").value;
          
          var url = "/generate_password?alphabets=" + alphabets + "&numbers=" + numbers + "&specials=" + specials;
          
          $.ajax({
            url: url,
            type: "GET",
            success: function(response) {
              document.getElementById("password").textContent = response;
            }
          });
        }
      </script>
    </head>
    <body>
      <h1>Password Generator</h1>
      <label for="alphabets">Alphabets:</label>
      <input type="number" id="alphabets" min="0" value="6">
      <br><br>
      <label for="numbers">Numbers:</label>
      <input type="number" id="numbers" min="0" value="4">
      <br><br>
      <label for="specials">Special Characters:</label>
      <input type="number" id="specials" min="0" value="2">
      <br><br>
      <button onclick="generatePassword()">Generate Password</button>
      <br><br>
      <div id="password"></div>
    </body>
    </html>
    '''

@app.route('/generate_password')
def generate_password():
    alphabets = int(request.args.get('alphabets'))
    numbers = int(request.args.get('numbers'))
    specials = int(request.args.get('specials'))
    
    length = alphabets + numbers + specials
    
    charset = string.ascii_letters * alphabets + string.digits * numbers + string.punctuation * specials
    password = ''.join(random.sample(charset, length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
