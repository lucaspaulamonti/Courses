public class Aluno {
    String nome;
    String curso;
    Avaliacao nota;

    Aluno(String nome, String curso, Avaliacao nota){
        this.nome = nome;
        this.curso = curso;
        this.nota = nota;
    }

    void info(){
        System.out.println("Nome: " + nome);
        System.out.println("Curso: " + curso);
        System.out.println("Média A.: " + nota.mediaAritmetica());
        System.out.println("Média P.: " + nota.mediaPonderada());
    }
}
