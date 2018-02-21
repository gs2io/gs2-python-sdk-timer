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

class Timer(object):

    def __init__(self, params=None):
        if params is None:
            self.__timer_id = None
            self.__owner_id = None
            self.__timer_pool_id = None
            self.__callback_method = None
            self.__callback_url = None
            self.__callback_body = None
            self.__execute_time = None
            self.__retry_max = None
            self.__create_at = None
        else:
            self.set_timer_id(params['timerId'] if 'timerId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_timer_pool_id(params['timerPoolId'] if 'timerPoolId' in params.keys() else None)
            self.set_callback_method(params['callbackMethod'] if 'callbackMethod' in params.keys() else None)
            self.set_callback_url(params['callbackUrl'] if 'callbackUrl' in params.keys() else None)
            self.set_callback_body(params['callbackBody'] if 'callbackBody' in params.keys() else None)
            self.set_execute_time(params['executeTime'] if 'executeTime' in params.keys() else None)
            self.set_retry_max(params['retryMax'] if 'retryMax' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)


    def get_timer_id(self):
        """
        タイマーGRNを取得
        :return: タイマーGRN
        :rtype: unicode
        """
        return self.__timer_id

    def set_timer_id(self, timer_id):
        """
        タイマーGRNを設定
        :param timer_id: タイマーGRN
        :type timer_id: unicode
        """
        self.__timer_id = timer_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_timer_pool_id(self):
        """
        タイマープールGRNを取得
        :return: タイマープールGRN
        :rtype: unicode
        """
        return self.__timer_pool_id

    def set_timer_pool_id(self, timer_pool_id):
        """
        タイマープールGRNを設定
        :param timer_pool_id: タイマープールGRN
        :type timer_pool_id: unicode
        """
        self.__timer_pool_id = timer_pool_id

    def get_callback_method(self):
        """
        コールバックHTTPメソッドを取得
        :return: コールバックHTTPメソッド
        :rtype: unicode
        """
        return self.__callback_method

    def set_callback_method(self, callback_method):
        """
        コールバックHTTPメソッドを設定
        :param callback_method: コールバックHTTPメソッド
        :type callback_method: unicode
        """
        self.__callback_method = callback_method

    def get_callback_url(self):
        """
        コールバックURLを取得
        :return: コールバックURL
        :rtype: unicode
        """
        return self.__callback_url

    def set_callback_url(self, callback_url):
        """
        コールバックURLを設定
        :param callback_url: コールバックURL
        :type callback_url: unicode
        """
        self.__callback_url = callback_url

    def get_callback_body(self):
        """
        コールバックボディ(PUT/POSTのときのみ有効)を取得
        :return: コールバックボディ(PUT/POSTのときのみ有効)
        :rtype: unicode
        """
        return self.__callback_body

    def set_callback_body(self, callback_body):
        """
        コールバックボディ(PUT/POSTのときのみ有効)を設定
        :param callback_body: コールバックボディ(PUT/POSTのときのみ有効)
        :type callback_body: unicode
        """
        self.__callback_body = callback_body

    def get_execute_time(self):
        """
        コールバック時間(エポック秒)を取得
        :return: コールバック時間(エポック秒)
        :rtype: int
        """
        return self.__execute_time

    def set_execute_time(self, execute_time):
        """
        コールバック時間(エポック秒)を設定
        :param execute_time: コールバック時間(エポック秒)
        :type execute_time: int
        """
        self.__execute_time = execute_time

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

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def to_dict(self):
        return { 
            "timerId": self.__timer_id,
            "ownerId": self.__owner_id,
            "timerPoolId": self.__timer_pool_id,
            "callbackMethod": self.__callback_method,
            "callbackUrl": self.__callback_url,
            "callbackBody": self.__callback_body,
            "executeTime": self.__execute_time,
            "retryMax": self.__retry_max,
            "createAt": self.__create_at,
        }