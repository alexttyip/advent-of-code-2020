import java.io.File
import kotlin.math.abs

fun main() {
    var ns = 0
    var ew = 0
    var degree = 0

    File("input.txt").forEachLine {
        var opc = it[0]
        val ope = it.subSequence(1, it.length).toString().toInt()

        if (opc == 'F') {
            opc = degreeToDir(degree)
        }

        when (opc) {
            'N' -> ns += ope
            'E' -> ew += ope
            'S' -> ns -= ope
            'W' -> ew -= ope

            'L' -> degree = (degree - ope + 360) % 360
            'R' -> degree = (degree + ope) % 360
        }
    }

    println(abs(ns) + abs(ew))
}

private fun degreeToDir(degree: Int): Char {
    return when (degree) {
        90 -> 'S'
        180 -> 'W'
        270 -> 'N'
        else -> 'E'
    }
}
