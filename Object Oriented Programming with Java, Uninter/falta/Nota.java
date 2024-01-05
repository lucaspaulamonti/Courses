public class Nota {
    private double notaUm;
    private double notaDois;
    private int faltas;

    public Nota(double notaUm, double notaDois, int faltas){
        setNotaUm(notaUm);
        setNotaDois(notaDois);
        setFaltas(faltas);
    }


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
    public void setFaltas(int faltas){
        if (faltas > 40 || faltas < 0){
            System.out.println("Faltas inválidas.");
            return;
        }
    }

    public double getNotaUm(){
        return notaUm;
    }
    public double getNotaDois(){
        return notaDois;
    }
    public int getFaltas(){
        return faltas;
    }

    void resultado(){
        double media = (notaUm + notaDois) / 2;

        System.out.println("Média:" + media);
        if (faltas > 7){
            System.out.println("Reprovado por faltas.");
        } else if(media < 4){
            System.out.println("Reprovado.");
        } else if (media < 7) {
            System.out.println("Exame.");
        } else {
            System.out.println("Aprovado.");
        }
    }
}
