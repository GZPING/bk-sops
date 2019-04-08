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

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_auto_20180717_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleservice',
            name='celery_id',
        ),
        migrations.RemoveField(
            model_name='scheduleservice',
            name='celery_info_lock',
        ),
        migrations.RemoveField(
            model_name='scheduleservice',
            name='is_frozen',
        ),
        migrations.RemoveField(
            model_name='scheduleservice',
            name='schedule_date',
        ),
    ]
