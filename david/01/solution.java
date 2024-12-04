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

sum of pair distances with each pair being the corresponding nth smallest number in its list

two minheaps
O(n) runtime/space
*/

import java.util.*;
import java.io.*;
public class solution {

    private static PriorityQueue<Integer> createMinHeap(List<Integer> inputList) {
        return new PriorityQueue<>(inputList);
    }
    
    public static void main(String[] args) throws FileNotFoundException {
        File f = new File(".//input.txt");
        Scanner scanner = new Scanner(f);

        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        while (scanner.hasNextLine()) {
            // System.out.println(scanner.nextLine());
            String[] numbers = scanner.nextLine().split("   ");
            list1.add(Integer.parseInt(numbers[0]));
            list2.add(Integer.parseInt(numbers[1]));
        }

        PriorityQueue<Integer> pq1 = createMinHeap(list1);
        PriorityQueue<Integer> pq2 = createMinHeap(list2);
        Integer totalDistance = 0;
        while (!pq1.isEmpty()) {
            totalDistance += Math.abs(pq1.poll() - pq2.poll());
        }
        System.out.println(totalDistance);

        scanner.close();
    }
}
