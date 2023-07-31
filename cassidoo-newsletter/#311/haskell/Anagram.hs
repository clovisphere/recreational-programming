--Given two strings s and t, return true if t is an anagram of s,
--and false otherwise.

module Anagram where

import Data.Char (toLower)
import Data.List (sort)
import Data.Function (on)

isAnagram :: [Char] -> [Char] -> Bool
isAnagram = (==) `on` (sort . map toLower)
