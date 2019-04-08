# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.test import TestCase
from pipeline.core.flow.base import FlowNode
from pipeline.core.flow.gateway import Gateway, ParallelGateway
from pipeline.exceptions import InvalidOperationException


class TestParallelGateway(TestCase):
    def test_parallel_gateway(self):
        gw_id = '1'
        pl_gateway = ParallelGateway(gw_id, 'cvg')
        self.assertTrue(isinstance(pl_gateway, FlowNode))
        self.assertTrue(isinstance(pl_gateway, Gateway))

    def test_next(self):
        gw_id = '1'
        pl_gateway = ParallelGateway(gw_id, None, None)
        self.assertRaises(InvalidOperationException, pl_gateway.next)
