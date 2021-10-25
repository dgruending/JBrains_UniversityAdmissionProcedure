# from statistics import mean
def department_admission(file, department_list, max_accepted):
    # get all applicants
    applicants_list = []
    with open(file) as applicants_file:
        for applicant in applicants_file:
            applicants_list.append(applicant.split())

    # init accepted dict
    accepted = dict()
    for department in department_list:
        accepted[department] = []

    for priority in range(3):
        department_applicants = dict()
        for department in department_list:
            department_applicants[department] = []
        for applicant in applicants_list:
            # add applicant with (forename, surname, gpa)
            department_applicants[applicant[3 + priority]].append(applicant)
        # sort applicants in each department
        for applicants in department_applicants.values():
            applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

        # acceptance
        applicants_list = []
        for department, applicants in department_applicants.items():
            cut_off = min(len(applicants), max_accepted - len(accepted[department]))
            accepted[department].extend(applicants[:cut_off])
            applicants_list.extend(applicants[cut_off:])

    # sort accepted students again
    for students in accepted.values():
        students.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
    return accepted


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
    # number_applicants = int(input())
    # max_acceptance = int(input())
    # applicants = []
    # for _ in range(number_applicants):
    #     applicants.append(input().split())
    #
    # # sort in respect to GPA and than full name
    # sorted_applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[1]))
    #
    # # print accepted list
    # print("Successful applicants:")
    # for i in range(max_acceptance):
    #     print(f"{sorted_applicants[i][0]} {sorted_applicants[i][1]}")

    # stage 4
    departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
    accepted_students = department_admission("applicants.txt", departments, int(input()))
    for department, students in accepted_students.items():
        print(department)
        for student in students:
            print(f"{student[0]} {student[1]} {student[2]}")
        print()
