import org.scalatest.FunSuite

class TestPacificAtlanticWaterFlow extends FunSuite {
    test("case01") {
        val matrix = Array(
            Array(1, 2, 2, 3, 5),
            Array(3, 2, 3, 4, 4),
            Array(2, 4, 5, 3, 1),
            Array(6, 7, 1, 4, 5),
            Array(5, 1, 1, 2, 4)
        )
        val expected = List(List(0, 4), List(1, 3), List(1, 4), List(2, 2), List(3, 0), List(3, 10), List(4, 0))
        assert(PacificAtlanticWaterFlow.pacificAtlantic(matrix) === expected)
    }
}
