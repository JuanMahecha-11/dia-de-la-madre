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
<title>Para Mamá 💖</title>

<style>

body{
    margin:0;
    overflow:hidden;
    font-family:Arial;
    background: linear-gradient(135deg,#ffd1dc,#ffe6f0);
}

/* CAMBIO DE FONDO FINAL */
.fondoFinal{
    background: linear-gradient(-45deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
    background-size:400% 400%;
    animation:fondo 8s ease infinite;
}

@keyframes fondo{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* PANTALLAS */
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

.oculto{opacity:0;pointer-events:none;}

/* CORAZON */
.corazon{
    font-size:180px;
    cursor:pointer;
    animation:latido 1.5s infinite;
}

@keyframes latido{
    0%{transform:scale(1);}
    50%{transform:scale(1.2);}
    100%{transform:scale(1);}
}

/* INPUT */
input{
    padding:15px;
    border-radius:10px;
    border:none;
}

/* BOTON */
button{
    margin-top:10px;
    padding:10px 20px;
    border:none;
    border-radius:10px;
    background:#ff4d6d;
    color:white;
}

/* FLORES Y CORAZONES */
.flor,.corazon-flotante{
    position:absolute;
    font-size:25px;
    animation:caer 6s linear infinite;
}

@keyframes caer{
    from{transform:translateY(-10%);}
    to{transform:translateY(110vh);}
}

/* TEXTO FINAL */
.final{
    text-align:center;
    color:black;
    font-size:20px;
    background:rgba(255,255,255,0.7);
    padding:25px;
    border-radius:20px;
    width:80%;
}

/* NOMBRE */
.nombre{
    font-size:40px;
    color:white;
    text-shadow:0 0 10px black;
    animation:flotar 3s infinite;
}

@keyframes flotar{
    0%{transform:translateY(0);}
    50%{transform:translateY(-20px);}
    100%{transform:translateY(0);}
}

/* FOTOS */
img{
    width:120px;
    margin:10px;
    border-radius:10px;
}

</style>
</head>

<body>

<!-- PANTALLA 1 -->
<div class="pantalla" id="p1">
    <div class="corazon" onclick="abrir()">❤️</div>
    <h1>Haz clic en el corazón 💖</h1>
</div>

<!-- PANTALLA 2 -->
<div class="pantalla oculto" id="p2">
    <h2>Escribe tu nombre</h2>
    <input id="nombre">
    <button onclick="entrar()">Entrar</button>
</div>

<!-- PANTALLA 3 -->
<div class="pantalla oculto" id="p3">

    <div class="nombre" id="saludo"></div>

    <div class="final">
        Gracias mamá por ser el amor más bonito del mundo ❤️<br><br>

        Eres la persona que ilumina cada día con tu esfuerzo, tu cariño y tu fuerza.<br><br>

        Gracias por nunca rendirte, por cuidarme siempre y por darme todo sin pedir nada a cambio.<br><br>

        Eres mi ejemplo de vida, mi paz y mi alegría 🌸<br><br>

        Te amo con todo mi corazón 💖
    </div>

    <img src="https://i.imgur.com/8Km9tLL.jpg">
    <img src="https://i.imgur.com/2nCt3Sbl.jpg">

</div>

<script>

function abrir(){
    document.getElementById("p1").classList.add("oculto");
    document.getElementById("p2").classList.remove("oculto");
}

function entrar(){

    let n = document.getElementById("nombre").value;

    if(n==""){
        alert("Escribe tu nombre");
        return;
    }

    document.getElementById("p2").classList.add("oculto");
    document.getElementById("p3").classList.remove("oculto");

    // CAMBIO DE FONDO
    document.body.classList.add("fondoFinal");

    document.getElementById("saludo").innerHTML =
    "Feliz día Mamá de " + n + " 💖";

    efectos();
}

function efectos(){

    setInterval(()=>{

        let r = document.createElement("div");
        r.classList.add("flor");
        r.innerHTML = "🌹";
        r.style.left = Math.random()*100+"vw";
        document.body.appendChild(r);
        setTimeout(()=>r.remove(),6000);

    },300);

    setInterval(()=>{

        let c = document.createElement("div");
        c.classList.add("corazon-flotante");
        c.innerHTML = "❤️";
        c.style.left = Math.random()*100+"vw";
        document.body.appendChild(c);
        setTimeout(()=>c.remove(),6000);

    },500);
}

</script>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
