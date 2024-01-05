// Calculando o fatorial de N por meio de função com recursão.
function factorial (n) {
    return n > 1 ? n * factorial(n - 1) : 1;
}
console.log(factorial(6));