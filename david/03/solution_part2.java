/*
 * Corrupted mul part 2
 *  do() .... dont() .... do() ...
 * 
 * match for pattern / dont() / do()

 */

import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class solution_part2 {
    private static String regex = "mul\\(([1-9][0-9]*),([1-9][0-9]*)\\)";
    private static String doString = "do()";
    private static String dontString = "don't()";
    private static String doRegex = "do\\(\\)";
    private static String dontRegex = "don't\\(\\)";
    private static String combinedRegex = regex + "|" + dontRegex + "|" + doRegex;

    public static void main(String[] args) throws FileNotFoundException {
        String line = new Scanner(new File(".//input.txt")).useDelimiter("\\Z").next();
        Pattern combinedPattern = Pattern.compile(combinedRegex);
        int result = 0;
        boolean enabled = true; // assuming enablement doesn't change between input lines
        Matcher combinedMatcher = combinedPattern.matcher(line);

        while (combinedMatcher.find()) {
            System.out.println(combinedMatcher.group());
            if (combinedMatcher.group().equals(doString)) {
                enabled = true;
            } else if (combinedMatcher.group().equals(dontString)) {
                enabled = false;
            } else if (enabled) {
                int left = Integer.parseInt(combinedMatcher.group(1));
                int right = Integer.parseInt(combinedMatcher.group(2));
                result += left * right;
            }
        }
        System.out.println("final result: " + result);
    }
}