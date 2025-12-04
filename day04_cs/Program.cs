class Program
{
    static bool CheckSurroundings(int[,] map, int row, int col, int rows, int cols)
    {
        int count = 0;
        if (row - 1 >= 0 && col - 1 >= 0 && map[row - 1, col - 1] == 1) count++;
        if (row - 1 >= 0 && map[row - 1, col] == 1) count++;
        if (row - 1 >= 0 && col + 1 < cols && map[row - 1, col + 1] == 1) count++;
        if (col - 1 >= 0 && map[row, col - 1] == 1) count++;
        if (col + 1 < cols && map[row, col + 1] == 1) count++;
        if (row + 1 < rows && col - 1 >= 0 && map[row + 1, col - 1] == 1) count++;
        if (row + 1 < rows && map[row + 1, col] == 1) count++;
        if (row + 1 < rows && col + 1 < cols && map[row + 1, col + 1] == 1) count++;
        return count < 4;
    }

    static void Part1(string file)
    {
        var lines = File.ReadAllLines(file);
        int rows = lines.Length;
        int cols = lines[0].Length;
        int[,] map = new int[rows, cols];
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (lines[r][c] == '@') map[r, c] = 1;
            }
        }
        int countAccessible = 0;
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                if (map[row, col] == 1 && CheckSurroundings(map, row, col, rows, cols))
                {
                    countAccessible++;
                }
            }
        }
        Console.WriteLine($"Answer for part 1: {countAccessible}");
    }

    static void Part2(string file)
    {
        var lines = File.ReadAllLines(file);
        int rows = lines.Length;
        int cols = lines[0].Length;
        int[,] map = new int[rows, cols];
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (lines[r][c] == '@') map[r, c] = 1;
            }
        }
        int countAccessible = 0;
        var accessiblePos = new List<(int, int)>();
        while (true)
        {
            bool hasAccessible = false;
            for (int row = 0; row < rows; row++)
            {
                for (int col = 0; col < cols; col++)
                {
                    if (map[row, col] == 1 && CheckSurroundings(map, row, col, rows, cols))
                    {
                        countAccessible++;
                        accessiblePos.Add((row, col));
                        hasAccessible = true;
                    }
                }
            }
            foreach (var pos in accessiblePos)
            {
                map[pos.Item1, pos.Item2] = 0;
            }
            accessiblePos.Clear();
            if (!hasAccessible) break;
        }
        Console.WriteLine($"Answer for part 2: {countAccessible}");
    }

    static void Main(string[] args)
    {
        string file = "day04_py/input.txt";
        // string file = "day04_py/test.txt";
        Part1(file);
        Part2(file);
    }
}
