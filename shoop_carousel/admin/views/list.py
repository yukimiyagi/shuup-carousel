# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from shoop.admin.utils.picotable import Column, TextFilter
from shoop.admin.utils.views import PicotableListView

from shoop_carousel.models import Carousel


class CarouselListView(PicotableListView):
    model = Carousel
    columns = [
        Column(
            "name",
            _("Name"),
            sort_field="translations__name",
            display="name",
            filter_config=TextFilter(filter_field="translations__name", placeholder=_("Filter by name..."))
        ),
    ]
