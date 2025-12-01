

static void Part1(string file)
{
    // To read a text file line by line
    if (File.Exists(file))
    {
        // Store each line in array of strings
        string[] lines = File.ReadAllLines(file);

        int num = 50;
        int password = 0;

        // Loop through each line
        foreach (string ln in lines)
        {
            string dist = ln.Substring(1);
            int rot = Convert.ToInt32(dist);
            if (ln[0] == 'L')
            {
                rot = -rot;
            }
            num = (num + rot) % 100;
            if (num == 0)
            {
                password += 1;
            }
        }

        Console.WriteLine("Password for part 1: " + password);
    }
}

static void Part2(string file)
{
    // To read a text file line by line
    if (File.Exists(file))
    {
        // Store each line in array of strings
        string[] lines = File.ReadAllLines(file);

        int num = 50;
        int password = 0;

        // Loop through each line
        foreach (string ln in lines)
        {
            string dist = ln.Substring(1);
            int rot = Convert.ToInt32(dist);
        }

        Console.WriteLine("Password for part 2: " + password);
    }

}

string file = "day01_cs/input.txt";
Part1(file);
Part2(file);
