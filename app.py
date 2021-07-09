from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/enviar', methods=['POST'])
def enviar(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operacion = request.form['operacion']

        if operacion == 'suma':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)

        elif operacion == 'resta':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operacion == 'multiplicacion':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operacion == 'divicion':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')



if __name__ == ' __main__':
    app.debug = True
    app.run()
