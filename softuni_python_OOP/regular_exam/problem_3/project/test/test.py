from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.sm = SocialMedia("Test", "Instagram", 100, "Some Content")

    def test_correct_init(self):
        self.assertEqual("Test", self.sm._username)
        self.assertEqual("Instagram", self.sm._platform)
        self.assertEqual("Some Content", self.sm._content_type)
        self.assertEqual(100, self.sm._followers)
        self.assertEqual([], self.sm._posts)

    def test_platform_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sm.platform = "Meta"

        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        expected = f"Platform should be one of {allowed_platforms}"
        self.assertEqual(expected, str(ve.exception))

    def test_platform_setter_works_correctly(self):
        self.sm.platform = "YouTube"
        self.assertEqual("YouTube", self.sm.platform)

    def test_followers_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sm.followers = -1
        expected = "Followers cannot be negative."
        self.assertEqual(expected, str(ve.exception))

    def test_followers_setter_works_correctly(self):
        self.sm.followers = 0
        self.assertEqual(0, self.sm.followers)
        self.sm.followers = 1
        self.assertEqual(1, self.sm.followers)

    def test_validate_platform_private_method_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sm._validate_and_set_platform("Test")

        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        expected = f"Platform should be one of {allowed_platforms}"
        self.assertEqual(expected, str(ve.exception))

    def test_validate_platform_private_method_correct(self):
        self.sm._validate_and_set_platform("Twitter")
        self.assertEqual("Twitter", self.sm.platform)

    def test_create_post(self):
        result = self.sm.create_post("Test Content")
        expected = "New Some Content post created by Test on Instagram."
        self.assertEqual(expected, result)
        new_post = {'content': "Test Content", 'likes': 0, 'comments': []}
        self.assertEqual([new_post], self.sm._posts)
        self.assertEqual(1, len(self.sm._posts))
        result = self.sm.create_post("Test Content1")
        self.assertEqual(2, len(self.sm._posts))


    def test_like_post_works_correct(self):
        new_post = {'content': "Test Content", 'likes': 0, 'comments': []}
        new_post1 = {'content': "Test Content1", 'likes': 0, 'comments': []}
        self.sm._posts.append(new_post)
        self.sm._posts.append(new_post1)
        result = self.sm.like_post(0)
        result1 = self.sm.like_post(1)
        expected = "Post liked by Test."
        self.assertEqual(expected, result)
        self.assertEqual(expected, result1)
        self.assertEqual(1, self.sm._posts[0]['likes'])
        self.assertEqual(1, self.sm._posts[1]['likes'])
        result2 = self.sm.like_post(0)
        self.assertEqual(2, self.sm._posts[0]['likes'])


    def test_like_post_return_maximum_likes_message(self):
        new_post = {'content': "Test Content", 'likes': 10, 'comments': []}
        self.sm._posts.append(new_post)
        result = self.sm.like_post(0)
        expected = "Post has reached the maximum number of likes."
        self.assertEqual(expected, result)
        self.assertEqual(10, self.sm._posts[0]['likes'])

    def test_message_invalid_post_index(self):
        self.sm.create_post("Test Content")
        result = self.sm.like_post(1)
        expected = "Invalid post index."
        self.assertEqual(expected, result)
        self.assertFalse(len(self.sm._posts) == 2)

    def test_comment_on_post_correct(self):
        self.sm.create_post("Test Content")
        self.sm.create_post("Test Content1")
        result = self.sm.comment_on_post(0, "Test Comment")
        expected = "Comment added by Test on the post."
        self.assertEqual(expected, result)
        self.assertEqual([{'comment': "Test Comment", 'user': "Test"}], self.sm._posts[0]["comments"])
        self.assertEqual(1, len(self.sm._posts[0]["comments"]))

    def test_comment_on_post_short_comment_message(self):
        self.sm.create_post("Test Content")
        self.sm.create_post("Test Content1")
        result = self.sm.comment_on_post(0, "Test")
        expected = "Comment should be more than 10 characters."
        self.assertEqual(expected, result)
        self.assertEqual(0, len(self.sm._posts[0]["comments"]))
        self.assertEqual(0, len(self.sm._posts[1]["comments"]))


if __name__ == '__main__':
    main()
