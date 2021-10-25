from statistics import mean


if __name__ == '__main__':
    # stage 1
    # scores = [int(input()) for _ in range(3)]
    # print(mean(scores))
    # print("Congratulations, you are accepted!")

    # stage 2
    scores = [int(input()) for _ in range(3)]
    mean_score = mean(scores)
    print(mean_score)
    if mean_score >= 60.0:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")
