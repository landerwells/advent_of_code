defmodule AdventOfCode.Input do
  def get_input(year, day) do

    file = Path.join(cache_dir(), "/#{year}/#{day}")

    if !in_cache?(year, day) do
      store_in_cache!(year, day, download!(year, day))
    end

    File.read!(file)
  end

  defp store_in_cache!(year, day, input) do
    path = cache_path(year, day)
    :ok = path |> Path.dirname() |> File.mkdir_p()
    :ok = File.write(path, input)
  end

  def download!(year, day) do
    HTTPoison.start()

    {:ok, %{status_code: 200, body: input}} =
      HTTPoison.get("https://adventofcode.com/#{year}/day/#{day}/input", headers())

    input
  end

  def cache_dir do
    Path.join(System.get_env("XDG_CACHE_HOME", "~/.cache"), "/advent_of_code_inputs")
  end

  def cache_path(year, day), do: Path.join(cache_dir(), "/#{year}/#{day}")

  def in_cache?(year, day), do: File.exists?(cache_path(year, day))

  defp headers do
    # Expand the path and read the session token from the file
    session_token =
      "~/.cache/advent_of_code_inputs/cookie"
      |> Path.expand()
      |> File.read!()
      |> String.trim()  # Trim to remove any trailing newlines or spaces

    # Return the headers with the session token
    [cookie: "session=" <> session_token]
  end
end
