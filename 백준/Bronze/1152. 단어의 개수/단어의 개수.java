import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int answer = input.length;
        if (answer != 0) {
            if (input[0] == "" ){
                answer-=1;
            }
        }
        System.out.println(answer);
    }
}