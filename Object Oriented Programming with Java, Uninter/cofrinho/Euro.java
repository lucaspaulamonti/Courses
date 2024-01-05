public class Euro extends Moeda {
    public Euro(double valor) {
        super(valor);
    }
    @Override
    public double info() {
        return this.valor;
    }
    @Override
    public double converter() {
        return this.valor * 6;
    }
}
