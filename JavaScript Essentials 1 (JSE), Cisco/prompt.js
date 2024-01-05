// Criando prompt para inserção de dados pelo usuário.
let name = window.prompt("What is your name?", "John Doe");
name = name ? name : "anonymous";

let age = prompt("Hello " + name + " how old are you?");
alert(name + " is " + age + " years old");