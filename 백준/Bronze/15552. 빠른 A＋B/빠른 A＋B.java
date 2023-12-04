import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            String[] inputs = br.readLine().split(" ");
            int sum =0;
            for(int j = 0; j < inputs.length; j++){
                sum += Integer.parseInt(inputs[j]);
            }
            bw.write(String.valueOf(sum));
            bw.newLine();
        }
        bw.flush();
    }
}