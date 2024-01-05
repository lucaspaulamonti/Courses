// Calculando o fatorial de N por meio de função com while.
function factorial (n) {
    let result = 1;
    while (n > 1) {
        result *= n;
        n--;
    }
    return result;
}
console.log(factorial(6));
