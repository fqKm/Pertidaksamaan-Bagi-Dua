from flask import Flask, render_template, request;
import sympy;
app = Flask(__name__);

@app.get("/")
def index():
    return render_template("bagidua.html", hasil = None)


@app.post("/")
def bagidua():
    hasil = None;
    fungsi_string = request.form['fungsi'];
    a = float(request.form['a'])
    b = float(request.form['b'])
    operator = request.form['operator']
    x = sympy.symbols('x');

    try:
        fungsi_extracted = sympy.sympify(fungsi_string);
        f = sympy.lambdify(x, fungsi_extracted, modules=['math']);

        if (f(a) * f(b)) >= 0:
            hasil = "Bisection tidak dapat digunakan, coba gunakan interval lain!"
        else :
            akar = hitung_bagidua(f, a, b)
            hasil = f"Akar f(x) {operator} 0 ditemukan di x = {akar:.6f}"
    except Exception as e :
        hasil = f"Terjadi error : {e}"
    return render_template("bagidua.html", hasil = hasil, fungsi=fungsi_string, a=a, b=b, operator=operator);

def hitung_bagidua(f,a,b, tol = 1e-6, max_iter=100):
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or abs(b - a) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c
if __name__ == "__main__":
    app.run(port=8000)