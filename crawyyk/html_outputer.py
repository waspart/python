class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        if new_data is None or len(new_data) == 0:
            return
        for dat in new_data:
            self.data.append(dat)

    def output(self):
        fout = open('output.txt', 'a+', encoding='utf-8')
        for dat in self.data:
            fout.write(dat + '*\n')
            print(dat)
        print(len(self.data))

        fout.close()
