Title: Watch it fail
Date: 2015-06-27
Category: Projects
Tags: testing, puzzles
Slug: watch-it-fail
Author: Amy Hanlon

A tenet of test-driven development is, because you're writing your test first, you _watch it fail_, and then you write code to make it pass.
Here are three examples of tests that pass even when they shouldn't. See if you can figure out why!

### 1. willow

A colleague of mine found a bunch of tests in our test suite using [mock](https://docs.python.org/3/library/unittest.mock.html) that were written like this:

    :::python
    class TestChangePrimaryEmail(unittest.TestCase):

        def test_change_primary_email_sends_email_notification(self):
            user = self.setup_test_user()
            old_email = user.email
            new_email = 'test@example.com'

            with patch.object(Emailer, 'send') as mock_send:
                user.change_primary_email(new_email)

            mock_send.assert_has_call(old_email)

This test would pass even if `user.change_primary_email` never sends an email! Why?

### 2. lying cat

Let's say we wanted to test cancelling a user, where a user object could look like this:

    :::python
    class User(object):

        ...

        def is_cancelled(self):
            return self._cancelled

        def cancel(self):
            self._cancelled = True

And then our test looks like this:

    :::python
    class TestCancelUser(unittest.TestCase):

        def test_cancel_user(self):
            user = self.setup_test_user()

            user.cancel()

            self.assertTrue(user.is_cancelled)

This test would pass even if the user wasn't cancelled! Why?

### 3. cady

Just this week we found a great bug:

* some users have special "post to wordpress" email addresses saved in their contact books
* users can send invites to join Venmo to all of the email addresses in their contact book (who aren't already Venmo users)

The combination of these two things could cause us to post an invite to join Venmo to the user's Wordpress blog. Oops.

A colleague fixed this bug by blacklisting emails with a Wordpress domain in our invite emailer and wrote a test for it like this:

    :::python
    class TestDontEmailWordpress(unittest.TestCase):

        def test_inviting_contacts_skips_wordpress_emails(self):
            user = self.setup_test_user()
            user_to_invite = self.setup_another_test_user()
            user_to_invite.email = 'blacklisted@wordpress.com'
            user.add_to_contacts(user_to_invite.email)

            with patch.object(Emailer, 'send') as mock_send:
                spam_contact_book_with_invites(user)

            self.assertFalse(mock_send.called)

This test would pass even if Wordpress emails weren't blacklisted! Why?
