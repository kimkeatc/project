using System.Text.RegularExpressions;
using System.Threading.Tasks;  // https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=net-7.0
using System.Net.Http;  // https://learn.microsoft.com/en-us/dotnet/api/system.net.http?view=net-7.0
using HtmlAgilityPack;  // https://html-agility-pack.net/documentation

namespace klse_screener
{
    public class StockScreener()
    {
        public string get_content()
        {
            string html_content = get_html_content();
            string content = new Miscellaneous().process_html_content(html_content);
            return content;
        }

        public string get_html_content()
        {
            string content = "";
            using (HttpClient client = new HttpClient())
            {
                client.DefaultRequestHeaders.UserAgent.ParseAdd(input: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36");
                HttpResponseMessage response = client.GetAsync(requestUri: "https://www.klsescreener.com/v2/screener/quote_results").Result;
                if (response.IsSuccessStatusCode)
                {
                    content = response.Content.ReadAsStringAsync().Result;
                }
            }
            return content;
        }
    }

    public class WarrantScreener()
    {
        public string get_content()
        {
            string html_content = get_html_content();
            string content = new Miscellaneous().process_html_content(html_content);
            return content;
        }

        public string get_html_content()
        {
            string content = "";
            using (HttpClient client = new HttpClient())
            {
                client.DefaultRequestHeaders.UserAgent.ParseAdd(input: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36");
                HttpResponseMessage response = client.GetAsync(requestUri: "https://www.klsescreener.com/v2/screener_warrants/quote_results").Result;
                if (response.IsSuccessStatusCode)
                {
                    content = response.Content.ReadAsStringAsync().Result;
                }
            }
            return content;
        }
    }

    public class Miscellaneous()
    {
        public string process_html_content(string html_content)
        {
            HtmlDocument html_document = new HtmlDocument();
            html_document.LoadHtml(html_content);

            List<string> content = new List<string>();
            foreach (HtmlNode table in html_document.DocumentNode.SelectNodes("/div[*]/table"))
            {
                foreach (HtmlNode row in table.SelectNodes("thead|tbody"))
                {
                    foreach (HtmlNode r in row.SelectNodes("tr"))
                    {
                        List<string> line = new List<string>();
                        foreach (HtmlNode cell in r.SelectNodes("th|td"))
                        {
                            string text = cell.InnerText.Trim();
                            text = Regex.Replace(text, @"\s+", " ");

                            line.Add(text);
                        }
                        string l = string.Join(",", line);
                        content.Add(l);
                    }
                }
            }
            string c = string.Join("\n", content);
            return c;
        }
    }
}