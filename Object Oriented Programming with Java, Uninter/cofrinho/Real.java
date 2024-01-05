public class Real extends Moeda {
    public Real(double valor) {
        super(valor);
    }
    @Override
    public double info() {
        return this.valor;
    }
    @Override
    public double converter() {
        return this.valor;
    }
}
