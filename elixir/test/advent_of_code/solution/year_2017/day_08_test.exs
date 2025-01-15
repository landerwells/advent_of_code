defmodule AdventOfCode.Solution.Year2017.Day08Test do
  use ExUnit.Case, async: true

  import AdventOfCode.Solution.Year2017.Day08

  setup do
    [
      input: """
      b inc 5 if a > 1
      a inc 1 if b < 5
      c dec -10 if a >= 1
      c inc -20 if c == 10
      """
    ]
  end

  @tag :skip
  test "part1", %{input: input} do
    result = part1(input)

    assert result == 1
  end

  @tag :skip
  test "part2", %{input: input} do
    result = part2(input)

    assert result
  end
end
