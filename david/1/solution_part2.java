// https://adventofcode.com/2024/day/1
/*
location ID

input:
3   4
4   3
2   5
1   3
3   9
3   3

similarity scores

hashmap
O(n) runtime/space
*/

import java.util.*;
import java.io.*;
public class solution_part2 {
    public static void main(String[] args) throws FileNotFoundException {
        File f = new File(".//input.txt");
        Scanner scanner = new Scanner(f);

        List<Integer> list1 = new ArrayList<>();
        Map<Integer, Integer> countMap = new HashMap<>();
        while (scanner.hasNextLine()) {
            // System.out.println(scanner.nextLine());
            String[] numbers = scanner.nextLine().split("   ");
            final Integer leftInt = Integer.parseInt(numbers[0]);
            final Integer rightInt = Integer.parseInt(numbers[1]);
            list1.add(leftInt);
            countMap.merge(rightInt, 1, Integer::sum);
        }

        Integer totalSimilarity = 0;
        for (Integer i : list1) {
            totalSimilarity += i * countMap.getOrDefault(i, 0);
        }
        System.out.println(totalSimilarity);

        scanner.close();
    }
}
