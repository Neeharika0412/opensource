import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int X = scanner.nextInt();
            int N = scanner.nextInt();
            int pointsPerTestCase = X / 10;
            int score = pointsPerTestCase * N;
            System.out.println(score);
        }
        scanner.close();
    }
}
