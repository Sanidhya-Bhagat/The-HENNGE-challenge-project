import sys

def main():
    data = sys.stdin.read().split()
    pos = [0]

    def next_int():
        val = int(data[pos[0]])
        pos[0] += 1
        return val

    def solve(n):
        if n == 0:
            return

        x = next_int()
        nums = list(map(int, data[pos[0] : pos[0] + x]))
        pos[0] += x

        if len(nums) != x:
            print(-1)
        else:
            print(sum(map(lambda y: y ** 4, filter(lambda y: y <= 0, nums))))

        solve(n - 1)

    solve(next_int())

if __name__ == "__main__":
    main()