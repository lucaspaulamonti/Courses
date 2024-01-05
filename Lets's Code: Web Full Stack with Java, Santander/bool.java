public class Main {
    public static void main(String[] args) {
//      Utilize variáveis booleanas para representar um algorítimo com atribuições condicionadas.
        boolean fimDeSemana = true;
        boolean fazSol = false;
        boolean irAPraia = fimDeSemana && fazSol;
        String aFimDeSemana = fimDeSemana ? "É fim de semana." : "Não é fim de semana.";
        System.out.println(aFimDeSemana);
        String aFazSol = fazSol ? "Faz sol." : "Não faz sol";
        System.out.println(aFazSol);
        String aIrAPraia = irAPraia ? "Ir a praia" : "Não ir a praia";
        System.out.println(aIrAPraia);
    }
}