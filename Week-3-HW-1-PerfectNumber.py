
### All Rights Reserved ###

#Copyright (c) ${PerfectNumber.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
                                ---PROJECT---
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
'''
from functools import reduce
nums=list(range(2,1000)) #between 1 and 1000
def perfect(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    if a==n:
        return n
print('Perfect Numbers: ',list(filter(perfect,nums)))
print('Sum of the perfect numbers: ',reduce(lambda x, y: x + y, list(filter(perfect,nums))))

### All Rights Reserved ###

#Copyright (c) ${PerfectNumber.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
