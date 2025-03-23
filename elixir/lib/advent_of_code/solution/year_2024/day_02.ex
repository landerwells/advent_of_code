defmodule AdventOfCode.Solution.Year2024.Day02 do
  def part1(input) do
    lines = parse(input)

    new_lines =
      lines
      |> Enum.map(fn line ->
        line
        # Pair each element with the next
        |> Enum.zip(tl(line))
        # Compute the difference
        |> Enum.map(fn {a, b} -> b - a end)
      end)

    IO.puts(new_lines)
  end

  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(fn line ->
      line
      |> String.split()
      |> Enum.map(&String.to_integer/1)
    end)
  end

  def part2(_input) do
  end
end
