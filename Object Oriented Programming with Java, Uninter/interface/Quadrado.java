public class Quadrado implements Imprimivel{
    int medidaLado;

    public Quadrado(int medidaLado) {
        this.medidaLado = medidaLado;
    }

    @Override
    public void imprimir() {
        System.out.println("QUADRADO");
        System.out.println("Medida do lado:" + medidaLado);
        System.out.println("Área: " + 4 * medidaLado);
    }
}
