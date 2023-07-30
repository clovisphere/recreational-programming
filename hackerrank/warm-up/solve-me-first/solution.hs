-- sum of two integers

main = interact $ show . sum . map read . words
