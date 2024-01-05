abstract class Moeda{
    double valor;
    public Moeda(double valor) {
        this.valor = valor;
    }
    abstract double info();
    abstract double converter();
}
