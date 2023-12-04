import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        List<Integer> inputs = new ArrayList<>();
        for(int i =0; i < T; i++){
            inputs.add(sc.nextInt());
        }
        System.out.println(Collections.min(inputs)+ " " + Collections.max(inputs));
    }
}