function login() {

    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("contraseña").value;

    if (user == "" && pass == "") {
        window.location.href = "home.html";

    }
    else {
        alert("Datos incorrectos, por favor verifica tu usuario y contraseña");
    }
}
