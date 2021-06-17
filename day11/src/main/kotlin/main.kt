import java.io.File

fun main() {
    val grid = arrayListOf<ArrayList<Char>>()
    File("input.txt").forEachLine {
        grid.add(ArrayList(it.toCharArray().toList()))
    }

    println(run(grid))
}

fun run(grid: ArrayList<ArrayList<Char>>): Int {
    val n = grid.size
    val m = grid[0].size

    val newGrid = ArrayList(Array(n) { ArrayList(Array(m) { '.' }.toList()) }.toList())

    var same = true

    grid.forEachIndexed { i, row ->
        row.forEachIndexed { j, c ->
            var count = 0

            for (dx in -1..1) {
                for (dy in -1..1) {
                    if (dx == 0 && dy == 0) {
                        continue
                    }

                    var nx = i + dx
                    var ny = j + dy

                    while (nx in 0 until n && ny in 0 until m && grid[nx][ny] == '.') {
                        nx += dx
                        ny += dy
                    }

                    if (nx in 0 until n && ny in 0 until m && grid[nx][ny] == '#') {
                        count++
                    }
                }
            }

            newGrid[i][j] = if (c == 'L' && count == 0) {
                same = false
                '#'
            } else if (c == '#' && count >= 5) {
                same = false
                'L'
            } else {
                c
            }
        }
    }

    return if (same) {
        var count = 0
        grid.forEach { row ->
            row.forEach {
                if (it == '#') count++
            }
        }

        count
    } else {
        run(newGrid)
    }
}