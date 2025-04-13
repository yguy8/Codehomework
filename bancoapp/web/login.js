function login() {

    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("contraseña").value;

    if (user == "x" && pass == "1234") {
        window.location.href = "home.html";
        alert("Bienvenido " + user);

    }
    else {
        alert("Datos incorrectos, por favor verifica tu usuario y contraseña");
    }
}

