public class Main {
    public static void main(String[] args) {
//      Crie um laço de repetição aninhado for que imprima as tabuadas de 1 a 10.
        for (int i = 1; i <= 10; i++){
            for (int j = 1; j <= 10; j++){
                System.out.println(j + "x" + i + "=" + j * i);
            }
        }
    }
}