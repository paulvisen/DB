# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME
from sqlalchemy.ext.declarative import declarative_base

from model import *
from modelV2 import  *
ORIGINAL_DB_CONNECT_STRING = 'mysql+mysqldb://root:SEUqianshou2015@218.244.147.240:3306/flasktestdb?charset=utf8'
New_DB_CONNECT_STRING ='mysql+mysqldb://root:qwer@localhost/wemedev?charset=utf8'


engine_original = create_engine(ORIGINAL_DB_CONNECT_STRING)
engine_now = create_engine(New_DB_CONNECT_STRING)
DBSession_original = sessionmaker(bind=engine_original)
DBSession_now = sessionmaker(bind=engine_now)
session1 = DBSession_original()
session2 = DBSession_now()

# 因为主键关系的存在，按照如下的步骤导出对应的数据
# 1. avatar  头像  ok
# 2. user  用户 ok
# 3. activity 活动 ok
# 4. activityimage 活动照片 ok
# 5. android_version 安卓版本 ok
# 6. checkmsg 短信验证 ok
# 7. topic 话题 ok
# 8. post 文章 ok
# 9. comment 评论 ok
# 10. comment_image 评论图片 ok
# 11. follow_id 关注 ok
# 12. foodcard 食物照片 ok
# 13. like_user_id 喜欢关系  ok
# 14. message消息  ok
# 15. message_image 图片消息
# 16. post_image 文章图片 ok
# 17. activity_poseter_image 海报照片 ok
# 18. Report 举报 ok
# 19. topic_image 话题照片 ok
# 20. user_attend_activity_realtion 用户参加活动关系 ok
# 21. user_image 用户照片 ok
# 22. user_like_activity_relation 用户喜欢关系表 ok
# 23. user_like_foodcard  用户食物卡片喜欢关系 ok
# 24. user_like_post  用户文章喜欢关系 ok
# 25. user_visit 用户访问关系  ok
# 26. activity_life_image 用户生活照 ok
# 27. community_poster_image 社区轮播照片
# 28. user_like_comment  用户喜欢评论


