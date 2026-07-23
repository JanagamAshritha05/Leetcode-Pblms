class Solution: #(BruteForce)
    def frequencySort(self, nums):
        unique = []

        # Step 1: Find unique numbers
        for num in nums:
            if num not in unique:
                unique.append(num)

        # Step 2: Count frequency of each unique number
        freq_list = []

        for num in unique:
            count = 0

            for value in nums:
                if value == num:
                    count += 1

            freq_list.append([num, count])

        # Step 3: Manual sorting
        for i in range(len(freq_list)):
            for j in range(i + 1, len(freq_list)):

                # Smaller frequency comes first
                if freq_list[i][1] > freq_list[j][1]:
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

                # Same frequency -> Larger number comes first
                elif freq_list[i][1] == freq_list[j][1]:
                    if freq_list[i][0] < freq_list[j][0]:
                        freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

        # Step 4: Build the answer
        result = []

        for num, frequency in freq_list:
            for i in range(frequency):
                result.append(num)

        return result

# FrequencyCount + Custom Sorting 

class Solution:
    def frequencySort(self, nums):
        # Step 1: Count frequency
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Sort nums using frequency rules
        nums.sort(key=lambda num: (freq[num], -num))

        # Step 3: Return sorted array
        return nums

#FrequencyCount + BucketSort 

class Solution:
    def frequencySort(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket_arr = [[] for _ in range(len(nums)+1)] 
        
        for num, frequency in freq.items():
            bucket_arr[frequency].append(num)
        
        res = []
        for frequency in range(len(bucket_arr)):
            if bucket_arr[frequency]:
                bucket_arr[frequency].sort(reverse=True)
                
                for num in bucket_arr[frequency]:
                    for _ in range(frequency):
                        res.append(num)
            
        return res 




