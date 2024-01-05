public class Ingresso {
    public String nomeEvento;
    public double valor;

    public Ingresso(String nomeEvento, double valor) {
        this.nomeEvento = nomeEvento;
        this.valor = valor;
    }

    public void info(){
        System.out.println("Nome do evento: " + nomeEvento);
        System.out.println("Valor do ingresso: " + valor);
    }

}
