### All Rights Reserved ###

#Copyright (c) ${Equal_Reverse.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

'''
------PROJECT----Equal_Reverse
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
'''
#b=list(input('Please enter your Equal_Reverse list by adding hyphen icon(-) between them :').split('-'))

t=[]
def rev(s):
    for i in s:
        if i == i[::-1]:
            t.append('True')
        else:
            t.append('False')
    return print(",".join(t))
   
rev(list(input('Please enter your Equal_Reverse list by adding comma (,) between them :').split(',')))

### All Rights Reserved ###

#Copyright (c) ${Equal_Reverse.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.