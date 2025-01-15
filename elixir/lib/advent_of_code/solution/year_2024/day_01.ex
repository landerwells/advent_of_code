defmodule AdventOfCode.Solution.Year2024.Day01 do
  def part1(input) do
    {list1, list2} = parse(input)

    list1 =
      list1
      |> Enum.sort()

    list2 =
      list2
      |> Enum.sort()

    zipped = Enum.zip(list1, list2)

    zipped
    |> Enum.map(fn x -> distance(x) end)
    |> Enum.sum()
  end

  def parse(input) do
    input
    |> String.trim()
    |> String.split()
    |> Enum.map(fn x -> String.to_integer(x) end)
    # Group into pairs of 2 elements
    |> Enum.chunk_every(2)
    # Convert each pair to a tuple
    |> Enum.map(&List.to_tuple/1)
    |> Enum.unzip()
  end

  def similarity_score(num, map) do
    Map.get(map, num, 0) * num
  end

  def distance(tuple) do
    abs(elem(tuple, 0) - elem(tuple, 1))
  end

  def frequency_map(list) do
    Enum.reduce(list, %{}, fn element, acc ->
      Map.update(acc, element, 1, &(&1 + 1))
    end)
  end

  def part2(input) do
    {list1, list2} = parse(input)

    map = frequency_map(list2)
    # need to create the map based out of 

    list1
    |> Enum.map(fn x -> similarity_score(x, map) end)
    |> Enum.sum()
  end
end
