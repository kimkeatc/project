namespace odd_or_even_v2
{
    public class OddOrEven
    {
        public bool is_even(int number)
        {
            return (number & 1) == 0;
        }

        public bool is_odd(int number)
        {
            return (number & 1) == 1;
        }
    }
}
