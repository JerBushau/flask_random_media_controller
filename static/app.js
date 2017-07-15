'use strict'

const mainForm = document.querySelector('.main-form');

function sendApiRequest(cat, num) {
  let xmlhttp = new XMLHttpRequest();
  let apiEndpoint =`http://192.168.1.143:8000/api/${cat}/${num}`;

  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
      if (xmlhttp.status == 200) {
        console.log('wo0t success!');
      } else if (xmlhttp.status == 400) {
        console.error('There was an error 400');
      } else {
        console.error('something else other than 200 was returned');
      }
    }
  };

  xmlhttp.open("GET", apiEndpoint, true);
  xmlhttp.send();
}

mainForm.addEventListener('submit', e => {
  let cat = document.getElementById('category');
  let num = document.getElementById('number');

  e.preventDefault();
  sendApiRequest(cat.value, num.value || 3);
  cat.value = '';
  num.value = '';
});
