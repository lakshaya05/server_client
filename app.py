from flask import Flask, render_template, request, jsonify
app = Flask(_name_, template_folder='templates')
# Server messages storage
server_messages = []
23
@app.route('/')
def client():
 return render_template('index.html')
@app.route('/server')
def server():
 return render_template('server.html', server_messages=server_messages)
@app.route('/send_message', methods=['POST'])
def send_message():
 data = request.get_json()
 client_message = data.get('message')
 # Store the client message in the server_messages list
 server_messages.append(f'Client: {client_message}')
 # Get the server response from the server's input box
 server_response = request.form.get('server_response', '')
 # Store the server response in server_messages list
 server_messages.append(f'Server: {server_response}')
 return jsonify({'status': 'Message received successfully!', 'response': server_response})
@app.route('/get_messages', methods=['GET'])
def get_messages():
 return jsonify(server_messages)
if _name_ == '_main_':
 app.run(debug=True)
