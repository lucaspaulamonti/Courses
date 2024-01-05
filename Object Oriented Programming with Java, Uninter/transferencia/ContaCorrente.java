import java.sql.SQLOutput;

public class ContaCorrente {
    int ccNumero;
    int ccDigito;
    String ccTitular;
    double ccSaldo;
    double ccLimite;

    public ContaCorrente(int ccNumero, int ccDigito, String ccTitular, double ccSaldo, double ccLimite){
        this.ccNumero = ccNumero;
        this.ccDigito = ccDigito;
        this.ccTitular = ccTitular;
        this.ccSaldo = ccSaldo;
        this.ccLimite = ccLimite;
    }

    void info(){
        System.out.println("Nome: "+ccTitular);
        System.out.println("Numero: "+ccNumero);
        System.out.println("Dígito: "+ccDigito);
        System.out.println("Saldo: "+ccSaldo);
        System.out.println("Limite: "+ccLimite);
    }

    boolean movDebito(double movValor){
        if((movValor>ccLimite)||(movValor>ccSaldo)||(movValor<=0)){
            return false;
        }
        System.out.println(ccTitular);
        System.out.println("-"+movValor);
        ccSaldo-=movValor;
        return true;
    }

    boolean movCredito(double movValor){
        if(movValor<=0){
            return false;
        }
        System.out.println(ccTitular);
        System.out.println("+"+movValor);
        ccSaldo+=movValor;
        return true;
    }

    boolean movDebTransferencia(double movValor, int ccNumero, int ccDigito){
        if(movValor>ccLimite){
            return false;
        }
        if(movValor>ccSaldo){
            return false;
        }
        if(movValor<=0){
            return false;
        }
        System.out.println(ccTitular);
        System.out.println("-"+movValor);
        ccSaldo-=movValor;
        return true;
    }
    void movCreTransferencia(double movValor, int ccNumero, int ccDigito){
        System.out.println(ccTitular);
        System.out.println("+"+movValor);
        ccSaldo+=movValor;
    }
}
