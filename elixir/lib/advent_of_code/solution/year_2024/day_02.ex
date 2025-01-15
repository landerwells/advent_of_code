defmodule AdventOfCode.Solution.Year2024.Day02 do
  def part1(input) do
    lines = parse(input)

    lines
    |> Enum.filter(is_safe?())
    |> Enum.count()


  end

  def is_safe?(line) do


  end

  def inc_or_dec(line) do
  
    
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
