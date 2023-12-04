
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> inputs = new ArrayList<>();
        while(inputs.size() != 9){
            inputs.add(sc.nextInt());
        }
        int inputMax = Collections.max(inputs);
        int cnt = inputs.indexOf(inputMax);

        System.out.println(inputMax);
        System.out.println(cnt+1);
    }
}