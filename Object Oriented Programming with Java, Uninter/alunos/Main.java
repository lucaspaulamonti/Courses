public class Main {
    public static void main(String[] args) {
        //  Crie uma classe Aluno com os atributos nome, matrícula, desconto e curso. Métodos: descrever e pagamento.

        Aluno alunoUm = new Aluno("Lucas", 111, 0.1, new Curso("Engenharia", 1000));
        alunoUm.info();
    }
}