import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        final List<String> commands = readCommands();
        List<Integer> keyVals = new LinkedList<Integer>();

        for(String command : commands) {
            Point tempPoint = new Point();

            for(char dir : command.toCharArray()) {

                switch (dir) {
                    case 'U':
                        tempPoint.move(Direction.UP);
                        break;
                    case 'D':
                        tempPoint.move(Direction.DOWN);
                        break;
                    case 'L':
                        tempPoint.move(Direction.LEFT);
                        break;
                    case 'R':
                        tempPoint.move(Direction.RIGHT);
                        break;
                }
            }

            keyVals.add(tempPoint.keypadVal());
        }

        System.out.println(keyVals.toString());
    }

    static List<String> readCommands() throws FileNotFoundException {
        BufferedReader br = new BufferedReader(new FileReader("in.txt"));
        List<String> commandList = new LinkedList<String>();
        String fileLine;
        try {
            while( (fileLine = br.readLine()) != null) {
                commandList.add(fileLine);
            }

        } catch (IOException ex) {
            throw new RuntimeException("Could not read from file");
        }
        return commandList;
    }
}



enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT
}

class Point {
    int x = 1, y = 1;

    /**  y  0   1   2
     * x
     * 0    1   2   3
     * 1    4   5   6
     * 2    7   8   9
     * @return Keypad val resolution from the x,y pair
     */
    Integer keypadVal() {
        return x*3 + y + 1;
    }

    /**
     * Moves the point in a certain direction
     * @param dir Direction to move the point
     */
    void move(Direction dir) {
        switch (dir) {
            case UP:
                if( x > 0 ) x--;
                break;
            case DOWN:
                if( x < 2 ) x++;
                break;
            case LEFT:
                if( y > 0 ) y--;
                break;
            case RIGHT:
                if( y < 2 ) y++;
                break;
        }
    }
}
