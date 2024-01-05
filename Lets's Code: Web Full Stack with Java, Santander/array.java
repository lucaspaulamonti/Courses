import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Crie uma array e imprima seus valores a partir de um for.
        String[] letra = {"A", "B", "C", "D", "E"};

        for (int i=0; i < letra.length; i++){
            System.out.println(letra[i]);
        }

        System.out.println(Arrays.toString(letra));
    }
}