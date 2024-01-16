using System;

namespace factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            factorial.Factorial factorial_instance = new factorial.Factorial();
            int number = 0;
            int result = factorial_instance.generate(number: number);
            Console.WriteLine($"Factorial of {number}! is {result}");
        }
    }
}
