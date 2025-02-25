import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class VacumWorld {
    private static List<Integer> world = new ArrayList<>();
    private static int position = 0;
    private static final int WORLD_SIZE = 20;

    public static void main(String[] args) {
        createWorld();
        System.out.println("Initial world: " + world);
        while (!verifyClean()) {
            positionStart();
            cleanWorld();
        }
        System.out.println("Final world: " + world);
    }

    private static void moveRight() {
        position = Math.min(position + 1, WORLD_SIZE - 1);
    }

    private static void moveLeft() {
        position = Math.max(position - 1, 0);
    }

    private static boolean isEnd() {
        return position == WORLD_SIZE - 1;
    }

    private static boolean isStart() {
        return position == 0;
    }

    private static boolean isClean() {
        return world.get(position) == 0;
    }

    private static void clean() {
        world.set(position, 0);
    }

    private static void positionStart() {
        while (!isStart()) {
            moveLeft();
        }
    }

    private static boolean verifyClean() {
        positionStart();
        while (!isEnd()) {
            if (!isClean()) {
                return false;
            }
            moveRight();
        }
        return true;
    }

    private static void cleanWorld() {
        while (!isEnd()) {
            clean();
            moveRight();
        }
    }

    private static void createWorld() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Number of dirty squares: ");
        int concurrency = scanner.nextInt();
        world.clear();
        for (int i = 0; i < concurrency; i++) {
            world.add(1);
        }
        for (int i = concurrency; i < WORLD_SIZE; i++) {
            world.add(0);
        }
        Collections.shuffle(world);
        position = new Random().nextInt(WORLD_SIZE);
    }
}