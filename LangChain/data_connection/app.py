import load_pdf 
import csv
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.ticker import FuncFormatter

def write_to_csv(billing_data):
    csv_file = "invoices.csv"

    header = billing_data[0].keys()

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(billing_data)

# def main():
#     billing_data = load_pdf.load_all_pdfs('data')
#     print("로딩이 완료되었습니다")

#     write_to_csv(billing_data)
#     print("CSV 파일 쓰기가 완료되었습니다")

# if __name__ == "__main__":
#     main()

def draw_graph(filename):
    df = pd.read_csv("invoices.csv", thousands=",")

    df["발행일"] = pd.to_datetime(
        df["발행일"].str.replace(" ", "").str.replace("년", "-").str.replace("월", "-").str.replace("일", ""), format="%Y-%m-%d",
    )

    fig, ax = plt.subplots()
    ax.bar(df["발행일"], df["청구금액(총액)"], color='#00d9aa')
    ax.set_xlabel("date")
    ax.set_ylabel("price")
    ax.set_xticks(df["발행일"])
    ax.set_xticklabels(df["발행일"].dt.strftime("%Y-%m-%d"), rotation=45)

    ax.set_ylim(0, max(df["청구금액(총액)"]) + 100000)

    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ",")))

    plt.tight_layout()
    plt.show()

def main():
    billing_data = load_pdf.load_all_pdfs("data")
    print("데이터 로드 완료")

    write_to_csv(billing_data)
    print("CSV 파일 쓰기 완료")

    draw_graph("invoices.csv")

if __name__ == "__main__":
    main()
