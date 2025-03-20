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
