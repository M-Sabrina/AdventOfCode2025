long findMaxJoltage(string bank, int digits)
{
    long maxJoltage = 0;
    var length = bank.Length;
    var startPos = 0;
    for (var exponent = digits - 1; exponent >= 0; exponent--)
    {
        for (long number = 9; number > 0; number--)
        {
            var index = bank.IndexOf(number.ToString(), startPos, length - exponent - startPos);
            if (index >= 0)
            {
                maxJoltage += number * Convert.ToInt64(Math.Pow(10, exponent));
                startPos = index + 1;
                break;

            }
        }
    }

    return maxJoltage;
}

void Part1(string file)
{
    // Store each line in array of strings
    var banks = File.ReadAllLines(file);

    long sumJoltage = 0;
    // Loop through each line
    foreach (string bank in banks)
    {
        var maxJoltage = findMaxJoltage(bank, 2);
        //Console.WriteLine(maxJoltage);
        sumJoltage += maxJoltage;
    }
    Console.WriteLine("Answer for part 1: " + sumJoltage);
}

void Part2(string file)
{
    // Store each line in array of strings
    var banks = File.ReadAllLines(file);

    long sumJoltage = 0;
    // Loop through each line
    foreach (string bank in banks)
    {
        var maxJoltage = findMaxJoltage(bank, 12);
        //Console.WriteLine(maxJoltage);
        sumJoltage += maxJoltage;
    }
    Console.WriteLine("Answer for part 2: " + sumJoltage);
}

var file = "day03_cs/input.txt";
//var file = "day03_cs/test.txt";
Part1(file);
Part2(file);
