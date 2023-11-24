from flask import Flask , render_template,url_for , redirect,request
import numpy
import pickle
# from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
# csrf = CSRFProtect(app)
# @app.after_request
# def apply_caching(response):
#     response.headers["X-Frame-Options"] = "SAMEORIGIN"
#     response.headers["HTTP-HEADER"] = "VALUE"
#     return response



app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)
#We can set secure cookies in response
# response.set_cookie('key', 'value', secure=True, httponly=True, samesite='Lax')






model = pickle.load(open("RFRmodel.pkl","rb"))


@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/home/" , methods = ["GET","POST"])
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():
    if request.method == "GET":
        return render_template("index.html")
    else:
        final_features = []
        
        
        makes = ['Subaru', 'LADA', 'Dodge', 'Kia', 'Alfa Romeo', 'Acura', 'Lexus',
                    'Mitsubishi', 'Citroen', 'Mini', 'Jaguar', 'Porsche', 'Fiat',
                    'Ford', 'Renault', 'Seat', 'Rover', 'Volkswagen', 'Jeep',
                    'Cadillac', 'Audi', 'Toyota', 'Volvo', 'Chevrolet', 'Lincoln',
                    'Hyundai', 'Nissan', 'Suzuki', 'BMW', 'Mazda', 'Land Rover',
                    'Skoda', 'Honda', 'Mercedes-Benz', 'Chrysler']
        f1 = request.form["carBrands"]
        final_features.append(makes.index(f1))
        
        
        transmission_types = ['automatic', 'mechanical']
        transmission_types.sort()
        f2 = str(request.form["transmission_type"])
        print(f2,type(f2) , transmission_types)
        final_features.append(transmission_types.index(f2))
        
        
        colors = ['silver', 'blue', 'red', 'black', 'brown',
                'white']
        colors.sort()
        f3 = request.form["color"]
        final_features.append(colors.index(f3))
        
        
        f4 = int(request.form["mileage"])
        final_features.append(f4)
        
        
        f5 = int(request.form["year"])
        final_features.append(f5)
        
        
        f6 = request.form["engine_type"]
        if f6 == "gasoline":
            final_features.append(2)
        else:
            final_features.append(0)
            
        
        f7 = request.form["engine_capacity"]
        final_features.append(f7)
        
        types = ['universal', 'suv', 'sedan', 'hatchback', 'liftback', 'minivan',
                'minibus', 'van', 'pickup', 'coupe', 'cabriolet', 'limousine']
        types.sort()
        f8 = request.form["body_type"]
        final_features.append(types.index(f8))
        
        
        l = ["True","False"]
        l.sort()
        f9 = request.form["has_warranty"]
        final_features.append(l.index(f9))
        
        
        l2 = ['all', 'front', 'rear']
        l2.sort()
        f10 = request.form["drivetrain"]
        final_features.append(l2.index(f10))
        
        
        prediction = model.predict([final_features])
        output = round(prediction[0],2)    
        return render_template('index.html',prediction_text="{}".format(output))
        
        





@app.route("/whatandwhy/" , methods = ["GET","POST"])
def whatandwhy():
    return render_template("whatandwhy.html")


@app.route("/stats/" , methods = ["GET","POST"])
def stats():
    return render_template("stats.html")


@app.route("/tables/" , methods = ["GET","POST"])
def tables():
    return render_template("tables.html")


@app.route("/all_algos_used/" , methods = ["GET","POST"])
def all_algos_used():
    return render_template("all_algos_used.html")


@app.route("/about/" , methods = ["GET","POST"])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)