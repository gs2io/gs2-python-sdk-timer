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


class CreateTimerRequest(Gs2BasicRequest):

    class Constant(Gs2Timer):
        FUNCTION = "CreateTimer"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateTimerRequest, self).__init__(params)
        if params is None:
            self.__timer_pool_name = None
            self.__callback_method = None
            self.__execute_time = None
            self.__retry_max = None
            self.__callback_body = None
            self.__callback_url = None
        else:
            self.set_timer_pool_name(params['timerPoolName'] if 'timerPoolName' in params.keys() else None)
            self.set_callback_method(params['callbackMethod'] if 'callbackMethod' in params.keys() else None)
            self.set_execute_time(params['executeTime'] if 'executeTime' in params.keys() else None)
            self.set_retry_max(params['retryMax'] if 'retryMax' in params.keys() else None)
            self.set_callback_body(params['callbackBody'] if 'callbackBody' in params.keys() else None)
            self.set_callback_url(params['callbackUrl'] if 'callbackUrl' in params.keys() else None)

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
        self.__timer_pool_name = timer_pool_name

    def with_timer_pool_name(self, timer_pool_name):
        """
        タイマープールの名前を指定します。を設定
        :param timer_pool_name: タイマープールの名前を指定します。
        :type timer_pool_name: unicode
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_timer_pool_name(timer_pool_name)
        return self

    def get_callback_method(self):
        """
        コールバックに利用するHTTPメソッドを取得
        :return: コールバックに利用するHTTPメソッド
        :rtype: unicode
        """
        return self.__callback_method

    def set_callback_method(self, callback_method):
        """
        コールバックに利用するHTTPメソッドを設定
        :param callback_method: コールバックに利用するHTTPメソッド
        :type callback_method: unicode
        """
        self.__callback_method = callback_method

    def with_callback_method(self, callback_method):
        """
        コールバックに利用するHTTPメソッドを設定
        :param callback_method: コールバックに利用するHTTPメソッド
        :type callback_method: unicode
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_callback_method(callback_method)
        return self

    def get_execute_time(self):
        """
        コールバックを実行するタイムスタンプを取得
        :return: コールバックを実行するタイムスタンプ
        :rtype: int
        """
        return self.__execute_time

    def set_execute_time(self, execute_time):
        """
        コールバックを実行するタイムスタンプを設定
        :param execute_time: コールバックを実行するタイムスタンプ
        :type execute_time: int
        """
        self.__execute_time = execute_time

    def with_execute_time(self, execute_time):
        """
        コールバックを実行するタイムスタンプを設定
        :param execute_time: コールバックを実行するタイムスタンプ
        :type execute_time: int
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_execute_time(execute_time)
        return self

    def get_retry_max(self):
        """
        最大リトライ回数を取得
        :return: 最大リトライ回数
        :rtype: int
        """
        return self.__retry_max

    def set_retry_max(self, retry_max):
        """
        最大リトライ回数を設定
        :param retry_max: 最大リトライ回数
        :type retry_max: int
        """
        self.__retry_max = retry_max

    def with_retry_max(self, retry_max):
        """
        最大リトライ回数を設定
        :param retry_max: 最大リトライ回数
        :type retry_max: int
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_retry_max(retry_max)
        return self

    def get_callback_body(self):
        """
        method に PUT/POST を指定したときに利用するリクエストボディを取得
        :return: method に PUT/POST を指定したときに利用するリクエストボディ
        :rtype: unicode
        """
        return self.__callback_body

    def set_callback_body(self, callback_body):
        """
        method に PUT/POST を指定したときに利用するリクエストボディを設定
        :param callback_body: method に PUT/POST を指定したときに利用するリクエストボディ
        :type callback_body: unicode
        """
        self.__callback_body = callback_body

    def with_callback_body(self, callback_body):
        """
        method に PUT/POST を指定したときに利用するリクエストボディを設定
        :param callback_body: method に PUT/POST を指定したときに利用するリクエストボディ
        :type callback_body: unicode
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_callback_body(callback_body)
        return self

    def get_callback_url(self):
        """
        コールバック先のURLを取得
        :return: コールバック先のURL
        :rtype: unicode
        """
        return self.__callback_url

    def set_callback_url(self, callback_url):
        """
        コールバック先のURLを設定
        :param callback_url: コールバック先のURL
        :type callback_url: unicode
        """
        self.__callback_url = callback_url

    def with_callback_url(self, callback_url):
        """
        コールバック先のURLを設定
        :param callback_url: コールバック先のURL
        :type callback_url: unicode
        :return: this
        :rtype: CreateTimerRequest
        """
        self.set_callback_url(callback_url)
        return self
