from flask import Flask, render_template, make_response, jsonify, request


app = Flask(__name__)

@app.route('/')
def html():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def get_value():
    req_data = request.get_json(force=True)
    print(req_data)
    if 'value' not in req_data:
        return make_response('', 400)
    data = req_data['value']
    x = int(data)
    y = x**2
    return make_response(jsonify({'result': y}), 200)

if __name__ == '__main__':
    app.run()