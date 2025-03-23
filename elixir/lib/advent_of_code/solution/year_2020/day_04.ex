defmodule AdventOfCode.Solution.Year2020.Day04 do
  def part1(input) do
    passports = input |> String.split("\n\n")

    passports
    |> Enum.count(&valid_passport?/1)
  end

  def valid_passport?(passport) do
    fields =
      passport
      |> String.split()
      |> Enum.map(fn field ->
        [key, value] = String.split(field, ":")
        {key, value}
      end)
      |> Enum.into(%{})

    to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    Enum.all?(to_check, fn key -> Map.has_key?(fields, key) end)
  end

  def part2(_input) do
  end
end