#
# print "*****************1  2**************************"
#
# print "strat transfer talbe User AvatarVoices "
# query = session1.query(User)
# for user in query:
#     #关联avatarvoice
#     avatarVoice = session1.query(AvatarVoice).filter_by(userid=user.id).first()
#     if avatarVoice is not None:
#         avatarVoiceV2 =AvatarVoiceV2(avatar_number = avatarVoice.avatar_number,avatar_url = avatarVoice.avatarurl,
#                 card_flag = avatarVoice.cardflag,disable = avatarVoice.disable, gender = avatarVoice.gender, name = avatarVoice.name,
#                                      voice_number = avatarVoice.voice_number,voice_url = avatarVoice.voiceurl)
#         session2.add(avatarVoiceV2)
#         session2.commit()
#         userV2 = UserV2(birthday=user.birthday, certification=user.certification, degree=user.degree,
#                         department=user.department,
#                         enrollment=user.enrollment, gender=user.gender, hobby=user.hobby, hometown=user.hometown,
#                         look_count=user.lookcount,
#                         name=user.name, password=user.password, phone=user.phone, preference=user.preference, qq=user.qq,
#                         school=user.school, tags=user.tags, token=user.token, username=user.username, wechat=user.wechat,
#                         weme=user.weme, old_id=user.id,avatar_voice=avatarVoiceV2.id)
#         session2.add(userV2)
#         session2.commit()
#     else:
#         userV2 = UserV2(birthday=user.birthday, certification=user.certification, degree=user.degree,
#                         department=user.department,
#                         enrollment=user.enrollment, gender=user.gender, hobby=user.hobby, hometown=user.hometown,
#                         look_count=user.lookcount,
#                         name=user.name, password=user.password, phone=user.phone, preference=user.preference,
#                         qq=user.qq,
#                         school=user.school, tags=user.tags, token=user.token, username=user.username,
#                         wechat=user.wechat,
#                         weme=user.weme, old_id=user.id)
#         session2.add(userV2)
#         session2.commit()
#
# print "finish transfer table User AvatarVoices"
#
# print "***************************3******************************"
#
#
# print "strat transfer talbe Avtivity "
# query = session2.query(UserV2)
# for user in query:
#     #关联avatarvoice
#     activitytemp = session1.query(Activity).filter_by(authorid=user.old_id).all()
#     if activitytemp is not None:
#         for activity in activitytemp:
#             activityV2 =ActivityV2(advertise = activity.advertise,detail = activity.detail,disable = activity.disable,
#                     label = activity.label,location = activity.location, number = activity.number, pass_flag = activity.passflag,
#                     remark = activity.remark,signnumber = activity.signnumber,sponser = activity.sponsor,state = activity.state,
#                     time = activity.time,timestamp=activity.timestamp,title =activity.title,top =activity.top,
#                     whether_image = activity.whetherimage,author_id = user.id,old_id =activity.id)
#             session2.add(activityV2)
#
#     else:
#         continue
# session2.commit()
# print "finish transfer table Activity"
#
#
#
#
# print "***************************4******************************"
#
# print "strat transfer talbe AvtivityImage "
#
# query = session2.query(ActivityV2)
# for activityV2 in query:
#     #关联avatarvoice
#     activityimagetemp = session1.query(ActivityImage).filter_by(activityid=activityV2.old_id).all()
#     if activityimagetemp is not None:
#         for activityimage in activityimagetemp:
#             url  = "http://218.244.147.240:80/activity/activityimages/"+str(activityimage.activityid)+"-"+str(activityimage.imageid)
#             activityimagev2 =ActivityImageV2(thumbnail_url = url,url = url,timestamp= activityimage.timestamp,activity_id = activityV2.id)
#             session2.add(activityimagev2)
#     else:
#         continue
# session2.commit()
# print "finish transfer table AvtivityImage"
#
# print "***************************5******************************"
#
# print "strat transfer talbe AndroidVersion "
#
# query = session1.query(AndroidVersions)
# for androidVersion in query:
#     #关联avatarvoice
#     androidVersionV2 = AndroidVersionsV2(disable=androidVersion.disable,timestamp = androidVersion.timestamp,v1 = androidVersion.v1,
#         v2 = androidVersion.v2,v3=androidVersion.v3,wemeurl = androidVersion.wemeurl)
#     session2.add(androidVersionV2)
# session2.commit()
# print "finish transfer table AndroidVersion"
#
#
#
# print "***************************6******************************"
#
# print "strat transfer talbe checkMsgs "
#
# query = session1.query(CheckMsgs)
# for checkMsg in query:
#     #关联avatarvoice
#     checkMsgV2 = CheckMsgsV2(code=checkMsg.code,phone = checkMsg.phone,timestamp = checkMsg.timestamp,old_id = checkMsg.id)
#     session2.add(checkMsgV2)
# session2.commit()
# print "finish transfer table checkMsgs"
#
# print "***************************7******************************"
# print "strat transfer talbe post "
#
# query = session1.query(Post)
# for post in query:
#   #关联avatarvoice
#   tempuser = session2.query(UserV2).filter_by(old_id =post.authorid).first()
#   temptopic = session2.query(TopicV2).filter_by(old_id = post.topicid).first()
#   if tempuser is not None and temptopic is not None:
#       postV2 = PostV2(body = post.body,disable = post.disable,timestamp = post.timestamp,title= post.title,top=post.top,publish_user_id = tempuser.id,
#                   topic_id= temptopic.id,old_id = post.id)
#       session2.add(postV2)
# session2.commit()
# print "finish transfer table post"
#
#
#
# print "***************************8******************************"
# print "strat transfer talbe topic and Image"
#
# query = session1.query(Topic)
# for topic in query:
#     #关联avatarvoice
#     topicV2 = TopicV2(note = topic.note,number = topic.number,rank = topic.rank,slogan = topic.slogan,
#                       theme = topic.theme,post_number = topic.postnumber,old_id = topic.id)
#     session2.add(topicV2)
#     session2.commit()
#     topicimage = TopicImageV2(disable =False,thumbnail_url=topic.imageurl,url = topic.imageurl,topic_id = topicV2.id)
#
#     session2.add(topicimage)
#     session2.commit()
#
# print "finish transfer table topic"
#
#
# print "***************************9******************************"
#
# print "strat transfer talbe likeuser "
#
# query = session1.query(LikeUser)
# for likeuser in query:
#     #关联avatarvoice
#     templikeuser = session2.query(UserV2).filter_by(old_id =likeuser.likeid).first()
#     templikeduser = session2.query(UserV2).filter_by(old_id = likeuser.likedid).first()
#     temp = LikeUserV2(timestamp = likeuser.timestamp,liked_id = templikeduser.id,liker_id=templikeuser.id)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table likeuser"
#
#
#
#
# print "***************************10******************************"
#
# print "strat transfer talbe foodcard "
#
# query = session1.query(FoodCard)
# for foodcard in query:
#     tempUser = session2.query(UserV2).filter_by(old_id = foodcard.authorid).first()
#     temp = FoodCardV2(comment = foodcard.comment,disable = foodcard.disable,image_url=foodcard.imageurl,location= foodcard.location,
#         longitude = foodcard.longitude ,latitude = foodcard.latitude ,price = foodcard.price,pass_flag= foodcard.passflag,title = foodcard.title,
#                     timestamp = foodcard.timestamp,author_id = tempUser.id,old_id = foodcard.id)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table foodcard"
#
# print "***************************11******************************"
#
# print "strat transfer talbe follow "
#
# query = session1.query(Follow)
# for follow in query:
#     tempfollower = session2.query(UserV2).filter_by(old_id = follow.follower_id).first()
#     tempfollowed = session2.query(UserV2).filter_by(old_id = follow.followed_id).first()
#     temp =FollowV2(timestamp= follow.timestamp,followed_id=tempfollowed.id,follower_id = tempfollower.id)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table follow"
#
#
# print "***************************12******************************"
# print "start transfer talbe user_attend_acitivity "
#
# query = session1.query(UserAttendAcitivity)
# for userattend in query:
#     tempactivity = session2.query(ActivityV2).filter_by(old_id = userattend.activityid).first()
#     tempuser = session2.query(UserV2).filter_by(old_id = userattend.userid).first()
#     temp =UserAttendActivityV2(user_id = tempuser.id,activity_id = tempactivity.id,timestamp = userattend.timestamp,state = userattend.state)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table user_attend_acitivity"
#
#
#
#
# print "***************************13******************************"
# print "start transfer talbe user image "
#
# query = session1.query(UserImage)
# for userimage in query:
#     tempuser = session2.query(UserV2).filter_by(old_id = userimage.userid).first()
#     temp =UserImageV2(user_id = tempuser.id,disable = userimage.disable,thumbnail_url = userimage.thumbnail_url,timestamp = userimage.timestamp,
#             url = userimage.url,old_id= userimage.id)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table user image"
#
#
# print "***************************14******************************"
# print "start transfer talbe user life image for activity"
#
# query = session1.query(UserLifeImage)
# for userlifeimage in query:
#     tempactivity = session2.query(ActivityV2).filter_by(old_id = userlifeimage.activityid).first()
#     tempuser = session2.query(UserV2).filter_by(old_id = userlifeimage.userid).first()
#     imageurl = session1.query(ImageUrls).filter_by(id=userlifeimage.imageid).first()
#     url = 'http://218.244.147.240:80/picture/activitylifeimages/' +str(userlifeimage.activityid)+'-'+str(userlifeimage.userid)+'-'+str(userlifeimage.imageid)
#     thumb =url+'_thumbnail.jpg'
#
#     temp =UserLifeImageV2(user_id = tempuser.id,thumbnail_url = thumb,timestamp = userlifeimage.timestamp,url =url,old_id= userlifeimage.id,
#                           disable=False,imageid= imageurl.number,activity_id=tempactivity.id)
#     session2.add(temp)
# session2.commit()
# print "finish transfer table user life image for activity"
#
#
# print "***************************15******************************"
# print "start transfer talbe user visit relation"
#
# query = session1.query(UserVisit)
# for uservisit in query:
#     tempvisiteduser = session2.query(UserV2).filter_by(old_id = uservisit.hostid).first()
#     tempvisitinguser = session2.query(UserV2).filter_by(old_id = uservisit.guestid).first()
#     temp = UserVisitV2(visited_id=tempvisiteduser.id,visiter_id=tempvisitinguser.id,timestamp=uservisit.timestamp )
#     session2.add(temp)
# session2.commit()
# print "finish transfer table user visit relation"

