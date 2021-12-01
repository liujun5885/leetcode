
object VowelSpellchecker {
    def spellchecker(wordlist: Array[String], queries: Array[String]): Array[String] = {
        var wordMap = Map[String, String]()

        for (i <- wordlist) {
            if (!wordMap.contains(i)) {
                wordMap += (i.toLowerCase() -> i)
            }
        }

        var output = Array[String]()
        queries.foreach(x => if (wordlist.contains(x)) {
            output :+= x
        } else if (wordMap.contains(x.toLowerCase())) {
            output :+= wordMap(x.toLowerCase())
        } else {
            output :+= ""
        })
        output
    }
}
