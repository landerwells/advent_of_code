defmodule AdventOfCode.Solution.Year2017.Day07Test do
  use ExUnit.Case, async: true

  import AdventOfCode.Solution.Year2017.Day07

  setup do
    [
      input: """
      pbga (66)
      xhth (57)
      ebii (61)
      havc (66)
      ktlj (57)
      fwft (72) -> ktlj, cntj, xhth
      qoyq (66)
      padx (45) -> pbga, havc, qoyq
      tknk (41) -> ugml, padx, fwft
      jptl (61)
      ugml (68) -> gyxo, ebii, jptl
      gyxo (61)
      cntj (57)
      """
    ]
  end

  @tag :skip
  test "part1", %{input: input} do
    result = part1(input)

    assert result == "tknk"
  end

  @tag :skip
  test "part2", %{input: input} do
    result = part2(input)

    assert result
  end
end
