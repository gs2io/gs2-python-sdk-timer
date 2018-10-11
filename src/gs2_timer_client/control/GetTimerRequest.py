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


class GetTimerRequest(Gs2BasicRequest):

    class Constant(Gs2Timer):
        FUNCTION = "GetTimer"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetTimerRequest, self).__init__(params)
        if params is None:
            self.__timer_pool_name = None
        else:
            self.set_timer_pool_name(params['timerPoolName'] if 'timerPoolName' in params.keys() else None)
        if params is None:
            self.__timer_id = None
        else:
            self.set_timer_id(params['timerId'] if 'timerId' in params.keys() else None)

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
        if timer_pool_name is not None and not (isinstance(timer_pool_name, str) or isinstance(timer_pool_name, unicode)):
            raise TypeError(type(timer_pool_name))
        self.__timer_pool_name = timer_pool_name

    def with_timer_pool_name(self, timer_pool_name):
        """
        タイマープールの名前を指定します。を設定
        :param timer_pool_name: タイマープールの名前を指定します。
        :type timer_pool_name: unicode
        :return: this
        :rtype: GetTimerRequest
        """
        self.set_timer_pool_name(timer_pool_name)
        return self

    def get_timer_id(self):
        """
        タイマーのIDを指定します。を取得
        :return: タイマーのIDを指定します。
        :rtype: unicode
        """
        return self.__timer_id

    def set_timer_id(self, timer_id):
        """
        タイマーのIDを指定します。を設定
        :param timer_id: タイマーのIDを指定します。
        :type timer_id: unicode
        """
        if timer_id is not None and not (isinstance(timer_id, str) or isinstance(timer_id, unicode)):
            raise TypeError(type(timer_id))
        self.__timer_id = timer_id

    def with_timer_id(self, timer_id):
        """
        タイマーのIDを指定します。を設定
        :param timer_id: タイマーのIDを指定します。
        :type timer_id: unicode
        :return: this
        :rtype: GetTimerRequest
        """
        self.set_timer_id(timer_id)
        return self
