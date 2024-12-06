import java.util.*;
import java.io.*;

// Each level increasing or decreasing
// 1 <= increse/decrease <= 3
// Can remove 1 to make safe

/**
 *  7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
 */
public class solution_part2 {
    private static Integer[] arrConcat(Integer[] arr1, Integer[] arr2) {
        Integer[] res = Arrays.copyOf(arr1, arr1.length + arr2.length);
        System.arraycopy(arr2, 0, res, arr1.length, arr2.length);
        
        return res;
    }

    private static int helper(Integer[] arr, boolean dampenerUsed) {
        Boolean isDesc = null;
        
        for (int i = 0; i+1 < arr.length; i++) {
            int diff = arr[i + 1] - arr[i];
            int absVal = Math.abs(diff);
            // System.out.println("-----" + arr[i] + "---" + arr[i+1]);
            // System.out.println("diff: " + diff);
            // System.out.println("absVal: " + absVal);
            // System.out.println("isDesc: " + isDesc);
            // System.out.println("dampenerUsed: " + dampenerUsed);
            if (absVal > 3 || absVal == 0) {
                if (!dampenerUsed) {
                    return (helper(arrConcat(Arrays.copyOfRange(arr, 0, i), Arrays.copyOfRange(arr, i + 1, arr.length)), true)) |
                    (helper(arrConcat(Arrays.copyOfRange(arr, 0, i + 1), Arrays.copyOfRange(arr, i + 2 >= arr.length ? arr.length : i + 2, arr.length)), true)) |
                    // Edge case: everything besides the first element is correct, but so is arr[0] -> arr[1] (stupid)
                    (helper(Arrays.copyOfRange(arr, 1, arr.length), true));
                }
                return 0;
            }

            if (isDesc == null) isDesc = diff != absVal;
            if ((isDesc && diff > 0) || (!isDesc && diff < 0)) {
                if (!dampenerUsed) {
                    return (helper(arrConcat(Arrays.copyOfRange(arr, 0, i), Arrays.copyOfRange(arr, i + 1, arr.length)), true)) |
                    (helper(arrConcat(Arrays.copyOfRange(arr, 0, i + 1), Arrays.copyOfRange(arr, i + 2 >= arr.length ? arr.length : i + 2, arr.length)), true)) |
                    // Edge case: everything besides the first element is correct, but so is arr[0] -> arr[1] (stupid)
                    (helper(Arrays.copyOfRange(arr, 1, arr.length), true));
                }
                return 0;
            }
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
                Integer[] report = Arrays.stream(splits).mapToInt(Integer::parseInt).boxed().toArray(Integer[]::new);

                safeReports += helper(report, false);
            }
            scanner.close();

            System.out.println(safeReports);
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
        }
    }
}