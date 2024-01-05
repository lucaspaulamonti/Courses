// Simulando erros de sintaxe, semântica e lógica.

// Erro de sintaxe.
let multiply = (a b) => a + b; // Uncaught SyntaxError: Unexpected identifier
let result = multiply(10, 20);
console.log(result);

// Erro de semântica.
let multipl = (a, b) => a + b;
let result = multiply(10, 20); // Uncaught ReferenceError: multiply is not defined
console.log(result);

// Erro de lógica.
let multiply = (a, b) => a + b;  
let result = multiply(10, 20);
console.log(result); // 30 ?

// Erro de tipagem.
const someConstValue = 5;
someConstValue = 7; // Uncaught TypeError: Assignment to constant variable.

//Erro de alcance.
let testArray1 = Array(10);
console.log(testArray1.length); // 10
let testArray2 = Array(-1); // Uncaught RangeError: Invalid array length
console.log(testArray2.length);