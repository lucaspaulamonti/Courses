public class Conta {
    String nome;
    double saldo;
    public Conta(String nome, double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }
    void depositar(double valor) throws Exception{
        if (valor < 0){
            throw new Exception("Valor inválido.");
        }
        saldo += valor;
    }
    void sacar(double valor) throws Exception{
        if (valor > saldo){
            throw new Exception("Saldo Insuficiente.");
        }
        if (valor < 0){
            throw new Exception("Valor inválido.");
        }
        saldo -= valor;
    }
    void transferir(double valor, Conta destino) throws Exception{
        this.sacar(valor);
        destino.depositar(valor);
    }
    void info(){
        System.out.println("Nome: " + nome);
        System.out.println("Saldo: " + saldo);
    }
}