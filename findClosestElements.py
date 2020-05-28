class Solution:
    def search(self, arr, x):
        xx = [x]*len(arr)
        dif = [abs(arr[i] - xx[i]) for i in range(len(arr))]
        min = [0, dif[0]]
        for i in range(len(dif)):
            if (dif[i] < min[1]):
                min[0] = i
                min[1] = dif[i]
        return min[0]




    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[0:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            x_index = self.search(arr, x)
            low = max(0, x_index -k - 1)
            high = min(len(arr) - 1, x_index + k - 1)
        while (high - low > k - 1):
            if (x - arr[low]) <= (arr[high] - x):
                high = high - 1
            else:
                low = low + 1
        return arr[low:high+1]