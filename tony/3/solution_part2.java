import java.util.*;
import java.util.regex.*;
import java.io.*;

public class solution_part2 {
    public static void main(String[] args) {
        try {
            File input = new File("input.txt");
            Scanner scanner = new Scanner(input);
            
            Integer mulSum = 0;
            boolean enabled = true;
            int lastEnable = 0;
            int lastDisable = 0;

            Pattern pEnable = Pattern.compile("(do\\(\\))");
                Pattern pDisable = Pattern.compile("(don't\\(\\))");
                Pattern pMulOp = Pattern.compile("(mul\\([0-9]{0,3},[0-9]{0,3}\\))");

            while (scanner.hasNextLine()) {
                String rawLine = scanner.nextLine();
                boolean newLine = true;
                
                Matcher mMulOp = pMulOp.matcher(rawLine);
                Queue<Integer> enabledIndexes = new LinkedList<Integer>();
                Matcher mEnable = pEnable.matcher(rawLine);
                while (mEnable.find()) {
                    enabledIndexes.add(mEnable.end());
                }
                Queue<Integer> disabledIndexes = new LinkedList<Integer>();
                Matcher mDisable = pDisable.matcher(rawLine);
                while (mDisable.find()) {
                    disabledIndexes.add(mDisable.end());
                }

                while (mMulOp.find()) {
                    int mulOpStartIndex = mMulOp.start();
                    System.out.println("mulOpStartIndex: " + mulOpStartIndex);
                    String mulOp = mMulOp.group();
                    System.out.println("mulOp: " + mulOp);
                    while (enabledIndexes.size() > 0 && enabledIndexes.peek() <= mulOpStartIndex) {
                        lastEnable = enabledIndexes.poll();
                        if (newLine) {
                            lastDisable = 0;
                            newLine = false;
                        }
                    }
                    while (disabledIndexes.size() > 0 && disabledIndexes.peek() <= mulOpStartIndex) {
                        lastDisable = disabledIndexes.poll();
                        if (newLine) {
                            lastEnable = 0;
                            newLine = false;
                        }
                    }

                    enabled = lastEnable >= lastDisable;

                    System.out.println(String.format("Last enabled index: %d, last disabled index: %d", lastEnable, lastDisable));
                    System.out.println("Enabled: " + enabled);

                    if (enabled) {
                        String[] tmp = mulOp.split(",");
                        int x = Integer.parseInt(tmp[0].substring(4));
                        int y = Integer.parseInt(tmp[1].substring(0, tmp[1].length() - 1));
                        
                        System.out.println(String.format("x: %d, y:%d", x, y));
                        mulSum += x * y;
                    }
                }
            }
            scanner.close();

            System.out.println(mulSum);
        } catch (FileNotFoundException err) {
            System.out.println("File not found");
        }
    }
}