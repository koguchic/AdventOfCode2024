import java.util.*;
import java.io.*;

public class solution_part1 {
    public static void main(String[] args) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        //#region Parse input
        try {
            File input = new File("input.txt");
            Scanner scanner = new Scanner(input);
            
            while (scanner.hasNextLine()) {
                String tmp = scanner.nextLine();

                String[] split = tmp.split("   ");
                left.add(Integer.parseInt(split[0]));
                right.add(Integer.parseInt(split[1]));
            }
            scanner.close();
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
            err.printStackTrace();
        }
        //#endregion

        //#region Sort then find diff
        Collections.sort(left);
        Collections.sort(right);

        Integer sum = 0;
        Iterator<Integer> lIterator = left.iterator();
        Iterator<Integer> rIterator = right.iterator();

        while (lIterator.hasNext()) {
            sum += Math.abs(lIterator.next() - rIterator.next());
        }
        ////#endregion

        System.out.println(sum);
    }
}