from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Mamá ❤️</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            overflow:hidden;
            font-family:'Segoe UI', sans-serif;
            background:linear-gradient(135deg,#ff9a9e,#fad0c4,#ffd1ff);
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            position:relative;
        }

        .pantalla{
            position:absolute;
            width:100%;
            height:100%;
            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction:column;
            transition:1s;
        }

        .oculto{
            opacity:0;
            pointer-events:none;
            transform:scale(0.9);
        }

        .corazon{
            font-size:180px;
            cursor:pointer;
            animation:latido 1s infinite;
            transition:0.5s;
            filter:drop-shadow(0 0 20px rgba(255,0,90,0.5));
        }

        .corazon:hover{
            transform:scale(1.1);
        }

        @keyframes latido{
            0%{transform:scale(1);}
            50%{transform:scale(1.15);}
            100%{transform:scale(1);}
        }

        h1{
            color:white;
            margin-top:20px;
            font-size:55px;
            text-shadow:0 5px 10px rgba(0,0,0,0.2);
        }

        .registro-box{
            background:rgba(255,255,255,0.25);
            backdrop-filter:blur(12px);
            padding:50px;
            border-radius:35px;
            text-align:center;
            box-shadow:0 10px 40px rgba(0,0,0,0.2);
            width:450px;
        }

        .registro-box h2{
            color:white;
            margin-bottom:25px;
            font-size:40px;
        }

        input{
            width:100%;
            padding:18px;
            border:none;
            border-radius:20px;
            font-size:20px;
            outline:none;
            margin-bottom:20px;
        }

        button{
            background:#ff4f81;
            color:white;
            border:none;
            padding:18px 35px;
            border-radius:20px;
            font-size:20px;
            cursor:pointer;
            transition:0.3s;
        }

        button:hover{
            transform:scale(1.05);
            background:#ff2f6d;
        }

        .final{
            text-align:center;
            padding:40px;
            position:relative;
            z-index:2;
        }

        .titulo-final{
            color:white;
            font-size:65px;
            margin-bottom:25px;
            text-shadow:0 5px 10px rgba(0,0,0,0.3);
            animation:brillo 2s infinite;
        }

        @keyframes brillo{
            0%{opacity:1;}
            50%{opacity:0.7;}
            100%{opacity:1;}
        }

        .mensaje{
            color:white;
            font-size:28px;
            width:80%;
            margin:auto;
            line-height:1.8;
            background:rgba(255,255,255,0.18);
            padding:30px;
            border-radius:30px;
            backdrop-filter:blur(10px);
            box-shadow:0 10px 30px rgba(0,0,0,0.2);
        }

        .flor{
            position:absolute;
            font-size:45px;
            animation:flotar linear infinite;
            opacity:0.8;
        }

        @keyframes flotar{
            from{
                transform:translateY(110vh) rotate(0deg);
            }

            to{
                transform:translateY(-120vh) rotate(360deg);
            }
        }

        .sol{
            position:absolute;
            width:500px;
            height:500px;
            border-radius:50%;
            animation:girar 25s linear infinite;
            z-index:1;
        }

        @keyframes girar{
            from{
                transform:rotate(0deg);
            }

            to{
                transform:rotate(360deg);
            }
        }

        .sol span{
            position:absolute;
            font-size:50px;
        }

        .s1{top:0; left:50%;}
        .s2{top:15%; right:10%;}
        .s3{top:50%; right:0;}
        .s4{bottom:15%; right:10%;}
        .s5{bottom:0; left:50%;}
        .s6{bottom:15%; left:10%;}
        .s7{top:50%; left:0;}
        .s8{top:15%; left:10%;}

        .frase{
            position:absolute;
            color:white;
            font-size:24px;
            font-weight:bold;
            animation:aparecer 6s infinite;
            opacity:0;
            text-shadow:0 4px 10px rgba(0,0,0,0.3);
        }

        @keyframes aparecer{
            0%{opacity:0; transform:translateY(20px);}
            20%{opacity:1; transform:translateY(0px);}
            80%{opacity:1;}
            100%{opacity:0; transform:translateY(-20px);}
        }

        .f1{top:10%; left:10%; animation-delay:0s;}
        .f2{top:20%; right:8%; animation-delay:2s;}
        .f3{bottom:15%; left:12%; animation-delay:4s;}
        .f4{bottom:10%; right:10%; animation-delay:6s;}

        .brillo-corazon{
            position:absolute;
            width:250px;
            height:250px;
            background:rgba(255,255,255,0.2);
            border-radius:50%;
            filter:blur(40px);
            animation:pulse 2s infinite;
        }

        @keyframes pulse{
            0%{transform:scale(1); opacity:0.7;}
            50%{transform:scale(1.3); opacity:0.3;}
            100%{transform:scale(1); opacity:0.7;}
        }

    </style>
