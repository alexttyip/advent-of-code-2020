import java.io.File
import kotlin.math.abs

fun main() {
    val ship = Coordinates(0, 0)
    val waypoint = Coordinates(1, 10)

    File("input.txt").forEachLine {
        val opc = it[0]
        val ope = it.subSequence(1, it.length).toString().toInt()

        when (opc) {
            'N' -> waypoint.NS += ope
            'E' -> waypoint.EW += ope
            'S' -> waypoint.NS -= ope
            'W' -> waypoint.EW -= ope

            'L' -> waypoint.rotate(360 - ope)
            'R' -> waypoint.rotate(ope)

            'F' -> ship.moveTo(waypoint, ope)
        }
    }

    print(ship.manhattan())
}

class Coordinates(var NS: Int, var EW: Int) {
    fun rotate(degree: Int) {
        when (degree % 360) {
            90 -> {
                val oldNS = NS
                NS = EW * -1
                EW = oldNS
            }
            180 -> {
                NS *= -1
                EW *= -1
            }
            270 -> {
                val oldNS = NS
                NS = EW
                EW = oldNS * -1
            }
        }
    }

    fun moveTo(dest: Coordinates, times: Int) {
        NS += dest.NS * times
        EW += dest.EW * times
    }

    fun manhattan(): Int = abs(NS) + abs(EW)
}