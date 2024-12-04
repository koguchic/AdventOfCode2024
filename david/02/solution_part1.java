import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.io.*;

public class solution_part1 {
    private static boolean isValidDiff(int diff) {
        return !(diff == 0 || Math.abs(diff) > 3);
    }

    private static int isSafe(int[] arr) {
        Boolean isIncrementing = null;
        for (int i = 0; i < arr.length - 1; i++) {
            final int diff = arr[i+1] - arr[i];
            if (!isValidDiff(diff)) return 0;
            if (isIncrementing == null) {
                isIncrementing = diff > 0;
            }
            if (isIncrementing && diff < 0 || !isIncrementing && diff > 0) return 0;
        }
        return 1;
    }
    public static void main(String[] args) throws FileNotFoundException {
        File f = new File(".//input.txt");
        Scanner scanner = new Scanner(f);
        int safeCount = 0;
        while (scanner.hasNextLine()) {
            // if interview - handle empty lines, invalid lines(1 number, nonintegers)
            String s = scanner.nextLine();
            int[] array = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
            safeCount += isSafe(array);
        }

        System.out.println("Number of safe reports: " + safeCount);
        scanner.close();
    }
}