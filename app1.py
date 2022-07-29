import os
import numpy as np #used for numerical analysis
from flask import Flask,request,render_template# Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.
#render_template- used for rendering the html pages
from tensorflow.keras.models import load_model#to load our trained model
from tensorflow.keras.preprocessing import image


app=Flask(__name__)#our flask app
model=load_model('food.h5')#loading the model

@app.route("/") #default route
def upload_file():
    return render_template("RR.html")#rendering html page

@app.route("/about") #route about page
def upoad_file1():
    return render_template("RR.html")#rendering html page
    

@app.route("/upload") # route for info page 
def upload_file2():
    return render_template("RRP.html")#rendering html page

#@app.route("/upload") # route for uploads
#def test():
    #return render_template("index.html")#rendering html page

@app.route("/predict",methods=["GET","POST"]) #route for our prediction
def upload():
    if request.method=='POST':
        f=request.files['file'] #requesting the file
        basepath=os.path.dirname('__file__')#storing the file directory
        filepath=os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
        f.save(filepath)#saving the file
        
        img=image.load_img(filepath,target_size=(64,64)) #load and reshaping the image
        x=image.img_to_array(img)#converting image to array
        x=np.expand_dims(x,axis=0)#changing the dimensions of the image

        pred = model.predict(x)  # predicting classes
        print(pred)  # printing the prediction
        index = ['French Fries', 'Pizza', 'Samosa']
        result = str(index[pred.argmax()])
        print(result)
        if (result=="French Fries"):
            return render_template("0.html",showcase =  str(result))
        elif (result=="Pizza"):
            return render_template("1.html",showcase =  str(result))
        else:
            return render_template("2.html",showcase =  str(result))
        #return result#resturing the result
    else:
        return None

#port = int(os.getenv("PORT"))
if __name__=="__main__":
    app.run(debug=False)#running our app
    #app.run(host='0.0.0.0', port=8000,debug=True)
            
            