import scala.collection.mutable

object KeysAndRooms {

    def canVisitAllRooms(rooms: List[List[Int]]): Boolean = {
        val used = new Array[Boolean](rooms.length)

        var p = rooms(0).toArray
        used(0) = true
        while (!p.isEmpty) {
            var newKeys = Array[Int]()
            for (k <- p) {
                used(k) = true
                for (i <- rooms(k)) {
                    if (!used(i)) {
                        newKeys :+= i
                    }
                }
            }
            p = newKeys
        }
        !used.contains(false)
    }
}
