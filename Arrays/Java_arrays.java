
public class Arrays {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Java 1D Array:");
        for (int num : numbers) {
            System.out.println(num);
        }
    }
}
public class MultiDimensionalArrays {
    
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };
        System.out.println("Java 2D Array Element [1][2]: " + matrix[1][2]);
    }
}
