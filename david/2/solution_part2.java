import java.util.*;
import java.util.stream.IntStream;
import java.io.*;

/*
    Part 1: Regular reports - all incrementing/or decrementing with abs(diff) < 4
 * Part 2: dampened reports - one number can be removed
 * O(N^2) time: Evaluate each subarray with one value omitted
 * 
 * To do in one pass: what does it mean to remove a number?
 * The pattern should be safe with the number removed (e.g. list[0] list[2] list [3] list[4])
 * Remove the first found unsafe pattern and continue evaluating
 * Q: Can the correct pattern to remove be the non-first found unsafe pattern?
 * A: No, because the string would have two unsafe patterns - always unsafe
 * Q: Can the pattern to remove be a safe pattern?
 * A: Yes, if the direction of the pattern changes
 * 
 * 
 * Sample: 7  8  4  1  0 -> remove the 8
 * Diffs:   1 -4 -3 -1
 * Sample: 1 7 8 9 10 -> remove the 1
 * Diffs: 6 1 1 1
 * Sample: 5 1 2 1 0 -> remove the first 1
 * Diffs: -4 1 -1 -1
 * Sample 6 4 2 2 0 -> remove either 2
 * Diffs: -2 -2 0 -2 
 * 
 * Sample 5 5 5 5 5
 * 1. Do single pass to populate diff array, increment/decrement count
 * 2. Incrementing = 1, decrementing = -1 ; abs(incDecCount) must be >= 2 or else invalid
 * 3. Pass through diff array until invalid diff found
 * 4a. If diffs[i] + diffs[i+1] is valid, a valid sequence exists (drop the right #) 
 * 4b. If diffs[i+1] is valid, a valid sequence exists (drop the left #)
 * 5. Therefore, if 4a or 4b is true, continue to evaluate
 * 
 * n = # of reports, m = length of report
 * O(n * (2m - 1)) = O(nm) time - iterate through array and diff array
 * O(m) space for diff array

 */

public class solution_part2 {
    private static boolean isValidDiff(int diff) {
        return !(diff == 0 || Math.abs(diff) > 3);
    }

    private static int isSafeWithDampenBruteForce(int[] arr) {
        for (int indexToSkip = 0; indexToSkip < arr.length; indexToSkip++) {
            int[] left = Arrays.copyOfRange(arr, 0, indexToSkip);
            int[] right = Arrays.copyOfRange(arr, indexToSkip + 1, arr.length);
            int [] subarray = IntStream.concat(IntStream.of(left), IntStream.of(right)).toArray();
            if (isSafe(subarray) == 1) {
                return 1;
            } 
        }
        return 0;
    }
    private static int isSafeWithDampen(int[] arr) {

        /*
         * Invalid diff values when more than one of the following happens
         * - Direction changes more than once
         * - Diff is zero more than once
         * 
         */
        int invalidDiffCount = 0;
        Boolean skipUsed = false;
        Boolean isIncrementing1 = null;
        int[] diffs = new int[arr.length - 1];
        for (int i = 0; i < arr.length - 1; i++) {
            final int diff = arr[i+1] - arr[i];
            diffs[i] = diff;
            if(!isValidDiff(diff)) {
                invalidDiffCount++;
            } else {
                if (isIncrementing1 != null) {
                    invalidDiffCount += (isIncrementing1 == diff > 0) ? 0 : 1;
                }
                isIncrementing1 = diff > 0 ? true : false;
            }            
        }
        if(invalidDiffCount > 1) return 0; // too many invalids
        for (int i = 0; i < diffs.length - 1; i++) {
            if(!isValidDiff(diffs[i])) {
                if (skipUsed) {
                    return 0;
                }                
                if (!isValidDiff(diffs[i] + diffs[i+1]) &&
                        !isValidDiff(diffs[i+1])) { // one condition has to be valid to be able to drop a number
                    return 0;
                }
                skipUsed = true;
            }
        }
        return 1;
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
        int safeWithDampenCount = 0;
        int safeWithDampenCountBruteForce = 0;
        while (scanner.hasNextLine()) {
            // if interview - handle empty lines, invalid lines(1 number, nonintegers)
            String s = scanner.nextLine();
            int[] array = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
            safeCount += isSafe(array);
            safeWithDampenCountBruteForce += isSafeWithDampenBruteForce(array);
            safeWithDampenCount += isSafeWithDampen(array);
        }

        System.out.println("Number of safe reports: " + safeCount);
        System.out.println("Number of safe dampened reports (Brute Force): " + safeWithDampenCountBruteForce);
        System.out.println("Number of safe dampened reports: " + safeWithDampenCount);

        scanner.close();
    }
}