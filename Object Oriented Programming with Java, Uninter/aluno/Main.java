public class Main {
    public static void main(String[] args) {
        //Crie uma classe aluno com atributos string nome, curso. Crie também um atributo da classe avaliacao. Cada aluno deve ter uma avaliacao associada. Imprima as informações completas.
        Aluno a1 = new Aluno("Lucas", "Psicologia", new Avaliacao(9, 10, 3));
        Aluno a2 = new Aluno("Mario", "Psicologia", new Avaliacao(5, 5, 3));
        a1.info();
        a2.info();
    }
}