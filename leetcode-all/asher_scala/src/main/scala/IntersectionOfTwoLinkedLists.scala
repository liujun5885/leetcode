object IntersectionOfTwoLinkedLists {

    class ListNode(var _x: Int = 0) {
        var next: ListNode = null
        var x: Int = _x
    }

    def getIntersectionNode(headA: ListNode, headB: ListNode): ListNode = {
        var nodeArrayA = Array[ListNode]()
        var nodeArrayB = Array[ListNode]()
        var nodeA = headA;
        while (nodeA != null) {
            nodeArrayA = nodeArrayA :+ nodeA
            nodeA = nodeA.next
        }
        var nodeB = headB;
        while (nodeB != null) {
            nodeArrayB = nodeArrayB :+ nodeB
            nodeB = nodeB.next
        }

        if (nodeArrayA.isEmpty || nodeArrayB.isEmpty) {
            return null
        }

        if (nodeArrayA.last != nodeArrayB.last) {
            return null
        }

        var i = nodeArrayA.length - 1
        var j = nodeArrayB.length - 1

        while (i >= 0 && j >= 0 && nodeArrayA(i) == nodeArrayB(j)) {
            i -= 1
            j -= 1
        }
        nodeArrayA(i + 1)
    }
}
