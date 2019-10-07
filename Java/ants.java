import java.util.*;
import java.lang.Math;

public class ants {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int tests = 0; tests < t; tests++) {
            int len = sc.nextInt();
            int noOfAnts = sc.nextInt();
            int min = 0;
            int[] ants = new int[noOfAnts];
            for(int i = 0; i < noOfAnts; i++) {
                ants[i] = sc.nextInt();
                min = Math.max(Math.min(ants[i], len - ants[i]), min);
            }

            Arrays.sort(ants);

            int[] longestPossible = new int[4];
            longestPossible[0] = ants[0];
            longestPossible[1] = ants[noOfAnts-1];
            longestPossible[2] = len - ants[0];
            longestPossible[3] = len - ants[noOfAnts-1];

            Arrays.sort(longestPossible);

            System.out.println(min + " " + longestPossible[3]);
        }
    }
}
