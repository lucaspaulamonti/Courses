// Substituindo if's e elses' por operadores ternários.
// let price = 100;
// let shippingCost;
// if (price > 50) {
//     shippingCost = 0;
// } else {
//     shippingCost = 5;
// }
// console.log('price = ${price}, shipping = ${shippingCost}');


let price = 100;
let shippingCost = price > 50 ? 0 : 5;
console.log('price = ${price}, shipping = ${shippingCost}');