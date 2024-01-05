import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Obtenha a entrada padrão peso (int), a altura (double) e imprima o IMC (Índice de Massa Corpórea).
        System.out.println("Informe o seu peso e a sua altura:");
        Scanner keyboard = new Scanner(System.in);
        int x = keyboard.nextInt();
        double y = keyboard.nextDouble();
        double imc = x / (y * y);
        System.out.printf("IMC: %.2f", imc);
    }
}