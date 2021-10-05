import json
import pandas as pd
import openpyxl


def json_to_xlsx(filename):
    """
    This function will export the converted .xlsx file in same folder

    :param filename : Pass the string filename as parameter (Example: if your file name is "myFile.json" then pass
                    "myFile" as parameter):
    :return : this function does not return anything:
    """

    with open(f'./{filename}.json') as json_file:
        data = json.load(json_file)
        df = pd.DataFrame(data)
        df.to_excel(f'./{filename}.xlsx', index=False)


if __name__ == "__main__":
    json_to_xlsx(filename="example")
