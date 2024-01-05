public class Main {
    public static void main(String[] args) {
        //  Crie uma interface que imprime todos os atributos das classes.
        Funcionario f = new Funcionario("Mario", "111.222.333-4");
        Carro c = new Carro("Palio", "Cinza", 4);
        Quadrado q = new Quadrado(10);

        Imprimivel i = f;
        i.imprimir();
        i = c;
        i.imprimir();
        i = q;
        i.imprimir();
    }
}