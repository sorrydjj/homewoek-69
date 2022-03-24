function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function onClick(event) {
    let url = event.target.dataset.numUrl
    let csrftokens = getCookie('csrftoken');
    let a = document.getElementById('num1').value;
    let b = document.getElementById('num2').value;
    data = {A: a, B: b}
    let response = await fetch(url, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftokens
    }
    })
    let answer = await response.json();
    let ans = document.getElementById('answer');
    if (answer['answer']) {
        ans.innerHTML = '<p id="answer" style="color: green;">Ответ: <b>' + String(answer['answer']) + '</b></p>';
    } else {
        ans.innerHTML = '<p id="answer" style="color: red;">Ошибка: <b>' + String(answer['error']) + '</b></p>';
    }


}

function onLoad() {
    let btn = document.querySelectorAll("#buttons")
    for (i = 0; i < btn.length; i++) {
        btn[i].addEventListener("click", onClick)
    }
}

window.onload = onLoad