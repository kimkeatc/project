namespace odd_or_even_v1
{
    public class OddOrEven
    {
        public bool is_even(int number)
        {
            return (number % 2) == 0;
        }

        public bool is_odd(int number)
        {
            return (number % 2) == 1;
        }
    }
}
