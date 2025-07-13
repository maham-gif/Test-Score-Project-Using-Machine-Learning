from flask import Flask, redirect, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

filename = "Test_Score_LR_v2.pkl"
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Data')
def data():
    return render_template('Data.html')

@app.route('/Results')
def results():
    return render_template('Results.html')

@app.route('/Model')
def model():
    return render_template('Model.html')

@app.route('/Research')
def research():
    return render_template('Research.html')

@app.route('/Predict', methods=['GET', 'POST'])
def predict():

    
    if request.method == 'GET':
        return(render_template('Predict.html', pass_='none', fail_='none', inds=[0,0,1,0,0,0,0,0]))

    if request.method == 'POST':
       
        X = []
        indices = []
        ints = []
        vals = []

        print(indices)

        vals = [x for x in request.form.values()]
        print(vals)
        
        ints = [int(x) for x in vals]
        X = [1]
        X.extend(ints[:5])
        
        if ints[5] == 0:
            mj = [1, 0, 0, 0, 0]
          
        elif ints[5] == 1:
            mj = [0, 1, 0, 0, 0]

        elif ints[5] == 4:
           mj = [0, 0, 1, 0, 0]

        elif ints[5] == 2:
            mj = [0, 0, 0, 1, 0]

        elif ints[5] == 3:
            mj = [0, 0, 0, 0, 1]

        X.extend(mj)

        if ints[6] == 0:
            fj = [1, 0, 0, 0, 0]
          
        elif ints[6] == 1:
            fj = [0, 1, 0, 0, 0]

        elif ints[6] == 4:
           fj = [0, 0, 1, 0, 0]

        elif ints[6] == 2:
            fj = [0, 0, 0, 1, 0]

        elif ints[6] == 3:
            fj = [0, 0, 0, 0, 1]

        X.extend(fj)
        
        if ints[7] == 1:
            r = [1, 0, 0, 0]

        elif ints[7] == 0:
            r = [0, 1, 0, 0]

        elif ints[7] == 3:
            r = [0, 0, 1, 0]

        elif ints[7] == 2:
            r = [0, 0, 0, 1]

        X.extend(r)

        print(X)
        pred = model.predict((np.asarray(X)).reshape(1, -1))

        if pred == 1:
            prediction = ['flex', 'none']
        else:
            prediction = ['none', 'flex']

        print(indices)

        indices = [1 if ints[0] == 0 else 0]
        indices.extend(ints[1:4])
        higher = [1 if ints[4] == 0 else 0]
        indices.extend(higher)
        indices.extend(ints[5:])
        

        print(indices)


        return (render_template('Predict.html', pass_= prediction[0], fail_= prediction[1], inds=indices))


if __name__ == '__main__':
    app.run()

