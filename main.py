from flask import (Flask, render_template, request)

app = Flask(__name__)

def is_number_tryexcept(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def imc_img(resultado):
    index = 'index.html'

    if resultado>0 and resultado < 18.5:
        if resultado<1 :
            frase_madruga = "\"Quando a fome aperta, a vergonha afrouxa...\""
            resultado = "o peso abaixo do ideal! Seu imc é: " + str(resultado) + " ."
            imagem = '/static/assets/magro_mais.gif'                  
            return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
        else:
            frase_madruga = "\"Quando a fome aperta, a vergonha afrouxa...\""
            resultado = "o peso abaixo do ideal! Seu imc é: " + format(resultado, '.2f') + " ."
            imagem = '/static/assets/magro_mais.gif'                  
            return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
        
    elif resultado>= 18.5 and resultado<=24.9: 
        frase_madruga = "\"Sou pobre, porém honrado!\""
        resultado = "o peso ideal! Seu imc é: " + format(resultado, '.2f') + " ."
        imagem = '/static/assets/normal.gif'
        return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
    
    elif resultado > 24.9 and resultado<=600:
        frase_madruga = "\"Sou um homem de muita barriga senhor sorte.\""
        resultado = "o peso acima do ideal! Seu imc é: " + format(resultado, '.2f') + " ."
        imagem = '/static/assets/seu_barriga.gif'
        return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
    
    else:
        resultado = "Por favor, insira dígitos válidos."
        frase_madruga = "\"Eu sabia que você era idiota, mas não a nível executivo!\""
        imagem = '/static/assets/invalido.gif'
        return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
    

@app.route('/', methods=['GET', 'POST'] )
def index():
    frase_madruga= None
    imagem = None
    n1 = None
    n2 = None
    resultado =  None
    index = 'index.html'

    if request.method == 'POST':
        if is_number_tryexcept(request.form['altura_number'].replace(',','.',1)) and is_number_tryexcept(request.form['peso_number'].replace(',','.',1)): 
            n1 = float(request.form['altura_number'].replace(',','.',1))
            n2 = float(request.form['peso_number'].replace(',','.',1))

            if n1>0 and n2>0:  
                resultado = n2/(n1*n1)
                n = imc_img(resultado)          
                return n
            else:
                resultado = "Por favor, insira dígitos válidos."
                frase_madruga = "\"Eu sabia que você era idiota, mas não a nível executivo!\""
                imagem = '/static/assets/invalido.gif'
                
         else:
                resultado = "Por favor, insira dígitos válidos."
                frase_madruga = "\"Eu sabia que você era idiota, mas não a nível executivo!\""
                imagem = '/static/assets/invalido.gif'
                
    return render_template( index, frase_madruga = frase_madruga, resultado = resultado, imagem = imagem)
