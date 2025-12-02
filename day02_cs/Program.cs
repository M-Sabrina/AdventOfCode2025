static void Part1(string file)
{
    // To read a text file line by line
    if (File.Exists(file))
    {
        long result = 0;

        var input = File.ReadAllText(file);
        var ranges = input.Split(",");

        foreach (string range in ranges)
        {
            var minMax = range.Split("-");
            long min = Convert.ToInt64(minMax[0]);
            long max = Convert.ToInt64(minMax[1]);

            long count = min;
            while (count <= max)
            {
                string number = count.ToString();
                int length = number.Length;
                if (length % 2 == 0)
                {
                    string first = number.Substring(0, length / 2);
                    string second = number.Substring(length / 2);
                    if (first == second)
                    {
                        //Console.WriteLine(first + " " + second);
                        result += count;
                    }
                }
                count += 1;
            }
        }

        Console.WriteLine("Answer for part 1: " + result);
    }
}


var file = "day02_cs/input.txt";
Part1(file);
