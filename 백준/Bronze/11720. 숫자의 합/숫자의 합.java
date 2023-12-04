
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        String[] inputs = sc.nextLine().split("");
        int sum = 0;
        for(int i = 0; i < T; i++){
            sum+=Integer.parseInt(inputs[i]);
        }
        System.out.println(sum);
    }
}