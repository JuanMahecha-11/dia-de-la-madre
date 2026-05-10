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
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

<style>

*{box-sizing:border-box;margin:0;padding:0;}

body{
    overflow:hidden;
    font-family:'Nunito',sans-serif;
    background: #ffe4ef;
    min-height:100vh;
    width:100%;
}

.fondoBase{
    background: linear-gradient(160deg, #ffd6e8 0%, #ffb3cd 40%, #ffc2d9 70%, #ffe0ec 100%);
    background-size: 300% 300%;
    animation: rosado 10s ease infinite;
}

.fondoFinal{
    background: linear-gradient(-45deg, #ff9ab8, #ffc2d9, #fbd0e0, #ff7fab, #ffa0c0) !important;
    background-size:400% 400% !important;
    animation: fondo 8s ease infinite !important;
}

@keyframes rosado{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

@keyframes fondo{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.particula{
    position:fixed;
    font-size:22px;
    pointer-events:none;
    z-index:0;
    animation: caer linear infinite;
    opacity:0.85;
}

@keyframes caer{
    0%  { transform: translateY(-60px) rotate(0deg);   opacity:0; }
    10% { opacity:0.9; }
    90% { opacity:0.8; }
    100%{ transform: translateY(110vh)  rotate(360deg); opacity:0; }
}

.pantalla{
    position:fixed;
    inset:0;
    width:100%;
    height:100%;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    transition: opacity 0.9s ease;
    z-index: 10;
}

.oculto{opacity:0;pointer-events:none;}

#p1 h1{
    font-family:'Dancing Script',cursive;
    font-size: clamp(22px,5vw,38px);
    color:#c0396a;
    text-shadow: 0 2px 12px rgba(255,100,150,0.4);
    margin-top:16px;
    text-align:center;
    padding:0 20px;
    animation: flotar 3s ease-in-out infinite;
}

.corazon-btn{
    font-size: clamp(120px,25vw,200px);
    cursor:pointer;
    animation: latido 1.4s ease-in-out infinite;
    filter: drop-shadow(0 0 18px rgba(255,80,120,0.6));
    user-select:none;
    transition: filter 0.2s;
}
.corazon-btn:hover{
    filter: drop-shadow(0 0 30px rgba(255,80,120,0.9));
}

@keyframes latido{
    0%,100%{transform:scale(1);}
    14%{transform:scale(1.22);}
    28%{transform:scale(1);}
    42%{transform:scale(1.14);}
    70%{transform:scale(1);}
}

#p2 .caja{
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 40px 36px;
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:14px;
    box-shadow: 0 8px 40px rgba(255,100,150,0.25);
    width: min(360px, 90vw);
}

#p2 h2{
    font-family:'Dancing Script',cursive;
    font-size:30px;
    color:#c0396a;
}

#p2 p{
    font-size:14px;
    color:#a05070;
    text-align:center;
}

input{
    width:100%;
    padding:14px 18px;
    border-radius:14px;
    border: 2px solid #ffb3cc;
    font-size:16px;
    font-family:'Nunito',sans-serif;
    outline:none;
    background:rgba(255,255,255,0.9);
    color:#8b2252;
    transition: border 0.2s, box-shadow 0.2s;
}
input:focus{
    border-color: #ff6b9d;
    box-shadow: 0 0 0 3px rgba(255,107,157,0.2);
}

button{
    width:100%;
    padding:14px;
    border:none;
    border-radius:14px;
    background: linear-gradient(135deg,#ff6b9d,#ff4d6d);
    color:white;
    font-size:17px;
    font-family:'Dancing Script',cursive;
    font-weight:700;
    cursor:pointer;
    box-shadow: 0 4px 18px rgba(255,77,109,0.4);
    transition: transform 0.15s, box-shadow 0.15s;
}
button:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(255,77,109,0.5);}
button:active{transform:translateY(0);}

#p3{
    overflow-y:auto;
    padding:20px 0 40px;
    align-items:center;
    justify-content:flex-start;
    padding-top: 30px;
}

.nombre-grande{
    font-family:'Dancing Script',cursive;
    font-size: clamp(28px,7vw,52px);
    color:#fff;
    text-shadow: 0 2px 20px rgba(180,0,80,0.5), 0 0 40px rgba(255,120,160,0.4);
    animation: flotar 3s ease-in-out infinite;
    text-align:center;
    padding:0 20px;
    margin-bottom:20px;
}

@keyframes flotar{
    0%,100%{transform:translateY(0);}
    50%{transform:translateY(-16px);}
}

.carta{
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    padding: 30px 28px;
    width: min(600px, 92vw);
    text-align:center;
    box-shadow: 0 8px 50px rgba(255,80,130,0.25);
    color: #7a2248;
    font-size: clamp(14px,2.2vw,17px);
    line-height:1.9;
}

.carta .titulo-carta{
    font-family:'Dancing Script',cursive;
    font-size: clamp(22px,4vw,32px);
    color:#d63068;
    margin-bottom:18px;
}

