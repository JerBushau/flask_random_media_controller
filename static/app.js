'use strict'

const mainForm = document.getElementById('main-form');
const nextBttn = document.getElementById('next-button');
const prevBttn = document.getElementById('prev-button');
const stopBttn = document.getElementById('stop-button');
// const api = 'http://localhost:8000/api/'
let api ='http://192.168.1.143:8000/api/'

function sendApiRequest(apiEndpoint, cb) {
  let xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
      if (xmlhttp.status == 200) {
        if (cb) { cb() };
        return console.log('wo0t success!');
      } else if (xmlhttp.status == 400) {
        return console.error('There was an error 400');
      } else if (xmlhttp.status == 500) {
        return console.error('');
      }
    }
  };

  xmlhttp.open("GET", apiEndpoint, true);
  xmlhttp.send();
}

function queueSuccessNotification(cat, num) {
  let successDiv = document.getElementById('success-notification');

  successDiv.textContent = `${num} random ${cat} files added to playlist!`;
  successDiv.classList.remove('hidden');

  setTimeout(_ => {
    successDiv.classList.add('hidden');
  }, 3000);
}

// events

mainForm.addEventListener('submit', e => {
  let cat = document.getElementById('category');
  let num = document.getElementById('number');

  e.preventDefault();

  if (!cat.value) {
    return
  }

  sendApiRequest(api + `${cat.value}/${num.value || 3}`, _ => {
    queueSuccessNotification(cat.value, num.value || 3);
  });

  cat.value = '';
  num.value = '';
});

nextBttn.addEventListener('click', e => {
  sendApiRequest((api + 'next'));
});

prevBttn.addEventListener('click', e => {
  sendApiRequest((api + 'prev'));
});

stopBttn.addEventListener('click', e => {
  sendApiRequest((api + 'stop'));
});
