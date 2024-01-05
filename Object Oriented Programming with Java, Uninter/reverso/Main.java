import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Leia uma sequência de N strings e as imprima em ordem reversa utilizando um método.
        System.out.println("Informe a quantidade de nomes:");
        Scanner keyboard = new Scanner(System.in);
        int qnt = keyboard.nextInt();
        ArrayList <String> seq = new ArrayList <String> ();
        for (int i = 0; i < qnt; i ++){
            seq.add(keyboard.next());
        }
        for (int i = seq.size() - 1; i >= 0; i --){
            System.out.println(seq.get(i));
        }
    }
}