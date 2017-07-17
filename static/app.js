'use strict'

const playBttn = document.getElementById('main-form');
const nextBttn = document.getElementById('next-button');
const prevBttn = document.getElementById('prev-button');
const stopBttn = document.getElementById('stop-button');
const api = 'http://localhost:8000/api/'
// const api ='http://192.168.1.143:8000/api/'

function sendApiRequest(apiEndpoint, cb) {
  let xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState === XMLHttpRequest.DONE ) {
      if (xmlhttp.status === 200) {
        console.log(xmlhttp.response)
        if (cb) { cb(xmlhttp.response) };
        return console.log('wo0t success!');
      } else if (xmlhttp.status === 400) {
        return console.error('There was an error 400');
      } else if (xmlhttp.status === 500) {
        return console.error('');
      }
    }
  };

  xmlhttp.open("GET", apiEndpoint, true);
  xmlhttp.send();
}

// turn this into a multiuse notification rather than only success
function queueSuccessNotification(cat, num) {
  let successDiv = document.getElementById('success-notification');

  successDiv.textContent = `${num} random ${cat} files added to playlist!`;
  successDiv.classList.remove('hidden');

  setTimeout(_ => {
    successDiv.classList.add('hidden');
  }, 3000);
}

function updateTitle() {
  const nowPlaying = document.getElementById('now-playing');
  sendApiRequest(api + 'now_playing', body => {
    nowPlaying.innerHTML = '';
    nowPlaying.insertAdjacentHTML('beforeend', `${body}`);
  });
}

// events

// setInterval(updateTitle, 1000);

playBttn.addEventListener('submit', e => {
  let cat = document.getElementById('category');
  let num = document.getElementById('number');

  e.preventDefault();

  if (!cat.value) {
    return
  }

  sendApiRequest(api + `${cat.value}/${num.value || 3}`, _ => {
    queueSuccessNotification(cat.value, num.value || 3);
    cat.value = '';
    num.value = '';
    setTimeout(updateTitle, 600);
  });
});

nextBttn.addEventListener('click', e => {
  sendApiRequest((api + 'next'), _ => { setTimeout(updateTitle, 600); });
});

prevBttn.addEventListener('click', e => {
  sendApiRequest((api + 'prev'), _ => { setTimeout(updateTitle, 600); });
});

stopBttn.addEventListener('click', e => {
  sendApiRequest((api + 'stop'), _ => { setTimeout(updateTitle, 600); });
});
