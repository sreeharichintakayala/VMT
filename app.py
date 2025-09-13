import os
from flask import Flask, render_template, url_for
from flask import request,jsonify
app = Flask(__name__)

counter_file = "counter.txt"

def get_and_increment_counter():
    if not os.path.exists(counter_file):
        with open(counter_file,"w") as f:
            f.write("0")
    with open(counter_file, "r+") as f:
        count = int(f.read().strip() or "0")
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return count









@app.route('/')
def home():
    visits = get_and_increment_counter()
    return render_template('home.html',visits = visits)

@app.route('/pressreleases')
def press_releases():
    press_folder = os.path.join(app.static_folder, 'images', 'press')
    images = [f'images/press/{filename}' for filename in os.listdir(press_folder)
              if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('pressreleases.html', images=images)


@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/woman')
def woman():
    return render_template('woman.html')


@app.route('/feedback', methods = ['POST'])
def receive_feedback():
    data = request.get_json()

    if not data:
        return jsonify({"error" : "No JSON data provided"}),400
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not name or not email or not message:
        return jsonify({"error" : "Missing required fields"}),400
    
    print('Recieved Feedback : ', data)

    return jsonify({"message" : "Feedback received successfully"}), 200

@app.route('/personalitydevelopment')
def personalitydevelopment():
    return render_template('personality.html')
@app.route('/education')
def education():
    return render_template('education.html')




if __name__ == '__main__':
    app.run(debug=True)
