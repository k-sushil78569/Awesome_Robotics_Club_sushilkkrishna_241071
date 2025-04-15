#include <stdio.h>

#define ROWS 10
#define COLS 10
#define INF 1000000000
#define MAX_PATHS 30000
#define MAX_PATH_LENGTH 100

struct Coord {
    int x, y, cost;
};

// Grid definition
char grid[ROWS][COLS] = {
    {'S', '.', '.', '.', '.', '~', '.', '.', '^', '.'},
    {'#', '#', '#', '.', '.', '~', '#', '.', '^', '.'},
    {'.', '.', '.', '#', '.', '.', '#', '.', '.', '.'},
    {'.', '~', '~', '#', '.', '.', '.', '.', '.', '.'},
    {'.', '.', '.', '.', '.', '#', '#', '#', '#', '.'},
    {'^', '^', '.', '.', '.', '.', '.', '.', '~', '.'},
    {'#', '.', '.', '.', '.', '#', '~', '~', '~', '.'},
    {'.', '.', '#', '#', '.', '.', '.', '.', '.', '.'},
    {'.', '.', '.', '.', '.', '^', '^', '^', '^', 'G'},
    {'.', '#', '#', '#', '#', '#', '#', '.', '.', '.'}
};

int costMap[ROWS][COLS];

// Path storage
Coord allPaths[MAX_PATHS][MAX_PATH_LENGTH];
int pathLengths[MAX_PATHS];
int pathCount = 0;

int isInPath(Coord path[], int length, int x, int y) {
    for (int i = 0; i < length; i++)
        if (path[i].x == x && path[i].y == y)
            return 1;
    return 0;
}

void initializeCostMap() {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            char cell = grid[i][j];
            if (cell == '#') costMap[i][j] = INF;
            else if (cell == '.') costMap[i][j] = 1;
            else if (cell == '~') costMap[i][j] = 3;
            else if (cell == '^') costMap[i][j] = 5;
            else if (cell == 'S' || cell == 'G') costMap[i][j] = 1;
        }
    }
}

int isValid(int x, int y, Coord path[], int length) {
    if (x < 0 || y < 0 || x >= ROWS || y >= COLS || costMap[x][y] == INF)
        return 0;
    return !isInPath(path, length, x, y);
}

void dfs(int x, int y, Coord path[], int length) {
    if (length >= MAX_PATH_LENGTH || pathCount >= MAX_PATHS)
        return;

    path[length].x = x;
    path[length].y = y;
    path[length].cost = costMap[x][y];
    length++;

    if (grid[x][y] == 'G') {
        for (int i = 0; i < length; i++)
            allPaths[pathCount][i] = path[i];
        pathLengths[pathCount] = length;
        pathCount++;
        return;
    }

    // Prefer moving down and right first
    int dx[] = {1, 0, 0, -1}; // down, right, left, up
    int dy[] = {0, 1, -1, 0};

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (isValid(nx, ny, path, length)) {
            dfs(nx, ny, path, length);
        }
    }
}

int main() {
    initializeCostMap();

    Coord path[MAX_PATH_LENGTH];
    dfs(0, 0, path, 0);

    if (pathCount == 0) {
        printf("No path found from S to G.\n");
        return 0;
    }

    int minCost = INF;
    int bestIndex = -1;

    for (int i = 0; i < pathCount; i++) {
        int total = 0;
        for (int j = 0; j < pathLengths[i]; j++)
            total += allPaths[i][j].cost;

        if (total < minCost) {
            minCost = total;
            bestIndex = i;
        }
    }

    printf("Best path coordinates:\n");
    for (int i = 0; i < pathLengths[bestIndex]; i++) {
        printf("(%d,%d) ", allPaths[bestIndex][i].x, allPaths[bestIndex][i].y);
    }

    printf("\nTotal cost: %d\n", minCost-2);
    return 0;
}
