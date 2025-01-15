defmodule Mix.Tasks.Solve do
  use Mix.Task

  def run(args) do
    # case args do

    # need to parse the args

    case args do
      [year, day | _] ->
        # Convert the year and day to integers
        {year_int, _} = Integer.parse(year)
        {day_int, _} = Integer.parse(day)
        input = AdventOfCode.Input.get_input(year, day)

        IO.puts("\nSolving Advent of Code for Year: #{year}, Day: #{day}\n")

        # Dynamically build the module name from year and day
        mod =
          Module.concat(["AdventOfCode", "Solution", "Year#{year_int}", "Day#{pad_day(day_int)}"])

        if Code.ensure_loaded?(mod) do
          IO.puts("Part 1: #{apply(mod, :part1, [input])}")
          IO.puts("Part 2: #{apply(mod, :part2, [input])}")
        else
          IO.puts("Module for Year #{year} Day #{day} not found")
        end

      _ ->
        IO.puts("Usage: mix run -- <year> <day>")
    end
  end

  # Pad the day to ensure it is two digits (e.g., 01, 02, ..., 31)
  defp pad_day(day) when day < 10, do: "0#{day}"
  defp pad_day(day), do: Integer.to_string(day)
end
