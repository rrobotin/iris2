# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *


class Test(FirefoxTest):

    @pytest.mark.DETAILS(
        description="This test case checks the awesomebar search after user input.",
        locale='[en-US]',
        test_case_id="108255",
        test_suite_id="1902"
    )


    def test_run(self):

        url = LocalWeb.FIREFOX_TEST_SITE
        localhost = Pattern('localhost.png')
        localhost_2 = Pattern('localhost_2.png')
        twitter_one_off_button = Pattern('twitter_one_off_button.png')
        bing_one_off_button = Pattern('bing_one_off_button.png')
        search_in_new_tab = Pattern('search_in_new_tab.png')
        bing_search_results_localhost = Pattern('bing_search_results_localhost.png')
        twitter_search_results_localhost = Pattern('twitter_search_results_localhost.png')
        twitter_search_results_localhost_2 = Pattern('twitter_search_results_localhost_2.png')

        region = Region(0, 0, Screen().width / 2, Screen().height / 2)


        navigate(url)
        expected = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert  expected, 'Page successfully loaded, firefox logo found.'

        # Type a partial part of the above address and perform a search, in a new tab, using an one-off.
        select_location_bar()
        paste('127')
        expected = region.exists(localhost, 10)
        assert expected, 'Searched string found at the bottom of the drop-down list.'

        expected = region.exists(twitter_one_off_button, 10)
        assert expected, 'The \'Twitter\' one-off button found.'

        hover(twitter_one_off_button)

        try:
            expected = region.wait_vanish(localhost, 10)
            assert expected, 'The \'Twitter\' one-off button is highlighted.'
        except FindError:
            raise FindError('The \'Twitter\' one-off button is not highlighted.')

        right_click(twitter_one_off_button)

        expected = exists(search_in_new_tab, 10)
        assert  expected, 'The \'Search in New Tab\' option found.'

        click(search_in_new_tab)
        time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

        # Move focus to the new tab opened.
        next_tab()
        time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

        expected = region.exists(twitter_search_results_localhost.similar(0.9), 5) or region.exists(
            twitter_search_results_localhost_2, 5)
        assert  expected, 'A new tab with \'Twitter\' search results for the searched string is opened.'

        # Type a partial part of the above address and perform a search, in the same tab, using an one-off .
        select_location_bar()
        paste('127.0')

        expected = region.exists(localhost_2, 10)
        assert  expected, 'Searched string found at the bottom of the drop-down list.'

        expected = region.exists(bing_one_off_button, 10)
        assert_true(self, expected, 'The \'Bing\' one-off button found.')

        hover(bing_one_off_button)

        try:
            expected = region.wait_vanish(localhost, 10)
            assert  expected, 'The \'Bing\' one-off button is highlighted.'
        except FindError:
            raise FindError('The \'Bing\' one-off button is not highlighted.')

        click(bing_one_off_button)
        time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

        expected = region.exists(bing_search_results_localhost.similar(0.9), 10)
        assert  expected, '\'Bing\' search results are opened in the same tab.'
