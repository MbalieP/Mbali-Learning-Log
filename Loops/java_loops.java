public class Loops {
    public static void main(String[] args) {
        // For loop
        for (int i = 0; i < 5; i++) {
            System.out.println("Java for loop: " + i);
        }

        // While loop
        int i = 0;
        while (i < 5) {
            System.out.println("Java while loop: " + i);
            i++;
        }

        // Nested loop
        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 2; y++) {
                System.out.println("Nested loop: x=" + x + ", y=" + y);
            }
        }
    }
}
