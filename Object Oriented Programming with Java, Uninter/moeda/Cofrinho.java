import java.util.ArrayList;

public class Cofrinho {
    private ArrayList<Moeda> moedas = new ArrayList();

    public void add(Moeda x){
        moedas.add(x);
    }

    public double calcularTotal(){
        double total = 0;
        for (Moeda x: moedas) {
            total += x.getValor();
        }
        return total;
    }
}
