import org.scalatest.FunSuite

class TestKeysAndRooms extends FunSuite {
    test("case01") {
        val input = List(List(1), List(2), List(3), List[Int]())
        val output = true
        assert(KeysAndRooms.canVisitAllRooms(input) === output)
    }

    test("case02") {
        val input = List(List(1, 3), List(3, 0, 1), List(2), List(0))
        val output = false
        assert(KeysAndRooms.canVisitAllRooms(input) === output)
    }
}
