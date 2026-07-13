#run in terminal: python "vishal/leet/1331.py"
def arrayRankTransform(arr):
        sorted_arr = sorted(arr)

        rank = {}
        current_rank = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1

        return [rank[num] for num in arr]
arr = [40, 10, 20, 30]
print(arrayRankTransform(arr))