#    Copyright 2014 Rustici Software
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import datetime
from tincan.base import Base
from tincan.conversions.iso8601 import make_datetime

class Document(Base):
    """Document class can be instantiated from a dict, another Document, or from kwargs

    :param id: The id of this document
    :type id: unicode
    :param content_type: The content type of the content of this document
    :type content_type: unicode
    :param content: The content of this document
    :type content: bytearray
    :param etag: The etag of this document
    :type etag: unicode
    :param timestamp: The time stamp of this document
    :type timestamp: :mod:`datetime.datetime`
    """
    _props_req = [
        'id',
        'content',
        'content_type',
        'etag',
        'timestamp',
    ]

    _props = []

    _props.extend(_props_req)

    @property
    def id(self):
        """The Document id

        :setter: Tries to convert to unicode
        :setter type: str | unicode
        :rtype: unicode
        """
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, unicode) and value is not None:
            unicode(value)
        self._id = value

    @property
    def content_type(self):
        """The Document content type

        :setter: Tries to convert to unicode
        :setter type: str | unicode
        :rtype: unicode
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        if not isinstance(value, unicode) and value is not None:
            unicode(value)
        self._content_type = value

    @property
    def content(self):
        """The Document content

        :setter: Tries to convert to bytearray.
        :setter type: str | unicode | bytearray
        :rtype: bytearray
        """
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, bytearray) and value is not None:
            value = bytearray(unicode(value), "utf-8")

        self._content = value

    @property
    def etag(self):
        """The Document etag

        :setter: Tries to convert to unicode
        :setter type: str | unicode
        :rtype: unicode
        """
        return self._etag

    @etag.setter
    def etag(self, value):
        if not isinstance(value, unicode) and value is not None:
            unicode(value)
        self._etag = value

    @property
    def timestamp(self):
        """The Document time stamp

        :setter: Tries to convert to unicode
        :setter type: :class:`datetime.datetime` | unicode | str | int | float | None
        :rtype: unicode
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if value is None or isinstance(value, datetime.datetime):
            self._timestamp = value
            return

        try:
            self._timestamp = make_datetime(value)
        except Exception as e:
            e.message = (
                "Property 'timestamp' in a 'tincan.documents.%s' "
                "object must be set with a "
                "datetime.datetime, str, unicode, int or float.\n\n%s" %
                (
                    self.__class__.__name__,
                    e.message,
                )
            )
            raise e