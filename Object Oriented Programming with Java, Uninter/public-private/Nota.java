public class Nota {
    private double notaUm;
    private double notaDois;

    public void setNotaUm(double nota){
        if (nota < 0 || nota > 10){
            System.out.println("Nota inválida.");
            return;
        }
        notaUm = nota;
    }
    public void setNotaDois(double nota) {
        if (nota < 0 || nota > 10) {
            System.out.println("Nota inválida.");
            return;
        }
        notaDois = nota;
    }

    public double getNotaUm(){
        return notaUm;
    }
    public double getNotaDois(){
        return notaDois;
    }

    void resultado(){
        double media = (notaUm + notaDois) / 2;

        System.out.println("Média:" + media);
        if(media < 4){
            System.out.println("Reprovado.");
        } else if (media < 7) {
            System.out.println("Exame.");
        } else {
            System.out.println("Aprovado.");
        }
    }
}
