public class Main {
    public static void main(String[] args) {
        //  Desenvolva uma classe conta com os métodos depositar, sacar e transferir. Utilize exceptions para tentativas inválidas.

        Conta c1 = new Conta("Mario",5000);
        Conta c2 = new Conta("Luigi",5000);

        try {
            c1.depositar(-1);
        } catch (Exception e){
            System.out.println("Ocorreu um erro.");
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Fechando o programa.");
        }

        try {
            c1.transferir(400,c2);
        } catch (Exception e){
            System.out.println("Ocorreu um erro.");
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Fechando o programa.");
        }
    }
}