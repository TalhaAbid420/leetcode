class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            string = ""

            if i % 3 == 0:  string += "Fizz"
            if i % 5 == 0:  string += "Buzz"

            result.append(string or str(i))

        return result
        