#
#
# print "***************************16******************************"
# print "start transfer talbe user like post"
#
# query = session1.query(UserLikePost)
# for userlikepost in query:
#
#     try:
#         temppost = session2.query(PostV2).filter_by(old_id=userlikepost.postid).first()
#         tempuser = session2.query(UserV2).filter_by(old_id=userlikepost.userid).first()
#         temp = UserLikePostV2(timestamp = userlikepost.timestamp,post_id=temppost.id,user_id=tempuser.id )
#         session2.add(temp)
#         session2.commit()
#     except Exception, e:
#         continue
#
# print "finish transfer table user like post"

#
# print "***************************17******************************"
# print "start transfer talbe user like food"
#
# query = session1.query(UserLikeFood)
# for userlikefood in query:
#
#     try:
#         tempfood = session2.query(FoodCardV2).filter_by(old_id=userlikefood.foodcardid).first()
#         tempuser = session2.query(UserV2).filter_by(old_id=userlikefood.userid).first()
#         temp = UserLikeFoodV2(timestamp = userlikefood.timestamp,foodcard_id=tempfood.id,user_id=tempuser.id )
#         session2.add(temp)
#         session2.commit()
#     except Exception,e:
#         session2.rollback()
#         continue
#
# print "finish transfer table user like food"

