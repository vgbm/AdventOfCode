from strutils import split, parseInt, strip

type
    Direction {.pure.} = enum
        Left,
        Right,
        Forward,
        Backward

    Move = tuple[dir: Direction, steps: int]

    #allocate ref to avoid copying object
    Point = ref object
        x, y: int
        dir: Direction


proc strToMove(input: string): Move =
    var retMove: Move
    if input[0] == 'L':
        retMove.dir = Direction.Left
    else:
        retMove.dir = Direction.Right
    retMove.steps = parseInt(input[1..^1])
    return retMove


proc inputMoves: seq[Move] =
    const input = readFile("in.txt").strip
    const individualInputs = input.split(", ")

    var moves: seq[Move] = @[]
    for str in individualInputs:
        moves.add(str.strTOMove)

    return moves


#quick and dirty way of pulling the new facingDir
proc rotate(facingDir, rotationDir: Direction): Direction =
    case facingDir
    of Direction.Forward:
        if rotationDir == Direction.Left:
            return Direction.Left
        else:
            return Direction.Right
    of Direction.Left:
        if rotationDir == Direction.Left:
            return Direction.Backward
        else:
            return Direction.Forward
    of Direction.Backward:
        if rotationDir == Direction.Left:
            return Direction.Right
        else:
            return Direction.Left
    of Direction.Right:
        if rotationDir == Direction.Left:
            return Direction.Forward
        else:
            return Direction.Backward


proc move(point: Point, move: Move) =
    case point.dir
    of Direction.Forward:
        point.y += move.steps
    of Direction.Left:
        point.x -= move.steps
    of Direction.Right:
        point.x += move.steps
    of Direction.Backward:
        point.y -= move.steps


proc finalLocation(moves: seq[Move]): Point =
    var point = Point(x: 0, y: 0, dir: Direction.Forward)
    for move in moves:
        point.dir = rotate(point.dir, move.dir)
        point.move(move)
    return point


proc distance(point: Point): int = abs(point.x) + abs(point.y)


let moves = inputMoves()
let point = finalLocation(moves)
echo point.distance
