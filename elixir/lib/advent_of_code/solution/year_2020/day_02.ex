defmodule AdventOfCode.Solution.Year2020.Day02 do
  def part1(input) do
    input
    # Split input into lines, ignoring empty lines
    |> String.split("\n", trim: true)
    |> Enum.map(fn line ->
      [range, letter_colon, password] = String.split(line)
      <<letter, ?:>> = letter_colon

      # Extract range values
      [[at_least_str], [at_most_str]] = Regex.scan(~r/\d+/, range)
      at_least = String.to_integer(at_least_str)
      at_most = String.to_integer(at_most_str)

      # Check validity
      is_valid?(at_least..at_most, <<letter>>, password)
    end)
    # Count valid passwords
    |> Enum.count(& &1)
  end

  def is_valid?(range, letter, password) do
    frequency_map =
      password
      |> String.graphemes()
      |> Enum.frequencies()

    occurrences = Map.get(frequency_map, letter, 0)
    occurrences in range
  end

  def is_valid2?(x, y, letter, password) do
    # Returns true if letter is at position x or y in password

    a = letter == password |> String.graphemes() |> Enum.at(x - 1)
    b = letter == password |> String.graphemes() |> Enum.at(y - 1)

    xor(a, b)
  end

  def xor(a, b) do
    (a and not b) or (not a and b)
  end

  def part2(input) do
    input
    # Split input into lines, ignoring empty lines
    |> String.split("\n", trim: true)
    |> Enum.map(fn line ->
      [range, letter_colon, password] = String.split(line)
      <<letter, ?:>> = letter_colon

      # Extract range values
      [[at_least_str], [at_most_str]] = Regex.scan(~r/\d+/, range)
      at_least = String.to_integer(at_least_str)
      at_most = String.to_integer(at_most_str)

      # Check validity
      is_valid2?(at_least, at_most, <<letter>>, password)
    end)
    # Count valid passwords
    |> Enum.count(& &1)
  end
end
