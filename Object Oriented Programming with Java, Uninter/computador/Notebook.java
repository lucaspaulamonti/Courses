public class Notebook extends Computador{
    int polegadasTela;

    public Notebook(int gbMemoria, int numProcessadores, int polegadasTela) {
        super(gbMemoria, numProcessadores);
        this.polegadasTela = polegadasTela;
    }

    @Override
    double calculaValor() {
        double total = (250 * gbMemoria) + (500 * numProcessadores) + (100 * polegadasTela);
        return total;
    }
}
