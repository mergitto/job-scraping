# -*- coding: utf-8 -*-

from natto import MeCab
mc = MeCab('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

def parser_mecab(text):
    words = []
    for n in mc.parse(text, as_nodes=True):
        node = n.feature.split(',');
        if node[0] != '助詞' and node[0] != '助動詞' and node[0] != '記号' and node[1] != '数':
            if node[0] == '動詞':
                words.append(node[6])
            elif node[0] == 'BOS/EOS':
                continue
            else:
                words.append(n.surface)
    return words

