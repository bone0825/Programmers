
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for(int i = 0; i < T; i++){
            int a = sc.nextInt();
            String[] b = sc.next().split("");
            for(String k :b){
                System.out.print(k.repeat(a));
            }
            System.out.println();
        }
    }
}