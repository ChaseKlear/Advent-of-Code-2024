# def parse_reports(report:str)->list[str]:
#     return report.split(" ")

# def make_int(report:str)->list[int]:



with open("input.txt") as input_raw:
    input:str = input_raw.read()
    reports:list[str] = [input.split("\n")]
    for i in range(len(reports)):
        reports[i] = reports[i].split(" ")
        for j in range(len(reports[i])):
            reports[i[j]] = int(reports[i[j]])
    print(reports)


    # first_reports:list[str] = input.split("\n")
    # second_reports:list[list[str]] = []
    # third_reports:list[list[int]] = []
    
    # for i in range(len(first_reports)):
    #     second_reports.append(first_reports[i].split(" "))
    #     third_reports.append()
    # print(third_reports)
    


    # for report in init_reports:
    #     for i in range(len(report.split(" "))):
    #         report[i] = int(report[i])
    #     reports.append(report.split(" "))

    




    # reports_map:map = map(parse_reports, init_reports)
    # for item in reports_map:
    #     print(item)

    
    #     print(temp)

    # reports:list[list[str]] = list(map(parse_reports, input.split("\n")))

    # for i in range(len(reports)):
    #     reports[i] = reports[i].split(" ")

    # print(reports)
