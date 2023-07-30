-- Given an array of integers, calculate the ratios of
-- its elements that are positive, negative, and zero

import Data.Function
import Numeric

pprint :: RealFloat a => Int -> a -> String
pprint n x = showGFloat (Just n) x ""

ratios :: [Int] -> [Float]
ratios xs = [pos/len, neg/len, (len-pos-neg)/len]
    where len   = fromIntegral $ length xs
          pos   = fromIntegral $ length $ filter (>0) xs
          neg   = fromIntegral $ length $ filter (<0) xs

main :: IO ()
main = interact $ unlines . map (pprint 6) . ratios . map read . tail . words
