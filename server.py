from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    print('the root was requested')
    name = 'Harry'
    response = model(x)
    return json.dumps({
        'statusCode': 200,
        'response': 'hello string'
    })

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    x = request.get_json()
    img = x['input']
    x = img_str
    print(x)
    return 'hello' 

if __name__ == '__main__':
    app.run(host='35.178.210.245', port=5000)#host='0.0.0.0', port=5000)
#0.0.0.0:5000/