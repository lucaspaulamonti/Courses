public class Main {
    public static int[] instanciaArray(int n){
        return new int[n];
    }
    public static void main(String[] args) {
        //Crie um método que recebe um inteiro e retorna uma intância para um vetor de n posições de inteiros. Trate a exceção "NegativeArraySizeException".
        int t = 10;
        int[] arr;
        try {
            arr = instanciaArray(t);
            for (int i = 0; i < t; i++){
                System.out.println(arr[i]);
            }
        } catch (NegativeArraySizeException e) {
            System.out.println("Valor inválido.");
            System.out.println(e.getMessage());
        }
    }
}