# print "***************************18******************************"
# print "start transfer talbe user like activity"
#
# query = session1.query(UserLikeActivity)
# for userlikeactivity in query:
#     try:
#         tempactivity = session2.query(ActivityV2).filter_by(old_id=userlikeactivity.activityid).first()
#         tempuser = session2.query(UserV2).filter_by(old_id=userlikeactivity.userid).first()
#         temp = UserLikeActivityV2(timestamp = userlikeactivity.timestamp,activity_id=tempactivity.id,user_id=tempuser.id )
#         session2.add(temp)
#         session2.commit()
#     except Exception,e:
#         continue
#
# print "finish transfer table user like activity"
#

# print "***************************19******************************"
# print "start transfer talbe comment"
#
# queryAct = session1.query(CommentAct)
# queryPost = session1.query(CommentPost)
# for commentact in queryAct:
#     tempactivity = session2.query(ActivityV2).filter_by(old_id=commentact.activityid).first()
#     tempuser = session2.query(UserV2).filter_by(old_id=commentact.authorid).first()
#     hasimage = session1.query(CommentActImageAttach).filter_by(commentid=commentact.id).first()
#     if hasimage is not None:
#         hasimage = True
#     else:
#         hasimage =False
#
#     to_user_id = None
#     if commentact.commentid != -1:
#         tempcomment = session1.query(CommentAct).filter_by(id=commentact.commentid).first()
#         to_user_id = session2.query(UserV2).filter_by(old_id = commentact.authorid).first()
#         to_user_id = to_user_id.id
#
#     tempCommentId =None
#     if commentact.commentid !=-1:
#         newComment = session2.query(CommentV2).filter_by(old_id=commentact.commentid).first()
#         tempCommentId =newComment.id
#
#
#
#     temp = CommentV2(timestamp = commentact.timestamp,content=commentact.body,has_image = hasimage,state = True,
#         type = 1,activity_id=tempactivity.id,authoruser_id=tempuser.id,comment_id=tempCommentId,to_user_id=to_user_id,old_id=commentact.id)
#     session2.add(temp)
#
#
#
# print "-----------------------------------"
#
# for commentpost in queryPost:
#
#     temppost = session2.query(PostV2).filter_by(old_id =commentpost.postid).first()
#     tempauthoruser = session2.query(UserV2).filter_by(old_id=commentpost.authorid).first()
#     hasimage = session1.query(CommentPostImageAttach).filter_by(commentid= commentpost.id).first()
#     if hasimage is not None:
#         hasimage = True
#     else:
#         hasimage = False
#
#     to_user_id =None
#     if commentpost.commentid !=-1:
#         tempcomment = session1.query(CommentPost).filter_by(id=commentpost.commentid).first()
#         to_user_id = session2.query(UserV2).filter_by(old_id =tempcomment.authorid).first()
#         to_user_id = to_user_id.id
#
#     tempCommentId =None
#     if commentact.commentid !=-1:
#         newComment = session2.query(CommentV2).filter_by(old_id=commentpost.commentid).first()
#         tempCommentId =newComment.id
#
#
#     temp = CommentV2(timestamp =commentpost.timestamp,content= commentpost.body,has_image=hasimage,state = commentpost.readflag,
#         type = 0,post_id =temppost.id,
#                      authoruser_id=tempauthoruser.id,
#                      comment_id=tempCommentId,to_user_id=to_user_id,old_id= commentpost.id)
#     session2.add(temp)
# session2.commit()
#
#
# print "finish transfer table comment"
#
# print "***************************20******************************"
# print "start transfer talbe commentimage"
#
# queryActImage = session1.query(CommentActImageAttach)
# queryPostImage = session1.query(CommentPostImageAttach)
# for queryactimage in queryActImage:
#     tempactcomment = session1.query(CommentAct).filter_by(id=queryactimage.commentid).first()
#     url ="http://218.244.147.240/activity/commentactsImage/"+str(tempactcomment.activityid)+'-'+str(queryactimage.commentid)+'-'+str(queryactimage.imageid)
#     thumb = url +"_thumbnail.jpg"
#     nowcomment = session2.query(CommentV2).filter_by(old_id=tempactcomment.id).filter_by(type=1).first()
#     temp = CommentImageV2(disable=False,thumbnail_url =thumb,url = url,timestamp = queryactimage.timestamp,comment_id= nowcomment.id)
#     session2.add(temp)
#
#
#
# print "-----------------------------------"
#
# for querypostimage in queryPostImage:
#     temppostcomment = session1.query(CommentPost).filter_by(id=querypostimage.commentid).first()
#     temppost = session1.query(Post).filter_by(id=temppostcomment.postid).first()
#     url ="http://218.244.147.240/community/commentattachs/"+str(temppost.topicid)+'-'+str(querypostimage.commentid)+'-'+str(querypostimage.imageid)
#     thumb = url +"_thumbnail.jpg"
#     nowcomment = session2.query(CommentV2).filter_by(old_id=temppostcomment.id).filter_by(type=0).first()
#     temp = CommentImageV2(disable=False,thumbnail_url =thumb,url = url,timestamp = querypostimage.timestamp,comment_id= nowcomment.id)
#     session2.add(temp)
#
# session2.commit()
#
# print "finish transfer table commentimage"

