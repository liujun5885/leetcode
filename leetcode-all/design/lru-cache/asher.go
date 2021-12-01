package main

type Node struct {
	key    int
	val    int
	next   *Node
	parent *Node
}

type LRUCache struct {
	capacity int
	kv       map[int]*Node
	head     *Node
}

func Constructor(capacity int) (cache LRUCache) {
	cache = LRUCache{
		capacity: capacity,
		kv:       map[int]*Node{},
		head: &Node{
			key:    0,
			val:    0,
			next:   nil,
			parent: nil,
		},
	}
	cache.head.next = cache.head
	cache.head.parent = cache.head
	return
}

func (this *LRUCache) pushNode(node *Node) {
	node.parent = this.head
	node.next = this.head.next
	this.head.next.parent = node
	this.head.next = node
}

func removeNode(node *Node) {
	node.parent.next = node.next
	node.next.parent = node.parent
	node.parent = nil
	node.next = nil
}

func (this *LRUCache) Get(key int) int {
	if this.capacity < 1 {
		return -1
	}
	if node, ok := this.kv[key]; ok {
		removeNode(node)
		this.pushNode(node)
		return node.val
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	if this.capacity < 1 {
		return
	}
	if node, ok := this.kv[key]; ok {
		node.val = value
		removeNode(node)
		this.pushNode(node)
		return
	}
	if len(this.kv) == this.capacity {
		node := this.head.parent
		removeNode(node)
		delete(this.kv, node.key)
	}
	node := &Node{
		key:    key,
		val:    value,
		next:   nil,
		parent: nil,
	}
	this.kv[key] = node
	this.pushNode(node)
}

func main() {
	cache := Constructor(1)
	cache.Put(2, 1)
	cache.Get(2)
	cache.Put(3, 2)
	cache.Get(2)
	cache.Get(3)
}
