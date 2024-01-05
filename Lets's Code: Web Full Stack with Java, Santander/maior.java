public class Main {
    public static void main(String[] args) {
        // Descubra o maior, menor e média de todos os inteiros de uma array.
        int[] numero = {9, 10, 12, 25, 2};
        int maior = numero[0];
        int menor = numero[0];
        float medio = 0;

        for (int i=0; i < numero.length; i++){
            if (numero[i] > maior){
                maior = numero[i];
            }
            if (numero[i] < menor){
                menor = numero[i];
            }
            medio += (float) numero[i];
        }
        System.out.println("Maior: " + maior);
        System.out.println("Menor: " + menor);
        System.out.println("Média: " + (medio / numero.length));

    }
}