public class Main {
    public static void main(String[] args) {
        //Crie uma classe Conta para administrar contas correntes de um banco.
        Conta c1 = new  Conta(111, "Mario", 2000, 500);

        if(!c1.debito(200)){
            System.out.println("Erro no saque.");
        }
        if(!c1.credito(500)){
            System.out.println("Erro no depósito.");
        }
        c1.info();
    }
}