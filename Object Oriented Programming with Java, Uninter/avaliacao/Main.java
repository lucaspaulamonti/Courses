public class Main {
    public static void main(String[] args) {
        //Crie uma classe Avaliacao com três atributos reais chamados nota1, nota2, nota3 e crie dois métodos para calcular e retornar média aritmética e média ponderada (peso 2, 3 e 4).
        Avaliacao luigui = new Avaliacao();
        luigui.n1 = 5;
        luigui.n2 = 10;
        luigui.n3 = 7;
        Avaliacao mario = new Avaliacao(7, 4, 10);
        System.out.println("Média aritmética do Luigui: " + luigui.mediaAritmetica());
        System.out.println("Média ponderada do Luigui: " + luigui.mediaPonderada());
        System.out.println("Média aritmética do Mário: " + mario.mediaAritmetica());
        System.out.println("Média ponderada do Mário: " + mario.mediaPonderada());
    }
}