// 47|53
// 97|13
// 97|61
// 97|47
// 75|29
// 61|13
// 75|53
// 29|13
// 97|29
// 53|29
// 61|53
// 97|53
// 61|29
// 47|13
// 75|47
// 97|75
// 47|61
// 75|61
// 47|29
// 75|13
// 53|13

// 75,47,61,53,29
// 97,61,53,29,13
// 75,29,13
// 75,97,47,61,53
// 61,13,29
// 97,13,75,29,47

/**
 * Rules
 * Two Map<Integer, Set<Integer>s - beforeMap and afterMap (numbers that should be before/after the key)
 * 
 * Updates
 * maintain Set of numbers we shoudln't see as we iterate through the numbers - populate based on numbers seen and above maps
 * for(num : nums) {
 *   if num is in invalidSet
 *    return false
 *   invalidSet.add(beforeMap(num))
 * }
 * return true
 * 
 * 
 * Part 2
 * Fix the wrong updates
 * assume all rules are compatible with each other
 * To Fix an incorrect update:
 * 
 * One pass?
 * Given A|B - incorrect update means A was found after B
 * To fix, move B before A
 * 
 * Test case #1
 * A|B A|C, C,A,B
 * 1. C found
 * 2. A found, invalid - move to before C
 *   A, C, B
 * 3. Now valid
 *
 * Test case #2

* A|B A|C B|C     C,B,A
* 1. C found
* 2. B found, invalid, move B before C 
* 3. A found, invalid
* 4. move to before A? before B?
* 
* 
* Based on the problem statement(sum of fixed update middle numbers), there must be a single right ordering for all rules (otherwise answer can change)
* 
* No need to actually fix the array - just check how many numbers are before & after it
* O(n * m^2) time where n = # of rows, m = length of update
* O(n + m) space
*/

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
public class solution_part2 {
    private static Map<Integer, Set<Integer>> beforeMap = new HashMap<>();
    private static Map<Integer, Set<Integer>> afterMap = new HashMap<>();

    // in an interview, would merge this function with isValidUpdate to do it in one pass
    private static int fixUpdateAndGetMiddleNum(List<Integer> numbers) {
        // check how many should be before and how many should be after
        for (Integer number: numbers) {
            Set<Integer> beforeSet = new HashSet<>(beforeMap.get(number));
            Set<Integer> afterSet = new HashSet<>(afterMap.get(number));

            // only keep the numbers that are in the current update
            beforeSet.retainAll(numbers); 
            afterSet.retainAll(numbers);
            if(beforeSet.size() == afterSet.size()) { // same count of numbers before and after this number
                return number;
            }
        }
        //shouldn't be hit
        System.out.println("No middle number found! Update was " + numbers.toString());
        return 0;
    }
    private static boolean isValidUpdate(List<Integer> numbers) {
        Set<Integer> invalidIntegers = new HashSet<>();
        for (Integer number : numbers) {
            if (invalidIntegers.contains(number)) {
                return false;
            }
            if (beforeMap.containsKey(number)) { 
                invalidIntegers.addAll(beforeMap.get(number));
            }
        }
        return true;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File f = new File(".//input.txt");
        Scanner s = new Scanner(f);
        int result = 0;

        while (s.hasNextLine()) {
            String line = s.nextLine();
            if (line.contains("|")) { // rules
                List<Integer> rule = Arrays.stream(line.split("\\|"))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
                Integer left = rule.get(0);
                Integer right = rule.get(1);

                // populate beforeMap - values must come before key
                if (!beforeMap.containsKey(right)) {
                    Set<Integer> beforeSet = new HashSet<>(Arrays.asList(left));
                    beforeMap.put(right, beforeSet);
                } else {
                    beforeMap.get(right).add(left);
                }

                // populate afterMap - values must be after key
                if (!afterMap.containsKey(left)) {
                    Set<Integer> afterSet = new HashSet<>(Arrays.asList(right));
                    afterMap.put(left, afterSet);
                } else {
                    afterMap.get(left).add(right);
                }
            } else if (line.contains(",")){ // updates
                List<Integer> numbers = Arrays.stream(line.split(","))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
                if (!isValidUpdate(numbers)) { // now we only care about the invalid rows
                result += fixUpdateAndGetMiddleNum(numbers);
                }
            }
        }
        System.out.println("result: " + result);
        s.close();
    }
}