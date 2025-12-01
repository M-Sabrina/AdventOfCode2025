using System;

namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            string file = @"input.txt";

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

                Console.WriteLine("Password: " + password);
            }
        }
    }
}
