// Validando um parâmetro passado para a função.
function getMeanTemp(temperatures) {
    if (!(temperatures instanceof Array)) {
        return NaN;
    }
    let sum = 0;
    for (let i = 0; i < temperatures.length; i++) {
        sum += temperatures[i];
    }
    return sum / temperatures.length;
}
console.log(getMeanTemp(10));
console.log(getMeanTemp([10, 30]));