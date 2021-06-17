import java.io.File
import java.math.BigInteger
import kotlin.math.pow

fun main() {
    val vals = HashMap<BigInteger, BigInteger>()
    var mask = CharArray(0)

    File("input.txt").forEachLine {
        if (it.startsWith("mask"))
            mask = it.substringAfter('=').trim().toCharArray()
        else {
            val origAddr = Integer.toBinaryString(it.substringAfter('[').substringBefore(']').toInt())
            val origAddrBits = origAddr.padStart(mask.size, '0').toCharArray()
            val value = BigInteger(it.substringAfter('=').trim())

            var xCount = 0
            val maskedAddress = mask.zip(origAddrBits).map { (maskBit, addressBit) ->
                if (maskBit == '0') addressBit else {
                    if (maskBit == 'X') {
                        xCount++
                    }
                    maskBit
                }
            }

            (0 until (2.toDouble()).pow(xCount).toInt()).forEach { perm ->
                val bits = Integer.toBinaryString(perm).padStart(xCount, '0').toCharArray()
                var pointer = 0
                val filledAddr = BigInteger(maskedAddress.map { bit ->
                    if (bit != 'X') bit else {
                        bits[pointer++]
                    }
                }.joinToString(separator = ""), 2)

                vals[filledAddr] = value
            }
        }
    }

    println(vals.values.reduce { acc, i -> acc+i })
}