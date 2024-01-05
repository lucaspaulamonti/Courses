public class Dolar extends Moeda {
    public Dolar(double valor) {
        super(valor);
    }
    @Override
    public double info() {
        return this.valor;
    }
    @Override
    public double converter() {
        return this.valor * 5;
    }
}
