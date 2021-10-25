from statistics import mean


if __name__ == '__main__':
    # stage 1
    # scores = [int(input()) for _ in range(3)]
    # print(mean(scores))
    # print("Congratulations, you are accepted!")

    # stage 2
    # scores = [int(input()) for _ in range(3)]
    # mean_score = mean(scores)
    # print(mean_score)
    # if mean_score >= 60.0:
    #     print("Congratulations, you are accepted!")
    # else:
    #     print("We regret to inform you that we will not be able to offer you admission.")

    # stage 3
    # get input
    number_applicants = int(input())
    max_acceptance = int(input())
    applicants = []
    for _ in range(number_applicants):
        applicants.append(input().split())

    # sort in respect to GPA and than full name
    sorted_applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))

    # print accepted list
    print("Successful applicants:")
    for i in range(max_acceptance):
        print(f"{sorted_applicants[i][0]} {sorted_applicants[i][1]}")
