using System;

class Animal
{
    public virtual void Speak()
    {
        Console.WriteLine("The animal makes a sound.");
    }
}

class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The dog barks.");
    }
}

class Calculator
{
    // Method Overloading
    public int Add(int a, int b) => a + b;
    public double Add(double a, double b) => a + b;
}

class Person
{
    // Getter and Setter using properties
    public string Name { get; set; }
}

class Program
{
    static void Main()
    {
        Dog dog = new Dog();
        dog.Speak();

        Calculator calc = new Calculator();
        Console.WriteLine(calc.Add(5, 10));
        Console.WriteLine(calc.Add(5.5, 4.5));

        Person p = new Person();
        p.Name = "Mbali";
        Console.WriteLine(p.Name);
    }
}

