let moneyElement = document.getElementById('money');
let amount = 100;

function growMoney() {
    amount += Math.floor(Math.random() * 100); // Incrementa el dinero aleatoriamente
    moneyElement.textContent = `$${amount}`;
    moneyElement.style.transform = 'scale(1.2)'; // Efecto de crecimiento
    setTimeout(() => {
        moneyElement.style.transform = 'scale(1)'; // Vuelve al tamaño original
    }, 500);
}

setInterval(growMoney, 1000); // Actualiza cada segundo
