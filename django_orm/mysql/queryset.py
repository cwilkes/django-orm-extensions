# -*- coding: utf-8 -*-

from django_orm.cache.queryset import CachedQuerySet

class UnaccentQuerysetMixin(object):
    def unaccent(self, **kwargs):
        where, params = [], []
        for field, search_term in kwargs.items():
            where_sql = "%s LIKE _utf8 %%s COLLATE utf8_unicode_ci" % (field)
            where.append(where_sql)
            params.append(self._prepare_search_term(search_term))

        return self.extra(where=where, params=params)

    def _prepare_search_term(self, term):
        return u"%%%s%%" % term

    iunaccent = unaccent


class MyQuerySet(UnaccentQuerysetMixin, CachedQuerySet):
    pass