#
# print "***************************21******************************"
#
# print "strat transfer talbe Report"
#
# query = session1.query(Report)
# for  report in query:
#     typeflag = 0
#     if report.type =='user':
#         typeflag = 0
#     elif report.type == 'post':
#         typeflag = 1
#     elif report.type == 'activity':
#         typeflag = 2
#     else:
#         typeflag = 3
#
#     user = session2.query(UserV2).filter_by(old_id = report.authorid).first()
#
#     reportV2 = ReportV2(be_reported_id = None,body = report.body,timestamp = report.timestamp,type = typeflag,
#         authoruser_id = user.id,typeid = report.typeid)
#     session2.add(reportV2)
# session2.commit()
#
# print "finish transfer table Report"
#
#
# print "***************************22******************************"
#
# print "strat transfer talbe postimage"
# query = session1.query(PostImage)
# for postimage in query:
#     post = session1.query(Post).filter_by(id =postimage.postid).first()
#     user = session2.query(UserV2).filter_by(old_id = post.authorid).first()
#     url = "http://218.244.147.240/community/postattachs/"+str(post.topicid)+'-'+str(postimage.postid)+'-'+str(postimage.imageid)
#     thumb = url+"_thumbnail.jpg"
#     nowpost = session2.query(PostV2).filter_by(old_id=post.id).first()
#     postimageV2 = PostImageV2(disable = False,thumbnail_url =thumb,timestamp = postimage.timestamp,url = url,post_id =nowpost.id)
#     session2.add(postimageV2)
# session2.commit()
#
# print "finish transfer table postimage"
#
#
# print "***************************23******************************"
#
# print "strat transfer talbe activity Poster Image"
# query = session1.query(ActivityPosterImage)
# for posterimage in query:
#     activity = session2.query(ActivityV2).filter_by(old_id = posterimage.activityid).first()
#     tempposter = PosterImageV2(disable = False,thumbnail_url=posterimage.imageurl,url= posterimage.imageurl,activity_id = activity.id,rank = posterimage.rank)
#     session2.add(tempposter)
# session2.commit()
#
# print "finish transfer table activity Poster Image"
#
#
#
# print "***************************24******************************"
#
# print "strat transfer talbe message"
# query = session1.query(Message)
# for message in query:
#     messageimage = session1.query(MessageImage).filter_by(message_id = message.id).first()
#     hasimage = False
#     if MessageImage is not None:
#         hasimage = True
#     nowsend = session2.query(UserV2).filter_by(old_id=message.sendid).first()
#     nowrec = session2.query(UserV2).filter_by(old_id = message.recid).first()
#     if nowsend is None or nowrec is None:
#         continue
#     tempmessagev2 = MessageV2(has_image= hasimage,state=message.state,text= message.text,timestamp  = message.sendtime,
#                            sendfrom_id = nowsend.id,
#                               sendto_id=nowrec.id,old_id = message.id)
#     session2.add(tempmessagev2)
# session2.commit()
#
# print "finish transfer table message"
#
# print "***************************25******************************部分数据无法导出"
# print "start transfer table message image"
# query = session1.query(MessageImage)
# for messageimage in query:
#     try:
#         url="http://218.244.147.240/message/image/"+str(messageimage.message_id)+'-'+str(messageimage.image_id)
#         thumb= url+"_thumbnail.jpg"
#         tempmessage = session2.query(MessageV2).filter_by(old_id = messageimage.message_id).first()
#
#         tempimagev2 = MessageImageV2(disable=False,thumbnail_url = thumb,url=url,message_id =tempmessage.id)
#         session2.add(tempimagev2)
#         session2.commit()
#     except Exception, e:
#         continue
#
#
# print "finish transfer table message image"


# print "***************************26******************************"
# print "start transfer table community poster image"
# query = session1.query(CommunityPosterImage)
# for temp in query:
#     tempPost = session2.query(PostV2).filter_by(old_id=temp.postid).first()
#     communtyposterv2 = CommunityPosterImageV2(disable = False,thumbnail_url = temp.imageurl,url = temp.imageurl,rank =temp.rank,post_id = tempPost.id)
#     session2.add(communtyposterv2)
# session2.commit()
# print "finish transfer table community poster image"

print "***************************27******************************"
print "start transfer table user like relation"
query = session1.query(UserLikeComment)
for temp in query:
    tempComment = session2.query(CommentV2).filter_by(old_id=temp.commentid).first()
    tempUser = session2.query(UserV2).filter_by(old_id = temp.userid).first()
    userlikecomment  = UserLikeCommentV2(timestamp = temp.timestamp,comment_id=tempComment.id,user_id = tempUser.id)
    session2.add(userlikecomment)
session2.commit()
print "finish transfer table user like relation"
