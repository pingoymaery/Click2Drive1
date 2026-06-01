from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/CARS')
def cars():
    cars_list = [
        {"img": "Fortuner.png", "name": "TOYOTA FORTUNER", "price": "₱1,775,000"},
        {"img": "Mitsubishi Montero Sport.png", "name": "MITSUBISHI MONTERO SPORT", "price": "₱1,568,000"},
        {"img": "Ford Everest.png", "name": "FORD EVEREST", "price": "₱1,864,000"},
        {"img": "BAIC B30e Dune.png", "name": "BAIC B30e DUNE", "price": "₱1,599,000"},
        {"img": "Jaecoo EJ6.png", "name": "JAECOO EJ6", "price": "₱1,649,000"},
        {"img": "Suzuki Jimny 5-Door.png", "name": "SUZUKI JIMMY 5-DOOR", "price": "₱6,100,000"},
        {"img": "VinFast VF.png", "name": "VinFast VF", "price": "₱590,000"},
        {"img": "JETOUR T2.png", "name": "JETOUR T2", "price": "₱2,498,000"},
        {"img": "GAC AION V.png", "name": "GAC AION V", "price": "₱1,498,000"},
        {"img": "KIA SORENTO.png", "name": "KIA SORENTO", "price": "₱2,188,000"},
    ]
    return render_template('cars.html', cars_list=cars_list)

if __name__=='__main__':
    app.run(debug='True')