from tornado.web import url

from apps.community.handler import *

urlpattern = (
    url("/groups/", GroupHandler),
    url("/groups/([0-9]+)/", GroupDetailHanlder),
    url("/groups/([0-9]+)/members/", GroupMemberHandler),
    url("/groups/([0-9]+)/posts/", PostHandler),

    url("/posts/([0-9]+)/", PostDetailHandler),

    #评论
    url("/posts/([0-9]+)/comments/", PostCommentHanlder),
    url("/comments/([0-9]+)/replys/", CommentReplyHandler),
    url("/comments/([0-9]+)/likes/", CommentsLikeHanlder),
)