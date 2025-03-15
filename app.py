from flask import Flask, render_template, request
import pickle
app=Flask(__name__)
model=pickle.load(open('saved_model.sav','rb'))

@app.route('/')
def home():
    result=''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    POSTED_BY=float(request.form['POSTED_BY'])
    UNDER_CONSTRUCTION=float(request.form['UNDER_CONSTRUCTION'])
    RERA=float(request.form['RERA'])
    BHK_NO=float(request.form['BHK_NO.'])
    BHK_OR_RK=float(request.form['BHK_OR_RK'])
    SQUARE_FT=float(request.form['SQUARE_FT'])
    READY_TO_MOVE=float(request.form['READY_TO_MOVE'])
    RESALE=float(request.form['RESALE'])
    result=model.predict([[POSTED_BY,UNDER_CONSTRUCTION,RERA,BHK_NO,BHK_OR_RK,SQUARE_FT,READY_TO_MOVE,RESALE]])
    return render_template('index.html',**locals())

if __name__=='__main__':
    app.run(debug=True)