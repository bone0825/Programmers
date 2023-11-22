class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[][] pad = {{0, 1}, {3, 0}, {3, 1}, {3, 2}, {2, 0}, {2, 1}, {2, 2}, {1, 0}, {1, 1}, {1, 2}, {0, 0}, {0, 2}};//0,1,2,3,4,5,6,7,8,9,*,#
        answer = getAnswer(numbers, pad, hand);
        return answer;
    }
   private static String getAnswer(int[] numbers, int[][] pad, String hand) {
        StringBuilder answer = new StringBuilder();
        int rx = pad[10][0];
        int ry = pad[10][1];
        int lx = pad[11][0];
        int ly = pad[11][1];

        int rDistance;
        int lDistance;

        for (int i : numbers) {
            rDistance = Math.abs(rx - pad[i][0]) + Math.abs(ry - pad[i][1]);
            lDistance = Math.abs(lx - pad[i][0]) + Math.abs(ly - pad[i][1]);
            if(i == 1 || i == 4 || i == 7) {
                answer.append("L");
                lx = pad[i][0];
                ly = pad[i][1];
            } else if (i == 3 || i == 6 || i == 9) {
                answer.append("R");
                rx = pad[i][0];
                ry = pad[i][1];
            }
            else{
                if (rDistance == lDistance) {
                    if (hand.equals("right")) {
                        answer.append("R");
                        rx = pad[i][0];
                        ry = pad[i][1];
                    } else {
                        answer.append("L");
                        lx = pad[i][0];
                        ly = pad[i][1];
                    }
                } else if (rDistance > lDistance) {
                    answer.append("L");
                    lx = pad[i][0];
                    ly = pad[i][1];
                } else if (rDistance < lDistance) {
                    answer.append("R");
                    rx = pad[i][0];
                    ry = pad[i][1];
                }
            }
        }
        return answer.toString();
    }
}