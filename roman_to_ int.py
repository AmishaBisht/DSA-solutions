class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result=0
        for i in range(len(s)):
            #check if the previous value is smaller
            if i+1<len(s) and romanValues[s[i]]<romanValues[s[i+1]]: 
                result -= romanValues[s[i]]
            else:
                result += romanValues[s[i]] #if the previous value os greater
        return result
        

        
print(py_solution().roman_to_int('MMMCMXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('CMXCVIII'))
print(py_solution().roman_to_int(III).int_val)
