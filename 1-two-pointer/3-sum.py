
arr = [-1, 0, 1, 2, -1, -4]
target = 0
arr.sort()

def solution(arr):
    result = []

    for i in range(len(arr) - 2):

        # skip duplicate i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        checksum = target - arr[i]
        l, r = i + 1, len(arr) - 1

        while l < r:
            current = arr[l] + arr[r]

            if current < checksum:
                l += 1
            elif current > checksum:
                r -= 1
            else:
                result.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1

    return result

print(solution(arr))






    


