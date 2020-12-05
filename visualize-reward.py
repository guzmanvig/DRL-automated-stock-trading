import docx

doc = docx.opendocx("./logs/currency_run_1.docx")
a2ctext = open('./results/a2c-logs-results.txt', 'w')
ddpgtext = open('./results/ddpg-logs-results.txt', 'w')
ppotext = open('./results/ppo-logs-results.txt', 'w')
all_paras = docx.getdocumenttext(doc)
a2c, ddpg, ppo = False, False, False


class DocReader:

    def __init__(self):
        print("Started writing")

    def get_algorithm(self, algo):
        switcher = {
            0: b'A2C Training',
            1: b'PPO Training',
            2: b'DDPG Training'
        }
        return switcher.get(algo, "Invalid algorithm")

    def write_txt(self):
        for para_text in all_paras:
            line = para_text.encode("utf-8")
            if self.get_algorithm(0) in line:
                a2c, ddpg, ppo = True, False, False
            elif self.get_algorithm(1) in line:
                a2c, ddpg, ppo = False, False, True
            elif self.get_algorithm(2) in line:
                a2c, ddpg, ppo = False, True, False
            else:
                print(line)

            if b'total_reward' in line:
                if a2c:
                    a2ctext.write('\n\n'.join(line))
                    # docx.savedocx(a2ctext)
                elif ddpg:
                    print(line)
                    ddpgtext.write('\n\n'.join(str(line)))
                elif ppo:
                    ppotext.write('\n\n'.join(line))
        a2c, ddpg, ppo = False, False, False

        # Create our properties, contenttypes, and other support files
        title = 'Python docx demo'
        subject = 'A practical example of making docx from Python'
        creator = 'Mike MacCana'
        keywords = ['python', 'Office Open XML', 'Word']

        coreprops = docx.coreproperties(title=title, subject=subject, creator=creator,
                                        keywords=keywords)
        appprops = docx.appproperties()
        contenttypes = docx.contenttypes()
        websettings = docx.websettings()
        wordrelationships = docx.wordrelationships(None)

        docx.savedocx(a2ctext, coreprops, appprops, contenttypes, websettings,
                      wordrelationships, 'Welcome to the Python docx module.docx')
        docx.savedocx(ddpgtext, coreprops, appprops, contenttypes, websettings,
                      wordrelationships, 'Welcome to the Python docx module.docx')
        docx.savedocx(ppotext, coreprops, appprops, contenttypes, websettings,
                      wordrelationships, 'Welcome to the Python docx module.docx')


def __main__():
    doc_reader = DocReader()
    doc_reader.write_txt()


__main__()
