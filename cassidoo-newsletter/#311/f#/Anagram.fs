(* given two strings `s` and `t` returns `true` if they're anagrams,
   false otherwise
*)

let transform (w: string): string =
    w.ToLower()
    |> Seq.sort
    |> System.String.Concat

let isAnagram (s: string) (t: string): bool = (=) (transform s) (transform t)