.carta p{
    margin-bottom:14px;
}

.carta .firma{
    font-family:'Dancing Script',cursive;
    font-size:22px;
    color:#ff4d7e;
    margin-top:18px;
}

/* ── TARJETAS ANIMADAS (reemplazan los GIFs) ── */
.gifs{
    display:flex;
    justify-content:center;
    align-items:stretch;
    gap:20px;
    flex-wrap:wrap;
    margin-top:24px;
    width: min(600px,92vw);
}

.gif-frame{
    background:rgba(255,255,255,0.85);
    border-radius:20px;
    padding:16px 12px 12px;
    box-shadow:0 6px 24px rgba(255,80,130,0.2);
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:10px;
    width:160px;
}

/* Escena animada 1 — oso con corazón */
.escena{
    width:140px;
    height:140px;
    border-radius:14px;
    background: linear-gradient(135deg,#fff0f6,#ffd6e8);
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
    overflow:hidden;
}

.oso{
    font-size:62px;
    animation: osito 1.8s ease-in-out infinite;
    position:relative;
    z-index:2;
}
@keyframes osito{
    0%,100%{transform:scale(1) rotate(-3deg);}
    50%{transform:scale(1.12) rotate(3deg);}
}

.corazon-anim{
    font-size:22px;
    position:absolute;
    animation: subir 1.8s ease-in-out infinite;
}
.corazon-anim:nth-child(2){top:18px;left:28px;animation-delay:0s;}
.corazon-anim:nth-child(3){top:10px;right:24px;animation-delay:0.6s;font-size:16px;}
.corazon-anim:nth-child(4){top:22px;right:44px;animation-delay:1.1s;font-size:14px;}

@keyframes subir{
    0%{opacity:0;transform:translateY(0) scale(0.5);}
    30%{opacity:1;transform:translateY(-18px) scale(1);}
    80%{opacity:0.6;transform:translateY(-50px) scale(0.8);}
    100%{opacity:0;transform:translateY(-70px) scale(0.5);}
}

/* Escena 2 — mamá e hijo */
.mama-hijo{
    font-size:0;
    display:flex;
    align-items:flex-end;
    gap:4px;
    animation: abrazo 2.2s ease-in-out infinite;
}
.mama-hijo span{font-size:52px;}
@keyframes abrazo{
    0%,100%{transform:scale(1);}
    40%{transform:scale(1.1);}
    60%{transform:scale(1.08);}
}

/* Escena 3 — flores girando */
.flores-wrap{
    position:relative;
    width:110px;
    height:110px;
}
.flor-centro{
    font-size:46px;
    position:absolute;
    top:50%;left:50%;
    transform:translate(-50%,-50%);
    animation: girar 4s linear infinite;
}
@keyframes girar{
    from{transform:translate(-50%,-50%) rotate(0deg);}
    to{transform:translate(-50%,-50%) rotate(360deg);}
}
.flor-orbit{
    font-size:22px;
    position:absolute;
    animation: orbitar 3s linear infinite;
    transform-origin: 55px 55px;
}
.flor-orbit:nth-child(2){top:-4px;left:44px;animation-delay:0s;}
.flor-orbit:nth-child(3){top:44px;right:-4px;animation-delay:-1s;}
.flor-orbit:nth-child(4){bottom:-4px;left:44px;animation-delay:-2s;}
.flor-orbit:nth-child(5){top:44px;left:-4px;animation-delay:-1.5s;}
@keyframes orbitar{
    from{transform:rotate(0deg) translateX(14px) rotate(0deg);}
    to{transform:rotate(360deg) translateX(14px) rotate(-360deg);}
}

.gif-frame span{
    font-size:12px;
    color:#c0396a;
    font-weight:700;
    text-align:center;
}

.divisor{
    font-size:22px;
    letter-spacing:8px;
    margin:12px 0;
    opacity:0.7;
}

</style>
</head>

<body class="fondoBase" id="cuerpo">

<div id="particulas"></div>

<!-- ══ PANTALLA 1 ══ -->
<div class="pantalla" id="p1">
    <div class="corazon-btn" onclick="abrir()">💖</div>
    <h1>Toca el corazón 💐</h1>
</div>

<!-- ══ PANTALLA 2 ══ -->
<div class="pantalla oculto" id="p2">
    <div class="caja">
        <h2>✨ ¿Cómo te llamas? ✨</h2>
        <p>Escribe tu nombre para personalizar el mensaje para mamá 🌸</p>
        <input id="nombre" placeholder="Tu nombre aquí..." maxlength="40"
               onkeydown="if(event.key==='Enter')entrar()">
        <button onclick="entrar()">💖 Continuar</button>
    </div>
</div>

<!-- ══ PANTALLA 3 ══ -->
<div class="pantalla oculto" id="p3">

    <div class="nombre-grande" id="saludo"></div>

    <div class="carta">
        <div class="titulo-carta">💖 Para la Mamá más hermosa del mundo 💖</div>

        <p>Gracias por ser el amor más bonito y más puro que existe. Desde el primer día de mi vida, tus manos me sostuvieron y tu corazón me dio calor. Eso nunca lo podré olvidar. 🌸</p>

        <div class="divisor">🌹 🌹 🌹</div>

        <p>Gracias por levantarte antes que todos, por trabajar sin descanso y por sonreír incluso cuando estabas cansada. Tú eres el motor silencioso de esta familia, la fuerza que mueve todo con amor. 💪❤️</p>

        <p>Por cada vez que me consolaste cuando lloré, por cada abrazo a tiempo, por cada "aquí estoy" que me diste… gracias, mamá. Tu presencia lo cura todo. 🤗</p>

        <div class="divisor">💐 💐 💐</div>

        <p>Eres sabia sin presumirlo, valiente sin saberlo y generosa sin medirlo. Nos das todo —tu tiempo, tu energía, tu amor— y nunca pides nada a cambio. Eso es algo que no tiene precio. 🌟</p>

        <p>Me enseñaste a ser buena persona, a levantarme cuando caigo, a dar gracias por lo pequeño y a luchar por lo que amo. Cada cosa buena que hay en mí viene de ti. 🦋</p>

        <div class="divisor">✨ ✨ ✨</div>

        <p>Hoy quiero que sepas que te admiro profundamente. Que eres mi ejemplo, mi refugio y mi mejor amiga. Que la vida sin ti no tendría el mismo color. 🌈</p>

        <p>No importa cuánto tiempo pase ni qué tan lejos estemos: mi amor por ti es infinito, como el tuyo por mí. 💞</p>

        <p>¡Feliz Día, Mamá! Ojalá este día y todos los que vengan estén llenos de flores, de risas y de la misma alegría que tú le das al mundo. 🎉🌺</p>

        <div class="firma">Con todo mi amor 💖<br>¡Te amo para siempre! 🌹</div>
    </div>

    <!-- TARJETAS ANIMADAS — sin dependencia de URLs externas -->
    <div class="gifs">

        <!-- Tarjeta 1: Oso con corazones -->
        <div class="gif-frame">
            <div class="escena">
                <span class="corazon-anim">💖</span>
                <span class="corazon-anim">💕</span>
                <span class="corazon-anim">❤️</span>
                <div class="oso">🐻</div>
            </div>
            <span>🐻 Con amor 💖</span>
        </div>

        <!-- Tarjeta 2: Mamá e hijo -->
        <div class="gif-frame">
            <div class="escena">
                <div class="mama-hijo">
                    <span>👩</span><span>🧒</span>
                </div>
            </div>
            <span>🤗 Te abrazo siempre</span>
        </div>

        <!-- Tarjeta 3: Flores girando -->
        <div class="gif-frame">
            <div class="escena">
                <div class="flores-wrap">
                    <div class="flor-centro">🌸</div>
                    <div class="flor-orbit">🌹</div>
                    <div class="flor-orbit">🌷</div>
                    <div class="flor-orbit">🌼</div>
                    <div class="flor-orbit">🌺</div>
                </div>
            </div>
            <span>🌹 Para ti mamá</span>
        </div>

    </div>

</div>

<script>

const contenedor = document.getElementById("particulas");
const emojis = ["🌹","💖","🌸","❤️","🌺","💕","🌷","💗","✨","🌼"];

function crearParticula(){
    const el = document.createElement("div");
    el.classList.add("particula");
    el.textContent = emojis[Math.floor(Math.random()*emojis.length)];
    el.style.left = (Math.random()*100) + "vw";
    const dur = 4 + Math.random()*6;
    el.style.animationDuration = dur + "s";
    el.style.animationDelay = (-Math.random()*dur) + "s";
    el.style.fontSize = (16 + Math.random()*18) + "px";
    contenedor.appendChild(el);
    setTimeout(()=>el.remove(), (dur+1)*1000);
}

setInterval(crearParticula, 220);
for(let i=0;i<30;i++) crearParticula();

function abrir(){
    document.getElementById("p1").classList.add("oculto");
    document.getElementById("p2").classList.remove("oculto");
    setTimeout(()=> document.getElementById("nombre").focus(), 400);
}

function entrar(){
    const n = document.getElementById("nombre").value.trim();
    if(!n){ 
        document.getElementById("nombre").style.borderColor="#ff4d6d";
        document.getElementById("nombre").placeholder="✏️ Por favor escribe tu nombre";
        return; 
    }
    document.getElementById("p2").classList.add("oculto");
    document.getElementById("p3").classList.remove("oculto");
    document.getElementById("cuerpo").classList.remove("fondoBase");
    document.getElementById("cuerpo").classList.add("fondoFinal");
    document.getElementById("saludo").innerHTML = "🌹 Feliz Día Mamá — con amor de " + n + " 💖";
}

</script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
