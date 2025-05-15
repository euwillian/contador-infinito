
from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
        <html>
        <head><title>Contador Infinito</title></head>
        <body style="background-color:#121212; color:white; text-align:center;">
            <h1>Contador Infinito</h1>
            <p>Clique no botão o máximo que puder em 10 segundos!</p>
            <button onclick="startGame()">Iniciar</button>
            <p id="counter">0</p>
            <script>
                let count = 0;
                let active = false;
                function startGame() {
                    count = 0;
                    active = true;
                    document.getElementById("counter").innerText = count;
                    setTimeout(() => active = false, 10000);
                }
                document.addEventListener("click", () => {
                    if (active) {
                        count += 1;
                        document.getElementById("counter").innerText = count;
                    }
                });
            </script>
        </body>
        </html>
    """)
