import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        List<Integer> weights = new ArrayList<>();
        List<Integer> values = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            weights.add(sc.nextInt());
            values.add(sc.nextInt());
        }

        int[][] dp = new int[n + 1][k + 1];

        for (int i = 1; i <= n; i++) {
            int weight = weights.get(i - 1);
            int value = values.get(i - 1);

            for (int j = 1; j <= k; j++) {
                if (j < weight) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight] + value);
                }
            }
        }

        System.out.println(dp[n][k]);
    }
}
