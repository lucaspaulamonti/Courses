import java.util.ArrayList;
public class Cofrinho{
    private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();

    //Método adicionar.
    public void adicionar(int tipoMoeda, double valorMoeda){
        //Switch recebe inteiro e double colhidos.
        switch (tipoMoeda) {
            //Chama o add com a subclasse correspondente ao inteiro recebido.
            case 1 -> listaMoedas.add(new Real(valorMoeda));
            case 2 -> listaMoedas.add(new Dolar(valorMoeda));
            case 3 -> listaMoedas.add(new Euro(valorMoeda));
        }
    }

    //Método remover.
    public void remover(int tipoMoeda, double valorMoeda) {
        // Para cada Moeda na listaMoeda.
        for (Moeda listaMoeda : listaMoedas) {

            //Colhendo a classe da moeda.
            String type = String.valueOf(listaMoeda.getClass());
            //Colhendo o valor da moeda.
            double value = listaMoeda.info();

            //Se inteiro recebido for 1.
            if (tipoMoeda == 1){
                //Se a classe for igual a coletada pelo usuário.
                if (type.equals("class Real")) {
                    //Se o valor for igual ao coletado pelo usuário.
                    if (value == valorMoeda) {
                        //Remove a moeda correspondente.
                        listaMoedas.remove(listaMoeda);
                        break;
                    }
                }
            }

            //Se inteiro recebido for 2.
            if (tipoMoeda == 2) {
                //Se a classe for igual a coletada pelo usuário.
                if (type.equals("class Dolar")) {
                    //Se o valor for igual ao coletado pelo usuário.
                    if (value == valorMoeda) {
                        //Remove a moeda correspondente.
                        listaMoedas.remove(listaMoeda);
                        break;
                    }
                }
            }

            //Se inteiro recebido for 3.
            if (tipoMoeda == 3) {
                //Se a classe for igual a coletada pelo usuário.
                if (type.equals("class Euro")) {
                    //Se o valor for igual ao coletado pelo usuário.
                    if (value == valorMoeda) {
                        //Remove a moeda correspondente.
                        listaMoedas.remove(listaMoeda);
                        break;
                    }
                }
            }
        }
    }

    //Método listagemMoedas.
    public void listagemMoedas(){
        //Se não existirem moedas.
        if(listaMoedas.isEmpty()){
            System.out.println("Não existem moedas.");
            System.out.println();

        } else {
            int count = 1;
            for (Moeda listaMoeda : listaMoedas) {
                System.out.println("Moeda: " + count);
                System.out.println(listaMoeda.getClass());
                System.out.println(listaMoeda.info());
                count++;
            }
            System.out.println();
        }
    }

    //Método totalConvertido.
    public void totalConvertido(){
        //Se não existirem moedas.
        if(listaMoedas.isEmpty()){
            System.out.println("Não existem moedas.");
            System.out.println();

        } else {
            double total = 0;
            for (Moeda listaMoeda : listaMoedas) {
                total += listaMoeda.converter();
            }
            System.out.println("Total de R$:" + total);
            System.out.println();
        }
    }
}