from strutils import split, strip, parseInt
from sequtils import map

type
    CmdType = enum
        Toggle
        Off
        On
    
    Point = tuple
        x, y: int
    
    Rectangle = object
        topLeft, bottomRight: Point
    
    Cmd = object
        cmdType: CmdType
        rect: Rectangle


#too lazy to come up with a more efficient solution
var lights: array[1000, array[1000, bool]]


proc makeRect(tokens: seq[string]): Rectangle = 
    var rect: Rectangle

    var pts = tokens[0].split(",")
    rect.topLeft.x = pts[0].parseInt    
    rect.topLeft.y = pts[1].parseInt    
    
    pts = tokens[2].split(",")
    rect.bottomRight.x = pts[0].parseInt    
    rect.bottomRight.y = pts[1].parseInt    

    return rect


proc strToCmd(str: string): Cmd = 
    let tokens = str.split()
    var retCmd: Cmd

    if tokens[0] == "toggle":
        retCmd.cmdType = Toggle
        retCmd.rect = makeRect(tokens[1..^1])
    elif tokens[1] == "on":
        retCmd.cmdType = On
        retCmd.rect = makeRect(tokens[2..^1])
    else:
        retCmd.cmdType = Off
        retCmd.rect = makeRect(tokens[2..^1])
 
    return retCmd


proc commands: seq[Cmd] =
    const input = readFile("in.txt").strip().split("\n")
    return map(input, strToCmd)


#this sucks but is good enough for this purpose
proc followCmd(cmd: Cmd) = 
    for y in countup(cmd.rect.topLeft.y, cmd.rect.bottomRight.y):
        for x in countup(cmd.rect.topLeft.x, cmd.rect.bottomRight.x):
            case cmd.cmdType
            of Toggle:
                lights[x][y] = not lights[x][y]
            of On:
                lights[x][y] = true
            else:
                lights[x][y] = false


proc processCmds = 
    const cmds = commands()
    for cmd in cmds:
        followCmd(cmd)


proc litLights: int = 
    var litCount: int = 0
    for y in 0..999:
        for x in 0..999:
            if lights[x][y] == true:
                litCount += 1
    return litCount


processCmds()
echo litLights()