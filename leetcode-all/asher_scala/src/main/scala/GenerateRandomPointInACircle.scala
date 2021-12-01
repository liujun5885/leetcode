import scala.util.Random

object GenerateRandomPointInACircle {

    class GenerateRandomPointInACircle(_radius: Double, _x_center: Double, _y_center: Double) {
        def randPoint(): Array[Double] = {
            val x = Random.between(_x_center - _radius, _x_center + _radius)
            println(math.pow(_radius, 2), math.pow(x - _x_center, 2))
            val _y = math.sqrt(math.pow(_radius, 2) - math.pow(x - _x_center, 2))
            val y = Random.between(_y_center - _y, _y_center + _y)

            Array(x, y)
        }
    }

    def main(args: Array[String]): Unit = {
        val obj = new GenerateRandomPointInACircle(7.5, 1.5, 2.5)
        for (i <- 0 to 100) {
            val param_1 = obj.randPoint()
            param_1.foreach(println)
        }
    }
}


