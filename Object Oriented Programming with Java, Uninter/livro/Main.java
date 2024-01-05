public class Main {
    public static void main(String[] args) {
        // Utilize herança para criar as classes livro físico e livro digital.
        LivroDigital ld = new LivroDigital("Senhor dos Anéis",
                new Autor("Tolkien", "Britânico", "tolkien@email.com"),
                "Aventura",5,10000,3500);
        ld.info();
        LivroFisico lf = new LivroFisico("Harry Potter",
                new Autor("J.K.R.", "Britânica", "jkr@email.com"),
                "Aventura", 10,1,1);
        lf.info();
    }
}