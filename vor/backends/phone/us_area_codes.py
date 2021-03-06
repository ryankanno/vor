#!/usr/bin/env python
# -*- coding: utf-8 -*-


US_STATE_TO_AREA_CODE = (
    ('AL', ['205', '251', '256', '334', '659', '938']),
    ('AK', ['907']),
    ('AZ', ['480', '520', '602', '623', '928']),
    ('AR', ['327', '479', '501', '870']),
    ('CA', []),
    ('CO', ['303', '719', '720', '970']),
    ('CT', ['203', '475', '860', '959']),
    ('DE', ['302']),
    ('DC', ['202']),
    ('FL', ['239', '305', '321', '352', '386', '407', '561', '689', '727',
            '754', '772', '786', '813', '850', '863', '904', '927', '941',
            '954']),
    ('GA', ['229', '404', '470', '478', '678', '706', '762', '770', '912']),
    ('HI', []),
    ('ID', []),
    ('IL', []),
    ('IN', []),
    ('IA', []),
    ('KS', []),
    ('KY', []),
    ('LA', []),
    ('ME', []),
    ('MD', []),
    ('MA', []),
    ('MI', []),
    ('MN', []),
    ('MS', []),
    ('MO', []),
    ('MT', []),
    ('NE', []),
    ('NV', []),
    ('NH', []),
    ('NJ', []),
    ('NM', []),
    ('NY', []),
    ('NC', []),
    ('ND', []),
    ('OH', []),
    ('OK', []),
    ('OR', []),
    ('PA', []),
    ('RI', []),
    ('SC', []),
    ('SD', []),
    ('TN', []),
    ('TX', []),
    ('UT', []),
    ('VT', []),
    ('VA', []),
    ('WA', []),
    ('WV', []),
    ('WI', []),
    ('WY', [])
)


class UsAreaCodes(object):
    def __init__(self, *args, **kwargs):
        super(UsAreaCodes, self).__init__(*args, **kwargs)

# vim: filetype=python
