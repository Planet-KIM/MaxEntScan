from maxentscan.mes3 import score3

seq_list = [
        "ctctactactatctatctaggtc",
        "ctctactactatctatctaggtc",
        "ctctactactatctatctagctc",
        "ctctactactatctatctagttc",
        "ctctactactatctatctagatc",
        "ctctactactatctatctccctc"
        ]
dic = score3(seq_list)
print(dic)


result = score3("ctctactactatctatctaggtc")
print(result)
