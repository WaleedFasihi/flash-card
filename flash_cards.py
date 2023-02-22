import pandas


class FlashCards():

    def __init__(self):
        super().__init__()
        self.foreign_lang = ""
        self.english_lang = ""
        self.sample_row = {}

        try:
            self.data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/list_of_words.csv")

        self.lang = self.data.columns[0]

    def get_random_words(self):
        self.sample_row = self.data.sample()
        sample_dict = self.sample_row.squeeze()
        self.foreign_lang = sample_dict[self.lang]
        self.english_lang = sample_dict["English"]

    def remove_words(self):
        self.data = self.data.drop(self.sample_row.index)
        self.data.to_csv("data/words_to_learn.csv", index=False)
