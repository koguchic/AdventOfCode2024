import java.util.*;
import java.util.regex.*;
import java.io.*;

public class solution_part1 {
    public static void main(String[] args) {
        try {
            File input = new File("input.txt");
            Scanner scanner = new Scanner(input);
            
            Integer mulSum = 0;
            while (scanner.hasNextLine()) {
                String rawLine = scanner.nextLine();
                String toMatch = "(mul\\([0-9]{0,3},[0-9]{0,3}\\))";

                Pattern p = Pattern.compile(toMatch);
                Matcher m = p.matcher(rawLine);

                while (m.find()) {
                    String mulOp = rawLine.substring(m.start(), m.end());

                    String[] tmp = mulOp.split(",");
                    int x = Integer.parseInt(tmp[0].substring(4));
                    int y = Integer.parseInt(tmp[1].substring(0, tmp[1].length() - 1));

                    mulSum += x * y;
                }
            }
            scanner.close();

            System.out.println(mulSum);
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
        }
    }
}