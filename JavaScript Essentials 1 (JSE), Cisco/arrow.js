// Transformando função em arrow.
let add = function(a, b) {
    return a + b;
}
console.log(add(10, 20));

// ...

let add1 = (a, b) => {
    return a + b;
}
console.log(add(10, 20));

// ...

let add2 = (a, b) => a + b;
console.log(add(10, 20));