import java.io.File
import java.math.BigInteger

fun main() {
    val vals = HashMap<Int, BigInteger>()
    var mask = CharArray(0)

    File("input.txt").forEachLine {
        if (it.startsWith("mask"))
            mask = it.substringAfter('=').trim().toCharArray()
        else {
            val index = it.substringAfter('[').substringBefore(']').toInt()
            val bitsString = Integer.toBinaryString(it.substringAfter('=').trim().toInt())
            val bits = bitsString.padStart(mask.size, '0').toCharArray()

            var value = ""
            mask.zip(bits).forEach { (maskBit, bit) ->
                value += if (maskBit == 'X') {
                    bit
                } else {
                    maskBit
                }
            }

            vals[index] = BigInteger(value, 2)
        }
    }

    print(vals.values.reduce { acc, curr -> acc + curr })
}