// ....XXMAS.
// .SAMXMS...
// ...S..A...
// ..A.A.MS.X
// XMASAMX.MM
// X.....XA.A
// S.S.S.S.SS
// .A.A.A.A.A
// ..M.M.M.MM
// .X.X.XMASX

/**
 * XMAS grid search
 * iterate through grid - initiate search for each X
 * recursive function
 */
import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class solution_part1 {
    private static String TARGET_STRING = "XMAS";
    private static int[][] DIRECTIONS = {
        {-1, -1}, // northwest
        {-1, 0}, // north
        {-1, 1}, // northeast
        {0, -1}, // west
        {0, 1}, // east
        {1, -1}, // southwest
        {1, 0}, // south
        {1, 1}, // southeast
    };

    private static int findXmas(char[][] grid, int row, int col, int targetStringIndex, int directionIndex) {
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length) {
            return 0;
        }
        if (grid[row][col] != TARGET_STRING.charAt(targetStringIndex)) { // X, M, A ,S
            return 0;
        } 
        if (targetStringIndex == TARGET_STRING.length() - 1) { // found S
            return 1;
        }
        int rowOffset = DIRECTIONS[directionIndex][0];
        int colOffset = DIRECTIONS[directionIndex][1];

        return findXmas(grid, row + rowOffset, col + colOffset, targetStringIndex + 1, directionIndex);
    }

    public static void main(String[] args) throws IOException {
        Path path = new File(".//input.txt").toPath();
        List<String> lines = Files.readAllLines(path, Charset.defaultCharset());
        char[][] grid = new char[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            grid[i] = lines.get(i).toCharArray();
        }
        int xmasCount = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                for (int i = 0; i < DIRECTIONS.length; i++) {
                    xmasCount += findXmas(grid, row, col, 0, i);
                }
            }
        }

        System.out.println("Xmas Count: " + xmasCount);
    }
}