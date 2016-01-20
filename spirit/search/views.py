# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from haystack.views import SearchView as BaseSearchView

from ..core.utils.paginator import yt_paginate


class SearchView(BaseSearchView):

    def build_page(self):
        paginator = None
        page = yt_paginate(
            self.results,
            ##@TODO create djconfig replacement

            per_page='0',
            page_number=self.request.GET.get('page', 1)
        )
        return paginator, page
