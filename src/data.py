class Data:
    def __init__(self, parsed):
        self.data = self.__from_parsed_to_data(parsed)

    def __from_parsed_to_data(self, parsed):
        return parsed

    def to_data(self):
        return self.data

    def to_cacheable(self):
        return self.data.to_json(orient='split')

    def to_tabular(self):
        return self.data.to_dict('records')

class Regs(Data):

    def from_parsed_to_data(parsed):
        return parsed

    def from_data_to_cacheable(data):
        return data

    def from_cacheable_to_data(cacheabel):
        return cacheabel

    def from_data_to_tabular(data):
        return data

class Foods(Data):

    def from_parsed_to_data(parsed):
        return parsed

    def from_data_to_cacheable(data):
        return data

    def from_cacheable_to_data(cacheabel):
        return cacheabel

    def from_data_to_tabular(data):
        return data
