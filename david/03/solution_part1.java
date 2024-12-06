/*
 * Corrupted mul
 * 
 * xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
 * parse regex
 * mul(num,num)
 * ints only
 */

import java.io.*;
import java.util.*;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
public class solution_part1 {
    private static String regex = "mul\\(([1-9][0-9]*),([1-9][0-9]*)\\)";
    public static void main(String[] args) throws FileNotFoundException {
        File f = new File(".//input.txt");
        Pattern pattern = Pattern.compile(regex);
        int result = 0;
        Scanner scanner = new Scanner(f);
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            List<MatchResult> s = pattern.matcher(line).results().collect(Collectors.toList());
            for (MatchResult match : s) {
                int left = Integer.parseInt(match.group(1));
                int right = Integer.parseInt(match.group(2));
                result += left * right;
            }
        }
        System.out.println("result: " + result);
        scanner.close();
    }
}