n=int(input())
day_shift=sorted(map(int,input().split()))
night_shift=sorted(map(int,input().split()),reverse=True)
x=int(input())

print(
    100 * sum(
        max(0, d + n - x)
        for d, n in zip(day_shift, night_shift)
    )
)
