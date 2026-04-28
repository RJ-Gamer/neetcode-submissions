class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array = []

        for i in range(len(arr)-1):
            max_elem = max(arr[i+1:])
            new_array.append(max_elem)

        new_array.append(-1)

        return new_array