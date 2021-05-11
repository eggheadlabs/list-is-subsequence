# list-is-subsequence
Validate an array (list) is a subsequence of another array
Example: A=[2, 4, 6, -3, 8, 5, 0], B=[4, -3, 5]. B is a subsequence of A. (Note that the order of sequence must be maintained). However, C=[4, 5, -3] is not a subsequence of A

Tips: traverse array A, match each element of sequence B in order. B is a subseq of A if matched sequence index counts equal to the length of seq B.
