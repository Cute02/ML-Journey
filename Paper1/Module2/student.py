import csv

lst = [["Name", "Score"],
       ["Alice", 85],
       ["Bob", 45],
       ["Charlie", 92],
       ["David", 60],
       ["Eva", 38]]
with open("student_data.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerows(lst)


def process_scores(filename):
    with open(filename, "r") as f:
        read = csv.DictReader(f)
        new_lst1 = []
        new_lst2 = []
        for row in read:
            if int(row["Score"]) >= 50:
                new_lst1.append(row["Name"])
            elif int(row["Score"]) < 50:
                new_lst2.append(row["Name"])
        new_dict = {"pass": new_lst1, "fail": new_lst2}
    return new_dict


print(process_scores("student_data.csv"))
