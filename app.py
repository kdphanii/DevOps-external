from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def register():
    if request.method=="POST":
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        email=request.form.get("email")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm_password")
        return render_template("success.html")
    
    return render_template("register.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)