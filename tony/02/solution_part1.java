import java.util.*;
import java.io.*;

// Each level increasing or decreasing
// 1 <= increse/decrease <= 3
public class solution_part1 {
    private static int helper(int[] arr) {
        Boolean isDesc = null;
        for (int i = 0; i+1 < arr.length; i++) {
            int diff = arr[i + 1] - arr[i];
            int absVal = Math.abs(diff);
            if (absVal > 3 || absVal == 0) return 0;

            if (isDesc == null) isDesc = diff != absVal;
            if ((isDesc && diff > 0) || (!isDesc && diff < 0)) return 0;
        }
        return 1;
    }
    public static void main(String[] args) {
        try {
            File input = new File("input.txt");
            Scanner scanner = new Scanner(input);
            
            Integer safeReports = 0;
            while (scanner.hasNextLine()) {
                String[] splits = scanner.nextLine().split(" ");
                int[] report = Arrays.stream(splits).mapToInt(Integer::parseInt).toArray();
                
                // Boolean isSafe = true;
                // int prevDiff = report[1] - report[0];
                // Boolean isDesc = prevDiff < 0;
                // for (int i = 1; i+1 < report.length; i++) {
                //     int diff = report[i + 1] - report[i];
                //     int absVal = Math.abs(diff);
                //     isSafe = absVal <= 3 && absVal != 0 && (isDesc ? diff < 0 : diff > 0);
                // }
                // if (isSafe) safeReports++;

                safeReports += helper(report);
            }
            scanner.close();

            System.out.println(safeReports);
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
        }
    }
}