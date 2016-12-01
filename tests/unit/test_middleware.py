import datetime

import pytest
from django.test.client import Client
from freezegun import freeze_time

from tests.factories.segment import (
    ReferralRuleFactory, SegmentFactory, TimeRuleFactory)
from tests.factories.site import SiteFactory


@pytest.mark.django_db
class TestUserSegmenting(object):

    def setup(self):
        """
        Sets up a site root to test segmenting
        """
        self.site = SiteFactory()

    def test_no_segments(self, client):
        request = client.get('/')

        assert client.session['segments'] == []

    @freeze_time("10:00:00")
    def test_time_segment(self, client):
        time_only_segment = SegmentFactory(name='Time only')
        time_rule = TimeRuleFactory(
            start_time=datetime.time(8, 0, 0),
            end_time=datetime.time(23, 0, 0),
            segment=time_only_segment)

        request = client.get('/')

        assert client.session['segments'][0]['encoded_name'] == 'time-only'

    def test_referral_segment(self, client):
        referral_segment = SegmentFactory(name='Referral')
        referral_rule = ReferralRuleFactory(
            regex_string="test.test",
            segment=referral_segment
        )

        client.get('/', **{ 'HTTP_REFERER': 'test.test'})

        assert client.session['segments'][0]['encoded_name'] == 'referral'

    @freeze_time("10:00:00")
    def test_time_and_referral_segment(self, client):
        segment = SegmentFactory(name='Both')
        time_rule = TimeRuleFactory(
            start_time=datetime.time(8, 0, 0),
            end_time=datetime.time(23, 0, 0),
            segment=segment
        )
        referral_rule = ReferralRuleFactory(
            regex_string="test.test",
            segment=segment
        )

        client.get('/', **{ 'HTTP_REFERER': 'test.test'})

        assert client.session['segments'][0]['encoded_name'] == 'both'

    @freeze_time("7:00:00")
    def test_no_time_but_referral_segment(self, client):
        segment = SegmentFactory(name='Not both')
        time_rule = TimeRuleFactory(
            start_time=datetime.time(8, 0, 0),
            end_time=datetime.time(23, 0, 0),
            segment=segment
        )
        referral_rule = ReferralRuleFactory(
            regex_string="test.test",
            segment=segment
        )

        client.get('/', **{ 'HTTP_REFERER': 'test.test'})

        assert len(client.session['segments']) == 0

    @freeze_time("9:00:00")
    def test_time_but_no_referral_segment(self, client):
        segment = SegmentFactory(name='Not both')
        time_rule = TimeRuleFactory(
            start_time=datetime.time(8, 0, 0),
            end_time=datetime.time(23, 0, 0),
            segment=segment
        )
        referral_rule = ReferralRuleFactory(
            regex_string="test.test",
            segment=segment
        )

        client.get('/')

        assert len(client.session['segments']) == 0