defmodule AdventOfCode.Solution.Year2024.Day01 do
def part1(input) do
    {list1, list2} =
      input
      |> String.trim()                     # Remove extra whitespace
      |> String.split("\n")                # Split by rows 
      |> Enum.map(fn row ->
        row
        |> String.split()
        |> Enum.map(&String.to_integer/1)
      end)
      |> Enum.unzip()
    
    IO.inspect(list1)
    
end

def part2(_input) do
end
end
