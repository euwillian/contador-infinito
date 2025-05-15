let timeLeft = 10;
let clicks = 0;
let timerInterval = null;

function startGame() {
  document.getElementById('intro').classList.add('hidden');
  document.getElementById('counter').classList.remove('hidden');
  document.getElementById('clicks').innerText = '0';
  clicks = 0;
  timeLeft = 10;
  document.getElementById('timer').innerText = timeLeft;
  timerInterval = setInterval(() => {
    timeLeft--;
    document.getElementById('timer').innerText = timeLeft;
    if (timeLeft <= 0) {
      endGame();
    }
  }, 1000);
}

function increment() {
  if (timeLeft > 0) {
    clicks++;
    document.getElementById('clicks').innerText = clicks;
  }
}

document.getElementById('clickButton').addEventListener('click', increment);

function endGame() {
  clearInterval(timerInterval);
  document.getElementById('counter').classList.add('hidden');
  document.getElementById('result').classList.remove('hidden');
  document.getElementById('finalClicks').innerText = clicks;

  fetch('/media')
    .then(response => response.json())
    .then(data => {
      const media = data.media;
      const score = Math.max(0, 100 - Math.abs(clicks - media) * 10);
      document.getElementById('mediaDia').innerText = media;
      document.getElementById('score').innerText = score;
    });
}

function sendResult() {
  const name = document.getElementById('playerName').value;
  fetch('/enviar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: name, clicks: clicks })
  })
    .then(() => fetchRanking());
}

function fetchRanking() {
  fetch('/ranking')
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById('rankingList');
      list.innerHTML = '';
      data.forEach(entry => {
        const li = document.createElement('li');
        li.textContent = `${entry.name || 'Anônimo'} - ${entry.score} pontos`;
        list.appendChild(li);
      });
    });
}

window.onload = fetchRanking;
