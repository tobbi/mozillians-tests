#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.mozillians_page import MozilliansStartPage
from unittestzero import Assert


class TestAboutPage:

    def test_about_page(self, mozwebqa):
        home_page = MozilliansStartPage(mozwebqa)
        about_mozillians_page = home_page.click_about_link()
        Assert.true(about_mozillians_page.is_privacy_section_present)
        Assert.true(about_mozillians_page.is_get_involved_section_present)
