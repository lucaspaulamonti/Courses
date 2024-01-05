// Utilizando os operadores lógicos and, or e not.
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

console.log(!true); // false
console.log(!false); // true

console.log("Alice" && "Bob"); // Bob
console.log("Alice" || "Bob"); // Alice

let a = true;
console.log(a); // true
a &&= false;
console.log(a); // false
// The instruction a &&= false means exactly the same as a = a && false.

let b = false;
console.log(b); // false
b ||= true;
console.log(b); // true
// This time, the operation b ||= true is interpreted as b = b || true.