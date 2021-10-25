from statistics import mean


if __name__ == '__main__':
    # stage 1
    scores = [int(input()) for _ in range(3)]
    print(mean(scores))
    print("Congratulations, you are accepted!")
