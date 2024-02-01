using System;

namespace klse_screener
{
    class Program
    {
        static void Main(string[] args)
        {
            string stock_screener = new klse_screener.StockScreener().get_content();
            string warrant_screener = new klse_screener.WarrantScreener().get_content();
            Console.WriteLine(warrant_screener);
        }
    }
}
