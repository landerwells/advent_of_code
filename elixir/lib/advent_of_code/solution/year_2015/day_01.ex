defmodule AdventOfCode.Solution.Year2015.Day01 do
  def part1(input) do
    input
    |> String.graphemes()
    |> Enum.reduce(0, fn char, acc ->
      case char do
        "(" -> acc + 1
        ")" -> acc - 1
      end
    end)
  end

  # This is an example of a reduce_while
  def part2(input) do
    input
    |> String.graphemes()
    |> Enum.reduce_while({0, 0}, fn
      "(", {acc, index} -> {:cont, {acc + 1, index + 1}}
      ")", {acc, index} when acc - 1 < 0 -> {:halt, index + 1}
      ")", {acc, index} -> {:cont, {acc - 1, index + 1}}
    end)
  end
end