</head>

<body>

    <!-- PANTALLA 1 -->
    <div class="pantalla" id="pantalla1">

        <div class="brillo-corazon"></div>

        <div class="corazon" onclick="abrirRegistro()">❤️</div>

        <h1>Tócame Mamá</h1>

    </div>

    <!-- PANTALLA 2 -->
    <div class="pantalla oculto" id="pantalla2">

        <div class="registro-box">

            <h2>🌸 Bienvenida 🌸</h2>

            <input type="text" id="nombre" placeholder="Escribe tu nombre">

            <button onclick="entrar()">Entrar ❤️</button>

        </div>

    </div>

    <!-- PANTALLA 3 -->
    <div class="pantalla oculto" id="pantalla3">

        <div class="sol">
            <span class="s1">🌸</span>
            <span class="s2">🌹</span>
            <span class="s3">💖</span>
            <span class="s4">🌷</span>
            <span class="s5">❤️</span>
            <span class="s6">🌺</span>
            <span class="s7">✨</span>
            <span class="s8">🌼</span>
        </div>

        <div class="frase f1">Eres mi lugar seguro ❤️</div>
        <div class="frase f2">Gracias por nunca rendirte 🌸</div>
        <div class="frase f3">Tu amor ilumina mi vida ✨</div>
        <div class="frase f4">La mejor mamá del mundo 🌷</div>

        <div class="final">

            <h1 class="titulo-final" id="saludo"></h1>

            <div class="mensaje">
                Gracias por cada sacrificio, cada abrazo y cada consejo.
                <br><br>
                A veces el tiempo pasa tan rápido que olvidamos decir lo importante:
                eres una mujer increíble.
                <br><br>
                Gracias por estar incluso cuando nadie más estuvo.
                Gracias por enseñarme a seguir adelante.
                <br><br>
                Hoy no quería darte solo un regalo.
                Quería darte un pequeño universo hecho especialmente para ti ❤️
                <br><br>
                Te amo muchísimo mamá 🌸
            </div>

        </div>

    </div>

    <script>

        function abrirRegistro(){

            document.getElementById('pantalla1').classList.add('oculto');

            setTimeout(() => {
                document.getElementById('pantalla2').classList.remove('oculto');
            }, 500);
        }

        function entrar(){

            let nombre = document.getElementById('nombre').value;

            if(nombre.trim() === ''){
                alert('Escribe tu nombre 🌸');
                return;
            }

            document.getElementById('pantalla2').classList.add('oculto');

            setTimeout(() => {

                document.getElementById('pantalla3').classList.remove('oculto');

                document.getElementById('saludo').innerHTML =
                'Feliz Día ' + nombre + ' ❤️';

                crearFlores();

            }, 500);
        }

        function crearFlores(){

            let emojis = ['🌸','🌷','🌹','💖','✨','🌺'];

            setInterval(() => {

                let flor = document.createElement('div');

                flor.classList.add('flor');

                flor.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];

                flor.style.left = Math.random() * 100 + 'vw';

                flor.style.animationDuration =
                (Math.random() * 5 + 5) + 's';

                document.body.appendChild(flor);

                setTimeout(() => {
                    flor.remove();
                }, 10000);

            }, 300);
        }

    </script>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
