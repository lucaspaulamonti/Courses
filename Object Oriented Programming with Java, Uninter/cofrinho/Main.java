import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Instanciando a classe Cofrinho.
        Cofrinho Cofrinho = new Cofrinho();

        //Menu principal do programa.
        while (true) {
            System.out.println("Cofrinho.");
            System.out.println("1. Adicionar moedas.");
            System.out.println("2. Remover moedas.");
            System.out.println("3. Listar moedas.");
            System.out.println("4. Converter moedas.");
            System.out.println("0. Sair.");

            //Colhendo o próximo inteiro informado pelo usuário.
            try {
                Scanner scanTypeKeyboardMenu = new Scanner(System.in);
                int keyboardMenu = scanTypeKeyboardMenu.nextInt();
                System.out.println();

                // Se 0, encerrando o programa.
                if (keyboardMenu == 0) {
                    System.out.println("Saindo.");
                    break;

                    //Se < 0 ou > 4, tratando como inválido.
                } else if (keyboardMenu < 0 || keyboardMenu > 4) {
                    System.out.println("Informe um valor válido.");
                    System.out.println();

                    //Se 1, Adicionar moedas.
                } else if (keyboardMenu == 1) {
                    while (true) {
                        System.out.println("Adicionar moedas.");
                        System.out.println("Informe o tipo: 1. Real, 2. Dolar, 3. Euro.");
                        System.out.println("Ou 0. Cancelar.");

                        //Colhendo o próximo inteiro informado pelo usuário.
                        try {
                            Scanner scanTypeKeyboardTipo = new Scanner(System.in);
                            int keyboardTipo = scanTypeKeyboardTipo.nextInt();
                            System.out.println();

                            // Se 0, voltando para o loop anterior.
                            if (keyboardTipo == 0) {
                                break;

                                //Se < 0 ou > 3, tratando como inválido.
                            } else if (keyboardTipo < 0 || keyboardTipo > 3) {
                                System.out.println("Informe um valor válido.");
                                System.out.println();

                            } else {
                                System.out.println("Informe o valor.");
                                System.out.println("Ou 0. Cancelar.");

                                //Colhendo o próximo double informado pelo usuário.
                                try {
                                    Scanner scanTypeKeyboardValor = new Scanner(System.in);
                                    double keyboardValor = scanTypeKeyboardValor.nextDouble();
                                    System.out.println();

                                    // Se 0, voltando para o loop anterior.
                                    if (keyboardValor == 0.0) {
                                        break;

                                        // Se < 0, tratando como inválido.
                                    } else if (keyboardValor < 0.0) {
                                        System.out.println("Informe um valor válido.");
                                        System.out.println();

                                    } else {
                                        // Chamando método Cofrinho.adicionar com inteiro e double colhidos.
                                        Cofrinho.adicionar(keyboardTipo, keyboardValor);
                                        System.out.println();
                                        break;
                                    }
                                    //Tratando strings não desejadas.
                                } catch (InputMismatchException e) {
                                    System.out.println("Informe um valor válido.");
                                    System.out.println();
                                    break;
                                }
                            }
                            //Tratando strings não desejadas.
                        } catch (InputMismatchException e) {
                            System.out.println("Informe um valor válido.");
                            System.out.println();
                            break;
                        }
                    }
                    //Se 2, Remover moedas.
                } else if (keyboardMenu == 2) {
                    while (true) {
                        System.out.println("Remover moedas.");
                        System.out.println("Informe o tipo: 1. Real, 2. Dolar, 3. Euro.");
                        System.out.println("Ou 0. Cancelar.");

                        //Colhendo o próximo inteiro informado pelo usuário.
                        try {
                            Scanner scanTypeKeyboardTipo = new Scanner(System.in);
                            int keyboardTipo = scanTypeKeyboardTipo.nextInt();
                            System.out.println();

                            // Se 0, voltando para o loop anterior.
                            if (keyboardTipo == 0) {
                                break;

                                //Se < 0 ou > 3, tratando como inválido.
                            } else if (keyboardTipo < 0 || keyboardTipo > 3) {
                                System.out.println("Informe um valor válido.");
                                System.out.println();

                            } else {
                                System.out.println("Informe o valor.");
                                System.out.println("Ou 0. Cancelar.");

                                //Colhendo o próximo double informado pelo usuário.
                                try {
                                    Scanner scanTypeKeyboardValor = new Scanner(System.in);
                                    double keyboardValor = scanTypeKeyboardValor.nextDouble();
                                    System.out.println();

                                    // Se 0, voltando para o loop anterior.
                                    if (keyboardValor == 0.0) {
                                        break;

                                        // Se < 0, tratando como inválido.
                                    } else if (keyboardValor < 0.0) {
                                        System.out.println("Informe um valor válido.");
                                        System.out.println();

                                    } else {
                                        // Chamando método Cofrinho.remover com inteiro e double colhidos.
                                        Cofrinho.remover(keyboardTipo, keyboardValor);
                                        System.out.println();
                                        break;
                                    }
                                    //Tratando strings não desejadas.
                                } catch (InputMismatchException e) {
                                    System.out.println("Informe um valor válido.");
                                    System.out.println();
                                    break;
                                }
                            }
                            //Tratando strings não desejadas.
                        } catch (InputMismatchException e) {
                            System.out.println("Informe um valor válido.");
                            System.out.println();
                            break;
                        }
                    }

                    //Se 3, Listar moedas.
                } else if (keyboardMenu == 3) {
                    System.out.println("Listar moedas.");

                    // Chamando método Cofrinho.listagemMoedas.
                    Cofrinho.listagemMoedas();

                    //Se 4, Converter moedas.
                } else {
                    System.out.println("Converter moedas.");

                    // Chamando método Cofrinho.totalConvertido.
                    Cofrinho.totalConvertido();
                }
                //Tratando strings não desejadas.
            } catch (InputMismatchException e) {
                System.out.println("Informe um valor válido.");
                System.out.println();
            }
        }
    }
}