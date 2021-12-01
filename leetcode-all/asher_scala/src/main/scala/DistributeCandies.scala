import scala.collection.mutable

object DistributeCandies {
    def distributeCandies(candyType: Array[Int]): Int = {
        val types = mutable.Map[Int, Int]()
        for (i <- candyType) {
            types(i) = types.getOrElse(i, 0) + 1
        }

        if (types.size > candyType.length / 2) {
            candyType.length / 2
        } else {
            types.size
        }
    }
}
