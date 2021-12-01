import org.scalatest.FunSuite

class TestVowelSpellchecker extends FunSuite {
    test("case01") {
        val Input = Array("KiTe", "kite", "hare", "Hare")
        val queries = Array("kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto")
        val Output = Array("kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe")
        assert(VowelSpellchecker.spellchecker(Input, queries) === Output)
    }
}
