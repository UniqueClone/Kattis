import java.util.Scanner;

public class aboveaverage {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int c = sc.nextInt();

        for(int tests = 0; tests < c; tests++) {
            int n = sc.nextInt();
            int[] results = new int[n];
            int sum = 0;

            for(int i = 0; i < n; i++) {
                results[i] = sc.nextInt();
                sum += results[i];
            }
            int avg = sum / n;
            int aboveAvg = 0;
            for(int i: results) {
                if (i > avg) {
                    aboveAvg++;
                }
            }
            double percent = (double)aboveAvg / (double)n * 100;
            System.out.printf("%.3f", percent);
            System.out.println("%");
        }
    }
}
