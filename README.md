# Contador Infinito

Um jogo simples e viciante onde o desafio é se conter! Você tem 10 segundos para clicar o máximo de vezes possível — mas atenção: ganha mais pontos quem se aproxima da média do dia.

## 🧠 Como funciona

- Duração: 10 segundos
- Objetivo: clicar várias vezes
- Pontuação: quanto mais próximo da média diária, maior a pontuação
- Ranking: os melhores do dia aparecem no topo!

## ▶️ Como rodar localmente

1. Clone o repositório:
```bash
git clone <repo>
cd contador-infinito
```

2. Instale as dependências:
```bash
pip install flask flask_sqlalchemy flask_cors
```

3. Rode o servidor:
```bash
python app.py
```

4. Acesse em:
```
http://127.0.0.1:5000
```

## 🌐 Como publicar online (Render)

1. Crie uma conta em: https://render.com
2. Clique em "New Web Service"
3. Conecte seu repositório do GitHub
4. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
   - Runtime: Python 3.x
   - Publicar com SQLite funciona, mas para produção, recomenda-se PostgreSQL

## 📁 Estrutura

- `app.py` — servidor Flask
- `index.html` — interface do jogo
- `static/script.js` — lógica do jogo
