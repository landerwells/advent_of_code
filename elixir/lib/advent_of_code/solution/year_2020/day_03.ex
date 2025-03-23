defmodule AdventOfCode.Solution.Year2020.Day03 do
  def part1(input) do
    traverse(0, 3, 0, 1, parse(input), 0)
  end

  def traverse(x, dx, y, dy, grid, tree_counter) do
    # Base case: if we've reached beyond the grid, return the tree counter
    if y >= length(grid) do
      tree_counter
    else
      char = Enum.at(grid, y) |> Enum.at(x)

      new_tree_counter = if char == "#", do: tree_counter + 1, else: tree_counter

      new_x = rem(x + dx, grid |> List.first() |> length())
      new_y = y + dy

      # Recursive case
      traverse(new_x, dx, new_y, dy, grid, new_tree_counter)
    end
  end

  def parse(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&String.codepoints/1)
  end

  def part2(input) do
    [{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}]
    |> Enum.map(fn {dx, dy} ->
      traverse(0, dx, 0, dy, parse(input), 0)
    end)
    |> Enum.reduce(1, &*/2)
  end
end
