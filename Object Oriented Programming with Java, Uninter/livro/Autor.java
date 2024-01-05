public class Autor {
    private String nome;
    private String nacionalidade;
    private String email;

    public Autor() {
    }
    public Autor(String nome, String nacionalidade, String email) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.email = email;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }
    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

    void info(){
        System.out.println("Nome do autor: " + nome);
        System.out.println("Nacionalidade do autor: " + nacionalidade);
        System.out.println("E-Mail do autor: " + email);;
    }
}