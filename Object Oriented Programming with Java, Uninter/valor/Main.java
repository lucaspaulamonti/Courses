import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Crie uma condição com operador ternário que informa se o número digitado pelo usuário está acima ou abaixo do número correto.
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Informe o seu palpite: ");
        int x = keyboard.nextInt();
        int y = 100;
        while (x != y) {
            String z = x < y ? "Um pouco mais." : "Um pouco menos.";
            System.out.println(z);
            System.out.println("Informe outro palpite: ");
            x = keyboard.nextInt();
        }
        System.out.println("Acertou!");
    }
}