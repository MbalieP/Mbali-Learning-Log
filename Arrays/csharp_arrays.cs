
using System;

class Arrays {
    static void Main() {
        int[] numbers = {1, 2, 3, 4, 5};
        Console.WriteLine("C# 1D Array:");
        foreach (int num in numbers) {
            Console.WriteLine(num);
        }
    }
}
using System;

class MultiDimensionalArrays {
    static void Main() {
        int[,] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };
        Console.WriteLine("C# 2D Array Element [1,2]: " + matrix[1, 2]);
    }
}

