// Enviando uma função como parâmetro para outra função (callback).
let inner = function() {
    console.log('inner 1');
}
let outer = function(callback) {
    console.log('outer 1');
    callback();
    console.log('outer 2');
}
outer(inner);