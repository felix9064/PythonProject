#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 流畅的Python 第一章示例程序1-1
# 生成一副扑克牌

from collections import namedtuple
from random import choice

# namedtuple可以生成一个带名字的tuple
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 生成扑克牌从2到A的序列
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 生成扑克牌的花色序列
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        print(self.suits)
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    @staticmethod
    def spades_high(poker_card):
        """计算一张牌在整副牌中的位置，其中梅花2为最小，黑桃A为最大"""
        rank_value = FrenchDeck.ranks.index(poker_card.rank)
        return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck[51])
    print(len(deck))

    # random库的choice方法是从列表中随机抽取一个元素
    for x in range(11):
        print(choice(deck))

    print('排序后的所有的牌为')
    for card in sorted(deck, key=FrenchDeck.spades_high):
        print(card)
