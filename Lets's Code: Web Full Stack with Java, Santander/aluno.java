public class Main {
    public static void main(String[] args) {
//    Crie uma estrutura condicional com if, else e switch que exiba aprovação/reprovação de aluno.
        int nota = 70;
        String resultado;

        if (nota >= 80) {
            System.out.println("Aluno com média A.");
            resultado = "A";
        } else if (nota < 80 && nota >= 70) {
            System.out.println("Aluno com média B.");
            resultado = "B";
        } else if (nota < 70 && nota >= 60) {
            System.out.println("Aluno com média C.");
            resultado = "C";
        } else if (nota < 60 && nota >= 0) {
            System.out.println("Aluno com média D.");
            resultado = "D";
        } else {
            System.out.println("Nota inválida.");
            resultado = "";
        }

        switch (resultado) {
            case "A":
            case "B":
            case "C":
                System.out.println("Aluno aprovado.");
                break;
            case "D":
                System.out.println("Aluno reprovado.");
                break;
            default:
                System.out.println("Algo deu errado.");
        }
    }
}