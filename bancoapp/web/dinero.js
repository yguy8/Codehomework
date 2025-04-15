class CuentaBancaria {
    constructor(titular, saldoInicial = 0) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    depositar(cantidad) {
        if (cantidad > 0) {
            this.saldo += cantidad;
            console.log(`Depósito exitoso: $${cantidad}. Saldo actual: $${this.saldo}.`);
        } else {
            console.log("La cantidad a depositar debe ser mayor a cero.");
        }
    }

    retirar(cantidad) {
        if (cantidad > 0 && cantidad <= this.saldo) {
            this.saldo -= cantidad;
            console.log(`Retiro exitoso: $${cantidad}. Saldo actual: $${this.saldo}.`);
        } else if (cantidad > this.saldo) {
            console.log("Fondos insuficientes.");
        } else {
            console.log("La cantidad a retirar debe ser mayor a cero.");
        }
    }

    consultarSaldo() {
        console.log(`Saldo actual: $${this.saldo}.`);
    }
}

// Ejemplo de uso
const miCuenta = new CuentaBancaria("Juan Pérez", 1000);
miCuenta.consultarSaldo();  // Saldo actual: $1000.
miCuenta.depositar(500);    // Depósito exitoso: $500. Saldo actual: $1500.
miCuenta.retirar(200);      // Retiro exitoso: $200. Saldo actual: $1300.
miCuenta.consultarSaldo();  // Saldo actual: $1300.


