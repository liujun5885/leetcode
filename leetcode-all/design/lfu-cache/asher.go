package main

type Node struct {
	key    int
	val    int
	freq   int
	next   *Node
	parent *Node
}

type LFUCache struct {
	capacity    int
	minReq      int
	kv          map[int]*Node
	freqHashMap map[int]*Node
}

func Constructor(capacity int) LFUCache {
	return LFUCache{capacity: capacity, kv: map[int]*Node{}, freqHashMap: map[int]*Node{}}
}

func (this *LFUCache) increaseFreq(node *Node) {
	node.parent.next = node.next
	node.next.parent = node.parent

	node.parent = nil
	node.next = nil

	if this.freqHashMap[node.freq].next == this.freqHashMap[node.freq] {
		delete(this.freqHashMap, node.freq)
		if this.minReq == node.freq {
			this.minReq++
		}
	}
	node.freq++

	this.putNodeInFreqHashmap(node.freq, node)
}

func (this *LFUCache) putNodeInFreqHashmap(freq int, node *Node) {
	if head, ok := this.freqHashMap[freq]; ok {
		node.parent = head
		node.next = head.next
		head.next.parent = node
		head.next = node
	} else {
		head = &Node{}
		head.next = head
		head.parent = head
		this.freqHashMap[freq] = head
		node.parent = head
		node.next = head.next
		head.next.parent = node
		head.next = node
	}
}

func (this *LFUCache) Get(key int) int {
	if this.capacity < 1 {
		return -1
	}
	node, ok := this.kv[key]
	if !ok {
		return -1
	}
	this.increaseFreq(node)
	return node.val
}

func (this *LFUCache) Put(key int, value int) {
	if this.capacity < 1 {
		return
	}
	node, ok := this.kv[key]
	if !ok {
		// remove node
		if len(this.kv) == this.capacity {
			head := this.freqHashMap[this.minReq]
			removedNode := head.parent
			head.parent = removedNode.parent
			removedNode.parent.next = head
			if head.next == head {
				delete(this.freqHashMap, this.minReq)
			}
			delete(this.kv, removedNode.key)
		}

		node = &Node{
			key:  key,
			val:  value,
			freq: 1,
		}
		this.kv[key] = node
		this.putNodeInFreqHashmap(1, node)
		this.minReq = 1
	} else {
		this.increaseFreq(node)
		node.val = value
	}
}

func main() {
	cache := Constructor(1)
	cache.Put(2, 1)
	cache.Get(2)
	cache.Put(3, 2)
	cache.Get(2)
	cache.Get(3)
}
