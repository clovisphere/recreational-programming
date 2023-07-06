-- haskell ☺️

twoSum :: [Int] -> Int -> (Int, Int)
twoSum nums target = [(x, y) | x <- i, y <- i, x < y && nums !! x + nums !! y == target] !! 0
    where i = [0..length nums - 1]
