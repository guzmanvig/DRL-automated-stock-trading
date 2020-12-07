import docx
import matplotlib.pyplot as plt


class DocReader:

    def __init__(self, doc_path):
        print("Started writing")
        self.doc = docx.opendocx(doc_path)
        self.all_paras = docx.getdocumenttext(self.doc)

    def write_txt(self):
        date_from_list = []
        date_to_list = []
        reward_list = []
        initial_asset = 1000000
        for para_text in self.all_paras:
            line = para_text
            if 'Trading from: ' in line:
                trade_line = ' '.join(line.split())
                date_from = trade_line.split(" ")[2]
                date_to = trade_line.split(" ")[4]
                date_from = date_from[:4] + "-" + date_from[4:6] + "-" + date_from[6:8]
                date_to = date_to[:4] + "-" + date_to[4:6] + "-" + date_to[6:8]
                date_from_list.append(date_from)
                date_to_list.append(date_to)
                print(date_from + " " + date_to + " ")
            if 'end_total_asset' in line:
                end_asset = int(line.split(":")[1].split(".")[0])
                reward = abs(end_asset - initial_asset) * 100 / initial_asset
                reward_list.append(reward)
                print(reward)
        print(date_from_list)
        print(date_to_list)
        print(reward_list)
        plt.plot(date_to_list, reward_list)
        plt.show()


def __main__():
    doc_reader = DocReader("./logs/currency_run_1.docx")
    doc_reader.write_txt()


__main__()
