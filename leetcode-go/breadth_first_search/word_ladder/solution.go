// Package word_ladder https://leetcode-cn.com/problems/word-ladder/
package word_ladder

func buildWordConnections(word string, conns map[int][]int, wordVsId map[string]int) {
	wordBytes := []byte(word)
	if _, exist := wordVsId[word]; exist {
		return
	}
	wordVsId[word] = len(wordVsId)

	for i := 0; i < len(wordBytes); i++ {
		tmp := wordBytes[i]
		wordBytes[i] = '*'
		curString := string(wordBytes)
		if _, exist := wordVsId[curString]; !exist {
			wordVsId[curString] = len(wordVsId)
		}
		conns[wordVsId[word]] = append(conns[wordVsId[word]], wordVsId[curString])
		conns[wordVsId[curString]] = append(conns[wordVsId[curString]], wordVsId[word])

		wordBytes[i] = tmp
	}
}

func bfs(conns map[int][]int, start, end int) int {
	if len(conns) == 0 {
		return 0
	}
	println(start, end)
	numOfLoops := 0

	stack := []int{start}
	visited := map[int]bool{}

	for i := 0; i < len(stack); {
		curLen := len(stack)
		numOfLoops += 1
		for ; i < curLen; i++ {
			if _, exists := visited[stack[i]]; exists {
				continue
			}
			visited[stack[i]] = true
			if stack[i] == end {
				return numOfLoops
			}
			for _, v := range conns[stack[i]] {
				stack = append(stack, v)
			}
		}
	}
	return 0
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordVsId := map[string]int{}
	conns := map[int][]int{}

	for _, w := range wordList {
		buildWordConnections(w, conns, wordVsId)
	}
	buildWordConnections(beginWord, conns, wordVsId)
	if _, exists := wordVsId[endWord]; !exists {
		return 0
	}

	length := bfs(conns, wordVsId[beginWord], wordVsId[endWord])
	if length == 0 {
		return length
	} else {
		return length/2 + 1
	}
}
