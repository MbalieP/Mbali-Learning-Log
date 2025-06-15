
#### **Java.md** ☕  
```markdown
# Type Casting in Java

## Implicit Casting (Widening Conversion)  
Java automatically converts smaller types into larger types:
```java
int num = 10;
double result = num;  // Implicit widening conversion
System.out.println(result);  // Output: 10.0
## Explicit typecasting
double num = 10.5;
int converted = (int) num;  // Converts double to int, dropping decimals
System.out.println(converted);  // Output: 10
