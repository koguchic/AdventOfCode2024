


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
 * NOTE: In retrospect, only beforeMap was needed here - but afterMap needed for part 2
 * 
 * Updates
 * maintain Set of numbers we shoudln't see as we iterate through the numbers - populate based on numbers seen and above maps
 * for(num : nums) {
 *   if num is in invalidSet
 *    return false
 *   invalidSet.add(beforeMap(num))
 * }
 * return true
 */

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
public class solution_part1 {
    private static Map<Integer, Set<Integer>> beforeMap = new HashMap<>();
    private static boolean isValidUpdate(List<Integer> numbers) {
        Set<Integer> invalidIntegers = new HashSet<>();
        System.out.println(invalidIntegers.toString());
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
            } else if (line.contains(",")){ // updates
                List<Integer> numbers = Arrays.stream(line.split(","))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
                if (isValidUpdate(numbers)) {
                    result += numbers.get(numbers.size() / 2); // add the middle number
                }
            }
        }
        System.out.println("result: " + result);
    }
}