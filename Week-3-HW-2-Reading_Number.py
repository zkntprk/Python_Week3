### All Rights Reserved ###

#Copyright (c) ${Reading_Number.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

'''
------PROJECT------
-Reading Numbers ( 2 digits)
Write a function that outputs the transcription of an input number with two digits.

Example:
28---------------->Twenty Eight
'''

def Reading_Number(a):
    b=list(a)
    a=int(a)
    c={10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
    d={20:'Twenty',30:'Thirty',40:'Fourty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
    e={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    if (a < 10 or a > 99):
        return print('Wrong Entry!')
    elif a<20 and a>9:
        return print(c[a])
    elif (a==20 or a==30 or a==40 or a==50 or a== 60 or a== 70 or a==80 or a==90):
        return print(d[a])
    else:
        return print(d[(int(b[0]))*10],e[int(b[1])])

a=input('Please enter 2 digit number: ')
Reading_Number(a)

### All Rights Reserved ###

#Copyright (c) ${Reading_Number.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.