from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Membuat rute utama yang akan merender file HTML
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Menjalankan server lokal
    print("Menjalankan jam vintage... Buka http://127.0.0.1:5000 di browsermu.")
    app.run(debug=True)
