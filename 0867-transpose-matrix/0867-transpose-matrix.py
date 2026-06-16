class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp = zip(*matrix)      
        temp = map(list, temp)
        answer = list(temp)
        return answer                                    