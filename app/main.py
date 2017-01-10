# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME
from sqlalchemy.ext.declarative import declarative_base

from model import *
from modelV2 import  *
ORIGINAL_DB_CONNECT_STRING = 'mysql+mysqldb://root:SEUqianshou2015@218.244.147.240:3306/flasktestdb?charset=utf8'
New_DB_CONNECT_STRING ='mysql+mysqldb://root:qwer@localhost/weme?charset=utf8'


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
# 9. comment 评论
# 10. comment_image 评论图片
# 11. follow_id 关注 ok
# 12. foodcard 食物照片 ok
# 13. like_user_id 喜欢关系  ok
# 14. message消息
# 15. message_image 图片消息
# 16. post_image 文章图片
# 17. poseter_image 海报照片
# 18. Report 举报
# 19. topic_image 话题照片
# 20. user_attend_activity_realtion 用户参加活动关系 ok
# 21. user_image 用户照片 ok
# 22. user_like_activity_relation 用户喜欢关系表
# 23. user_like_foodcard  用户食物卡片喜欢关系
# 24. user_like_post  用户文章喜欢关系
# 25. user_visit 用户访问关系  ok
# 26. activity_life_image 用户生活照 ok
#



# for report in query:
#     print report.id
#     print report.authorid
#     print report.body
#     print report.type
#     print report.typeid
#     print report.timestamp

# print "strat transfer talbe avatarVoice"
# query =session1.query(AvatarVoice)
# for avatarVoice in query:
#     avatatVoiceV2 =AvatarVoiceV2(avatar_number=avatarVoice.avatar_number,avatar_url=avatarVoice.avatarurl,
#             card_flag=avatarVoice.cardflag,disable=avatarVoice.disable,gender=avatarVoice.gender,name=avatarVoice.name,
#                                  voice_number =avatarVoice.voice_number,voice_url=avatarVoice.voiceurl)
#     session2.add(avatatVoiceV2)
# session2.commit()
# print "finish transfer table avatarVoice"

# user.old_id 补充对应的主键的信息

#   *****************12**************************

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

#***************************3******************************


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




#***************************4******************************

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

#***************************5******************************

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



#***************************6******************************

# print "strat transfer talbe checkMsgs "
#
# query = session1.query(CheckMsgs)
# for checkMsg in query:
#     #关联avatarvoice
#     checkMsgV2 = CheckMsgsV2(code=checkMsg.code,phone = checkMsg.phone,timestamp = checkMsg.timestamp,old_id = checkMsg.id)
#     session2.add(checkMsgV2)
# session2.commit()
# print "finish transfer table checkMsgs"


#***************************7******************************

# print "strat transfer talbe topic "
#
# query = session1.query(Topic)
# for topic in query:
#     #关联avatarvoice
#     topicV2 = TopicV2(image_url=topic.imageurl,note = topic.note,number = topic.number,rank = topic.rank,slogan = topic.slogan,
#                       theme = topic.theme,postnumber = topic.postnumber,old_id = topic.id)
#     session2.add(topicV2)
# session2.commit()
# print "finish transfer table topic"

#***************************8******************************

# print "strat transfer talbe post "
#
# query = session1.query(Post)
# for post in query:
#     #关联avatarvoice
#     tempuser = session2.query(UserV2).filter_by(old_id =post.authorid).first()
#     temptopic = session2.query(TopicV2).filter_by(old_id = post.topicid).first()
#     if tempuser is not None and temptopic is not None:
#         postV2 = PostV2(body = post.body,disable = post.disable,timestamp = post.timestamp,title= post.title,top=post.top,publish_user_id = tempuser.id,
#                     topic_id= temptopic.id,old_id = post.id)
#         session2.add(postV2)
# session2.commit()
# print "finish transfer table post"

#***************************9******************************

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


#***************************10******************************

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




#***************************10******************************
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

#***************************11******************************

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


#***************************11******************************
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


#***************************12******************************
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



#***************************12******************************
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



#***************************13******************************
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


#***************************14******************************
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


#***************************15******************************
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



#***************************16******************************
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


#***************************16******************************
print "start transfer talbe user like post"

query = session1.query(UserLikePost)
for userlikepost in query:

    try:
        temppost = session2.query(PostV2).filter_by(old_id=userlikepost.postid).first()
        tempuser = session2.query(UserV2).filter_by(old_id=userlikepost.userid).first()
        temp = UserLikePostV2(timestamp = userlikepost.timestamp,post_id=temppost.id,user_id=tempuser.id )
        session2.add(temp)
        session2.commit()
    except Exception, e:
        continue

print "finish transfer table user like post"
