var username = document.getElementById("welcome-message").getAttribute("data-username");

var currentHour = new Date().getHours(); // Pegando a hora local no formato de 24h

// Mensagem de boas-vindas com base na hora local
var welcomeMessage = "";

if (currentHour < 12) {
  welcomeMessage = "Bom dia, " + username + "!";
} else if (currentHour < 18) {
  welcomeMessage = "Boa tarde, " + username + "!";
} else {
  welcomeMessage = "Boa noite, " + username + "!";
}

document.getElementById("welcome-message").innerHTML = welcomeMessage;

function toggleEdit(id) {
  const viewMode = document.getElementById('view-mode-' + id);
  const editForm = document.getElementById('edit-form-' + id);
  const botoes = document.getElementById('botoes-' + id);

  viewMode.classList.add('d-none');
  editForm.classList.remove('d-none');
  if (botoes) {
    botoes.classList.add('d-none');
  }
}

function cancelEdit(id) {
  const viewMode = document.getElementById('view-mode-' + id);
  const editForm = document.getElementById('edit-form-' + id);
  const botoes = document.getElementById('botoes-' + id);

  viewMode.classList.remove('d-none');
  editForm.classList.add('d-none');
  if (botoes) {
    botoes.classList.remove('d-none');
  }
}

function salvarEdicao(event, id) {
  event.preventDefault(); // Impede o envio padrão

  const input = document.getElementById('input-titulo-' + id);
  const novoTitulo = input.value;

  fetch(`/editar_ajax/${id}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ tarefa: novoTitulo }),
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'ok') {
      // Atualiza o texto na interface
      document.getElementById('view-mode-' + id).innerText = data.titulo;
      cancelEdit(id); // Volta para o modo de visualização
    } else {
      alert('Erro ao salvar: ' + data.mensagem);
    }
  })
  .catch(error => {
    console.error('Erro AJAX:', error);
    alert('Erro na requisição');
  });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}