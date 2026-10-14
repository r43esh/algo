# happy number
class Solution:
    def do(self,n):
        sum=0
        while n:
            ones=n%10
            n//=10
            sum=sum+ones*ones
        return sum
    def isHappy(self, n: int) -> bool:
        nums=set()
        while n!=1 and n not in nums:
            nums.add(n)
            n=self.do(n)

        if n==1:
            return True
        return False
      