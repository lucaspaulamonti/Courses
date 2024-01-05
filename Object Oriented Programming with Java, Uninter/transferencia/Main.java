public class Main {
    public static void main(String[] args) {
        //Complemente o exercício anterior criando um método de transferir que receba uma conta destino e um valor.
ContaCorrente CC1 = new ContaCorrente(00001,0,"Lucas",1000.00,500.00);
ContaCorrente CC2 = new ContaCorrente(00002,0,"Mario",1000.00,500.00);

        CC1.info();
        CC2.info();

        if(!CC1.movDebito(200)){
            System.out.println("Erro no saque.");
        } else {
            System.out.println("Sucesso no saque");
        }

        if(!CC1.movCredito(500)){
            System.out.println("Erro no depósito.");
        } else {
            System.out.println("Sucesso no depósito");
        }

        if(!CC1.movDebTransferencia(500, 00001, 0)){
            System.out.println("Erro na transferência.");
        } else {
                CC2.movCreTransferencia(500,0002,0);
                System.out.println("Sucesso na transferência.");
            }

        CC1.info();
        CC2.info();
    }
}