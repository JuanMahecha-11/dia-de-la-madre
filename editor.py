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
<title>Para Mamá</title>

<style>

body{
    margin:0;
    overflow:hidden;
    font-family:Arial;
    background:linear-gradient(135deg,#ffe6e6,#ffd1dc);
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

/* CORAZON PUERTA */
.corazon{
    font-size:200px;
    cursor:pointer;
    transition:1s;
}

.abrir{
    transform:scale(3) rotateY(180deg);
    opacity:0;
}

/* TEXTO */
h1{
    color:black;
}

/* REGISTRO */
.box{
    background:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
}

/* EFECTOS */
.flor,.corazon-flotante{
    position:absolute;
    font-size:30px;
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
    font-size:30px;
    padding:20px;
}

.nombre-flotante{
    font-size:50px;
    animation:flotar 3s infinite;
}

@keyframes flotar{
    0%{transform:translateY(0);}
    50%{transform:translateY(-20px);}
    100%{transform:translateY(0);}
}

/* ESPACIO FOTOS */
.fotos img{
    width:120px;
    border-radius:15px;
    margin:10px;
}

</style>
</head>

<body>

<!-- PANTALLA 1 -->
<div class="pantalla" id="p1">
    <div class="corazon" onclick="abrir()">❤️</div>
    <h1>Haz clic en el corazón</h1>
</div>

<!-- PANTALLA 2 -->
<div class="pantalla oculto" id="p2">
    <div class="box">
        <h2>Escribe tu nombre</h2>
        <input id="nombre" type="text">
        <button onclick="entrar()">Entrar</button>
    </div>
</div>

<!-- PANTALLA 3 -->
<div class="pantalla oculto" id="p3">

    <div class="nombre-flotante" id="saludo"></div>

    <div class="final">
        Mamá eres el amor más bonito del mundo ❤️
        <br>
        Gracias por todo lo que haces por mí 🌸
    </div>

    <div class="fotos">
        <!-- AQUÍ PUEDES PONER FOTOS -->
        <img src="https://i.postimg.cc/13853d0B/image.png">
        <img src="https://i.postimg.cc/v1tS7c6n/image.png">
    </div>

</div>

<script>

function abrir(){
    document.querySelector("#p1 .corazon").classList.add("abrir");
    setTimeout(()=>{
        document.getElementById("p1").classList.add("oculto");
        document.getElementById("p2").classList.remove("oculto");
    },800);
}

function entrar(){

    let n = document.getElementById("nombre").value;

    if(n==""){
        alert("Escribe tu nombre");
        return;
    }

    document.getElementById("p2").classList.add("oculto");
    document.getElementById("p3").classList.remove("oculto");

    document.getElementById("saludo").innerHTML =
    "Feliz Día Mamá de " + n + " ❤️";

    crearEfectos();
}

function crearEfectos(){

    setInterval(()=>{

        let rosa = document.createElement("div");
        rosa.classList.add("flor");
        rosa.innerHTML = "🌹";
        rosa.style.left = Math.random()*100+"vw";
        document.body.appendChild(rosa);
        setTimeout(()=>rosa.remove(),6000);

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
