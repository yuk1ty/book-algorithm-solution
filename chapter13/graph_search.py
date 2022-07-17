# code 13.1
from graph import Graph


# 本書の中では「search」という名前の関数になっている
# 幅優先探索
def bfs(G: Graph, s: int):
    N = len(G)

    seen = [False] * N
    todo = []  # キューとして利用する

    seen[s] = True
    todo.append(s)

    while not len(todo) == 0:
        v = todo.pop(0)

        for x in G[v]:
            if seen[x]:
                continue

            seen[x] = True
            todo.append(x)


# 深さ優先探索
def dfs(G: Graph, s: int):
    N = len(G)

    seen = [False] * N
    todo = []  # スタックとして利用する

    seen[s] = True
    todo.append(s)

    while not len(todo) == 0:
        v = todo.pop()

        for x in G[v]:
            if seen[x]:
                continue

            seen[x] = True
            todo.append(x)
