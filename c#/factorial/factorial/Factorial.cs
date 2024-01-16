using System.Linq;

namespace factorial
{
    public class Factorial
    {
        public int generate(int number)
        {
            int result = 1;
            foreach (int value in Enumerable.Range(start: 1, count: number))
            {
                result *= value;
            }
            return result;
        }
    }
}
