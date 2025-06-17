class Animal {
    public void speak() {
        System.out.println("The animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("The dog barks.");
    }
}

class Calculator {
    // Method Overloading
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}

class Person {
    // Getter and Setter
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

public class JavaMethods {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.speak();

        Calculator calc = new Calculator();
        System.out.println(calc.add(5, 10));
        System.out.println(calc.add(5.5, 4.5));

        Person p = new Person();
        p.setName("Mbali");
        System.out.println(p.getName());
    }
}

