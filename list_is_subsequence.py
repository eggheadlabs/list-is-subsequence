# Validate an array is a subsequence of another array
# Example: A=[2, 4, 6, -3, 8, 5, 0], B=[4, -3, 5]. B is a subsequence of A. (Note that the order of sequence must be maintained)
# However, C=[4, 5, -3] is not a subsequence of A 

# is seq a subsequence of array
def isSubsequence(array, seq):
    a = 0   # array index
    s = 0   # seq index
    while a < len(array) and s < len(seq):
        if seq[s] == array[a]:
            s += 1
        a += 1
    return s == len(seq)

A = [2, 4, 6, -3, 8, 5, 0]
B = [4, -3, 5]

if isSubsequence(A, B):
    print(str(B) + ' is a subseq of ', str(A))
else:
    print(str(B) + ' is NOT a subseq of ', str(A))