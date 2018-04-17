# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_timer_client.Gs2Timer import Gs2Timer


class DescribeTimerRequest(Gs2BasicRequest):

    class Constant(Gs2Timer):
        FUNCTION = "DescribeTimer"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeTimerRequest, self).__init__(params)
        if params is None:
            self.__timer_pool_name = None
        else:
            self.set_timer_pool_name(params['timerPoolName'] if 'timerPoolName' in params.keys() else None)
        if params is None:
            self.__page_token = None
        else:
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
        if params is None:
            self.__limit = None
        else:
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

    def get_timer_pool_name(self):
        """
        タイマープールの名前を指定します。を取得
        :return: タイマープールの名前を指定します。
        :rtype: unicode
        """
        return self.__timer_pool_name

    def set_timer_pool_name(self, timer_pool_name):
        """
        タイマープールの名前を指定します。を設定
        :param timer_pool_name: タイマープールの名前を指定します。
        :type timer_pool_name: unicode
        """
        if timer_pool_name and not (isinstance(timer_pool_name, str) or isinstance(timer_pool_name, unicode)):
            raise TypeError(type(timer_pool_name))
        self.__timer_pool_name = timer_pool_name

    def with_timer_pool_name(self, timer_pool_name):
        """
        タイマープールの名前を指定します。を設定
        :param timer_pool_name: タイマープールの名前を指定します。
        :type timer_pool_name: unicode
        :return: this
        :rtype: DescribeTimerRequest
        """
        self.set_timer_pool_name(timer_pool_name)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if page_token and not (isinstance(page_token, str) or isinstance(page_token, unicode)):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeTimerRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if limit and not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeTimerRequest
        """
        self.set_limit(limit)
        return self
