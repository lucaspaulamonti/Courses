public class Main {
    public static void main(String[] args) {
        //  Crie uma classe abstrata computador com os atributos gbmemoria e numprocessadores e o método abstrato calculavalor. Implemente duas classes filhas, desktop e notebook.

        Desktop compA = new Desktop(8,4,600);
        Notebook compB = new Notebook(8,4,15);

        Computador comp;

        comp = compA;
        System.out.println("Valor: " + comp.calculaValor());
        comp = compB;
        System.out.println("Valor: " + comp.calculaValor());
    }
}