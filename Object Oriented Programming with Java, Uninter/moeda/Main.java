public class Main {
    public static void main(String[] args) {
        // Classes Moeda e Cofrinho com método de adicionar moedas.

        Cofrinho cofre = new Cofrinho();
        cofre.add(new Moeda("Euro", 0.5));
        cofre.add(new Moeda("Euro", 1));
        cofre.add(new Moeda("Euro", 0.1));
        cofre.add(new Moeda("Euro", 0.05));
        System.out.println("O total no cofrinho é de: " + cofre.calcularTotal());
    }
}