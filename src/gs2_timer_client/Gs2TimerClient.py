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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2TimerClient(AbstractGs2Client):

    ENDPOINT = "timer"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2TimerClient, self).__init__(credential, region)

    def create_timer_pool(self, request):
        """
        タイマープールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_timer_client.control.CreateTimerPoolRequest.CreateTimerPoolRequest
        :return: 結果
        :rtype: gs2_timer_client.control.CreateTimerPoolResult.CreateTimerPoolResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.CreateTimerPoolRequest import CreateTimerPoolRequest
        from gs2_timer_client.control.CreateTimerPoolResult import CreateTimerPoolResult
        return CreateTimerPoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool",
            service=self.ENDPOINT,
            component=CreateTimerPoolRequest.Constant.MODULE,
            target_function=CreateTimerPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_timer_pool(self, request):
        """
        タイマープールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_timer_client.control.DeleteTimerPoolRequest.DeleteTimerPoolRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.DeleteTimerPoolRequest import DeleteTimerPoolRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "",
            service=self.ENDPOINT,
            component=DeleteTimerPoolRequest.Constant.MODULE,
            target_function=DeleteTimerPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_timer_pool(self, request):
        """
        タイマープールの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_timer_client.control.DescribeTimerPoolRequest.DescribeTimerPoolRequest
        :return: 結果
        :rtype: gs2_timer_client.control.DescribeTimerPoolResult.DescribeTimerPoolResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.DescribeTimerPoolRequest import DescribeTimerPoolRequest

        from gs2_timer_client.control.DescribeTimerPoolResult import DescribeTimerPoolResult
        return DescribeTimerPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool",
            service=self.ENDPOINT,
            component=DescribeTimerPoolRequest.Constant.MODULE,
            target_function=DescribeTimerPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_timer_pool(self, request):
        """
        タイマープールを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_timer_client.control.GetTimerPoolRequest.GetTimerPoolRequest
        :return: 結果
        :rtype: gs2_timer_client.control.GetTimerPoolResult.GetTimerPoolResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.GetTimerPoolRequest import GetTimerPoolRequest

        from gs2_timer_client.control.GetTimerPoolResult import GetTimerPoolResult
        return GetTimerPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "",
            service=self.ENDPOINT,
            component=GetTimerPoolRequest.Constant.MODULE,
            target_function=GetTimerPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_timer_pool(self, request):
        """
        タイマープールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_timer_client.control.UpdateTimerPoolRequest.UpdateTimerPoolRequest
        :return: 結果
        :rtype: gs2_timer_client.control.UpdateTimerPoolResult.UpdateTimerPoolResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.UpdateTimerPoolRequest import UpdateTimerPoolRequest
        from gs2_timer_client.control.UpdateTimerPoolResult import UpdateTimerPoolResult
        return UpdateTimerPoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "",
            service=self.ENDPOINT,
            component=UpdateTimerPoolRequest.Constant.MODULE,
            target_function=UpdateTimerPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_timer(self, request):
        """
        タイマーを新規作成します<br>
        <br>
        タイマーの timestamp は秒単位で指定できますが、<br>
        指定した時刻以降で通常1分以内にコールバックURLは呼び出されます<br>
        <br>
        混雑時などには数分の遅れが出ることがあります<br>
        <br>
        タイマーによるコールバックは指定されたリトライ回数試行します<br>
        タイムアウトなどの理由により、実際には通信が到達しているにもかかわらず、リトライが発生する可能性があります<br>
        <br>
        コールバックは同等のリクエストが複数回呼び出されても問題なく動作するように設計してください<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_timer_client.control.CreateTimerRequest.CreateTimerRequest
        :return: 結果
        :rtype: gs2_timer_client.control.CreateTimerResult.CreateTimerResult
        """
        body = { 
            "callbackMethod": request.get_callback_method(),
            "callbackUrl": request.get_callback_url(),
            "executeTime": request.get_execute_time(),
        }

        if request.get_callback_body() is not None:
            body["callbackBody"] = request.get_callback_body()
        if request.get_retry_max() is not None:
            body["retryMax"] = request.get_retry_max()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.CreateTimerRequest import CreateTimerRequest
        from gs2_timer_client.control.CreateTimerResult import CreateTimerResult
        return CreateTimerResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "/timer",
            service=self.ENDPOINT,
            component=CreateTimerRequest.Constant.MODULE,
            target_function=CreateTimerRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_timer(self, request):
        """
        タイマーを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_timer_client.control.DeleteTimerRequest.DeleteTimerRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.DeleteTimerRequest import DeleteTimerRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "/timer/" + str(("null" if request.get_timer_id() is None or request.get_timer_id() == "" else request.get_timer_id())) + "",
            service=self.ENDPOINT,
            component=DeleteTimerRequest.Constant.MODULE,
            target_function=DeleteTimerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_timer(self, request):
        """
        タイマーの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_timer_client.control.DescribeTimerRequest.DescribeTimerRequest
        :return: 結果
        :rtype: gs2_timer_client.control.DescribeTimerResult.DescribeTimerResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.DescribeTimerRequest import DescribeTimerRequest

        from gs2_timer_client.control.DescribeTimerResult import DescribeTimerResult
        return DescribeTimerResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "/timer",
            service=self.ENDPOINT,
            component=DescribeTimerRequest.Constant.MODULE,
            target_function=DescribeTimerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_timer(self, request):
        """
        タイマーを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_timer_client.control.GetTimerRequest.GetTimerRequest
        :return: 結果
        :rtype: gs2_timer_client.control.GetTimerResult.GetTimerResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_timer_client.control.GetTimerRequest import GetTimerRequest

        from gs2_timer_client.control.GetTimerResult import GetTimerResult
        return GetTimerResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/timerPool/" + str(("null" if request.get_timer_pool_name() is None or request.get_timer_pool_name() == "" else request.get_timer_pool_name())) + "/timer/" + str(("null" if request.get_timer_id() is None or request.get_timer_id() == "" else request.get_timer_id())) + "",
            service=self.ENDPOINT,
            component=GetTimerRequest.Constant.MODULE,
            target_function=GetTimerRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
