object RemovePalindromicSubsequences {
    def isPalindromic(s: String): Boolean = {
        var i = 0
        var j = s.length - 1
        while (i <= j) {
            if (s(i) != s(j)) {
                return false
            }
            i += 1
            j -= 1
        }
        true
    }

    def removePalindromeSub(s: String): Int = {
        if (s.isEmpty) {
            return 0
        }
        if (isPalindromic(s)) {
            return 1
        }
        2
    }
}
