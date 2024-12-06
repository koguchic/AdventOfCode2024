// .M.S......
// ..A..MSMS.
// .M.S.MAA..
// ..A.ASMSM.
// .M.S.M....
// ..........
// S.S.S.S.S.
// .A.A.A.A..
// M.M.M.M.M.
// ..........

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

public class solution_part2 {
    private static boolean findMAS(char[][] grid, int row, int col) {
        if (row == 0 || col == 0 || row == grid.length - 1 || col == grid.length - 1) {
            return false;
        }
        if (grid[row-1][col-1] == 'M' && grid[row+1][col+1] == 'S' || grid[row-1][col-1] == 'S' && grid[row+1][col+1] == 'M') {
            if (grid[row-1][col+1] == 'M' && grid[row+1][col-1] == 'S' || grid[row-1][col+1] == 'S' && grid[row+1][col-1] == 'M') {
                return true;
            }
        }
        return false;
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
                if (grid[row][col] != 'A') {
                    continue;
                }
                xmasCount += findMAS(grid, row, col) ? 1 : 0;
            }
        }

        System.out.println("Xmas Count: " + xmasCount);
    }
}