# Run in terminal: python "vishal/leet/165.py"
def compareVersion(version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n = max(len(v1), len(v2))
        
        for i in range(n):
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
        return 0
v1="1.0.1"
v2="1"
print(compareVersion(v1, v2))  # Output: 1