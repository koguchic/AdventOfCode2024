import java.util.*;
import java.io.*;

public class solution_part2 {
    public static void main(String[] args) {
        List<Integer> left = new ArrayList<>();
        Map<Integer, Integer> right = new HashMap<Integer, Integer>();

        //#region Parse input
        try {
            File input = new File("input.txt");
            System.out.println(input.getAbsolutePath());
            Scanner scanner = new Scanner(input);
            
            while (scanner.hasNextLine()) {
                String tmp = scanner.nextLine();

                String[] split = tmp.split("   ");
                left.add(Integer.parseInt(split[0]));
                right.merge(Integer.parseInt(split[1]), 1, (a, b) -> a + 1);
            }
            scanner.close();
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
        }
        //#endregion

        //#region Look through L and multiple by count in R
        Integer sum = 0;
        
        for (int i : left) {
            sum += i * right.getOrDefault(i, 0);
        }
        //#endregion

        System.out.println(sum);
    }
}