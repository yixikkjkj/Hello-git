import logging
import os
import csv

import chardet
from numpy.core.fromnumeric import size


import jieba
import jieba.analyse
from gensim.models import word2vec
from sklearn.feature_extraction.text import TfidfVectorizer

logger = logging.getLogger(__name__)

class BaseParser:
    def __init__(self, source_path, column_names=None):
        self.path = source_path

        if column_names is None:
            column_names = {
                'goods_name': ['商品名', '商品名称'],
            }
        self.column_names = column_names
        self.column_indexes = {}

    def _match_index(self, first_row):
        """
        使用第一行的内容，得到需要取得的数据的 index
        """
        for key, names in self.column_names.items():
            for name in names:
                try:
                    index = first_row.index(name)
                    self.column_indexes[key] = index
                    break
                except ValueError:
                    continue
            else:
                ValueError('未找到对应列')

    def _parser(self, data_list):
        """
        解析每一行的内容
        """
        data = {}
        for key, index in self.column_indexes.items():
            if index >= len(data_list):
                data[key] = ''
                continue
            data[key] = data_list[index].strip()
        return data


class CsvParser(BaseParser):
    def __init__(self, source_path, column_names=None, file_encoding='utf-8'):
        """
        csv parser
        增加encode参数
        """
        super(CsvParser, self).__init__(source_path, column_names)
        self.file_encoding = file_encoding

    def __iter__(self):
        self._try_detect_encoding()
        with open(self.path, 'rb') as file_obj:
            reader = csv.reader(self._remove_null_byte(file_obj))
            try:
                head_row = next(reader)
            except StopIteration:
                logger.warning('read csv [%s] with no header', self.path)
                return

            try:
                self._match_index(head_row)
            except ValueError:
                logger.warning('read csv [%s] with no columns', self.path, str(head_row))
                return

            for line in reader:
                yield self._parser(line)

    def _remove_null_byte(self, file_obj):
        for binary_line in file_obj:
            no_null_line = binary_line.replace(b'\x00', b'')
            yield no_null_line.decode(self.file_encoding, 'ignore')

    def _try_detect_encoding(self):
        with open(self.path, 'rb') as file_obj:
            head_line = file_obj.readline()
            head_encoding = chardet.detect(head_line)
            if head_encoding['confidence'] >= 0.8 and \
                    head_encoding['encoding'] != self.file_encoding:  # 超过 80% 的识别，认为识别正确，记录并且使用 encoding
                logger.info('file %s detect encoding %s differ from %s/%s',
                            self.path, head_encoding['encoding'],
                            self.file_encoding, head_encoding['confidence'])
                self.file_encoding = head_encoding['encoding']


def init_jieba():
    jieba.suggest_freq('礼物', True)


def goods_name_parser(source_path):
    if not os.path.exists(source_path) or not os.path.isfile(source_path):
        raise ValueError('文件不存在')

    extension = os.path.basename(source_path).split('.').pop()
    if extension == 'csv':
        parser = CsvParser(source_path)
    else:
        raise ValueError('未知的类型')
    return parser


def pre_handle(source_path, target_path):
    init_jieba()
    name_list = []
    for goods_data in goods_name_parser(source_path):
        name_list.append(' '.join(jieba.cut(goods_data['goods_name'])))

    data = '\n'.join(name_list)
    with open(target_path, 'w+') as fileobj:
        fileobj.write(data)


def tezheng_chuli(cut_path):
    data = []
    with open(cut_path, 'r') as fileobj:
        data = fileobj.read()
    vector = TfidfVectorizer(stop_words=[])
    vector.fit_transform([[], []])


def build_model(cut_path):
    sentences = word2vec.LineSentence(cut_path)
    model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=3, size=100)
    return model



def test_model(model):
    count = 10
    for key in model.wv.similar_by_word('生日', topn=100):
        # print(key)
        if (len(key[0]) == 3):
            print(key[0], key[1])
            count -= 1
            if count <= 0:
                break


def main():
    source_path = data_dir + '/taobao-order_2020-11-09_15_00_1604905243388830915_36697614.snappy'
    cut_path = data_dir + '/taobao-order_2020-11-09_15_00_1604905243388830915_36697614_cut'
    pre_handle(source_path, cut_path)
    # tezheng_chuli()
    old_model = load_model(model_path)
    model = build_model(cut_path, model=old_model)
    save_model(model, model_path)
    # test_model(model)




def save_model(model, model_path):
    model.save(model_path)


def load_model():
    model_path = '/Users/wangyijun/Documents/用户商品模型数据.txt'
    model = word2vec.Word2Vec.load(model_path)
    test_model(model)


if __name__ == "__main__":
    print('main in')
    load_model()


def test():
    file_name = data_dir + '/taobao-order_2020-11-09_15_00_1604905243388830915_36697614.snappy'
    parser = goods_name_parser(file_name)
    parser.set_column_names({'goods_name': ['title']})
    name_list = []
    for goods_data in parser:
        name_list.append(goods_data['goods_name'])

    data = '\n'.join(name_list)
    with open(data_dir + '/test.txt', 'w+') as file_obj:
        file_obj.write(data)


def test2():
    init_jieba()
    hashed_word = set()
    with open(data_dir + '/test.txt', 'r') as file_obj:
        for line in file_obj.readlines():
            cut_list = list(jieba.posseg.cut(line, HMM=True, use_paddle=True))
            for word, flag in cut_list:
                word_hash = hash(word)
                if not word_hash in hashed_word:

                print(word, flag)
            break


def test3():
    file_list = [
        'taobao-order_2020-11-09_15_00_1604905243388830915_36697614.snappy',
        'taobao-order_2020-11-09_15_02_1604905369481629671_36698007.snappy',
        'taobao-order_2020-11-09_15_03_1604905425849770162_36698161.snappy',
        'taobao-order_2020-11-09_15_02_1604905363862322396_36697986.snappy',
        'taobao-order_2020-11-09_15_00_1604905244204526265_36697624.snappy',
        'taobao-order_2020-11-09_15_03_1604905433349542488_36698188.snappy',
        'taobao-order_2020-11-09_15_01_1604905310437634952_36697827.snappy',
        'taobao-order_2020-11-09_15_05_1604905500293208750_36698396.snappy',
        'taobao-order_2020-11-09_15_01_1604905312524758494_36697836.snappy',
        'taobao-order_2020-11-09_15_05_1604905506217919052_36698415.snappy',
    ]
    model = word2vec_model
    init_jieba()
    for file_name in file_list:
        source_path = data_dir + '/' + file_name
        print(source_path)
        cut_path = data_dir + '/' + file_name.split('.')[0] + '.cut'
        pre_handle(source_path, cut_path)
        model = build_model(cut_path, model=model)
    save_model(model)
