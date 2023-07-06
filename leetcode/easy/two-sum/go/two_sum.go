package leetcode

func twoSum(nums []int, target int) []int {
	indices := make(map[int]int)
	var result []int
	for i, num := range nums {
		if j, ok := indices[target-num]; ok {
			result = append(result, j, i)
			break
		}
		indices[num] = i
	}
	return result
}
