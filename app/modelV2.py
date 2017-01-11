# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME,BigInteger,BOOLEAN
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()



class AvatarVoiceV2(BaseModel):
    __tablename__='t_avatar_voice'
    id = Column(BigInteger,primary_key=True)
    avatar_number = Column(Integer)
    avatar_url = Column(VARCHAR)
    card_flag = Column(BOOLEAN)
    disable = Column(BOOLEAN)
    gender = Column(VARCHAR)
    name = Column(VARCHAR)
    voice_number = Column(Integer)
    voice_url =Column(VARCHAR)






class UserV2(BaseModel):
    __tablename__='t_user'
    id = Column(BigInteger,primary_key=True)
    birthday = Column(VARCHAR)
    certification = Column(BOOLEAN,default=False)
    degree = Column(VARCHAR)
    department = Column(VARCHAR)
    enrollment = Column(VARCHAR)
    gender = Column(VARCHAR)
    hobby = Column(VARCHAR)
    hometown = Column(VARCHAR)
    latest_login_time = Column(DATETIME)
    look_count = Column(Integer)
    name = Column(VARCHAR)
    password = Column(VARCHAR)
    phone = Column(VARCHAR)
    preference = Column(VARCHAR)
    qq = Column(VARCHAR)
    salt = Column(VARCHAR)
    school = Column(VARCHAR)
    tags = Column(LONGTEXT)
    timestamp = Column(DATETIME)
    token = Column(VARCHAR)
    username = Column(VARCHAR)
    wechat = Column(VARCHAR)
    weme = Column(VARCHAR)
    avatar_voice = Column(BigInteger)
    old_id = Column(BigInteger)


class ActivityV2(BaseModel):
    __tablename__='t_activity'
    id=Column(BigInteger,primary_key=True)
    advertise = Column(VARCHAR)
    detail = Column(LONGTEXT)
    disable = Column(BOOLEAN,default=False)
    label = Column(VARCHAR)
    location = Column(VARCHAR)
    number = Column(VARCHAR)
    pass_flag = Column(Integer)
    remark = Column(VARCHAR)
    signnumber = Column(Integer)
    sponser = Column(VARCHAR)
    state = Column(BOOLEAN)
    time = Column(VARCHAR)
    timestamp = Column(DATETIME)
    title = Column(VARCHAR)
    top = Column(VARCHAR)
    whether_image = Column(BOOLEAN)
    author_id = Column(BigInteger)
    old_id =Column(BigInteger)


class ActivityImageV2(BaseModel):
    __tablename__='t_activity_image'
    id= Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN,default=False)
    thumbnail_url= Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    activity_id = Column(BigInteger)


class AndroidVersionsV2(BaseModel):
    __tablename__='t_android_version'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN,default=False)
    timestamp = Column(DATETIME)
    v1 = Column(Integer)
    v2 = Column(Integer)
    v3 = Column(Integer)
    wemeurl =Column(VARCHAR)


class CheckMsgsV2(BaseModel):
    __tablename__='t_check_msg'
    id =Column(BigInteger,primary_key=True)
    code = Column(VARCHAR)
    phone = Column(VARCHAR)
    timestamp  = Column(DATETIME)
    old_id = Column(BigInteger)


class TopicV2(BaseModel):
    __tablename__='t_topic'
    id = Column(BigInteger,primary_key=True)
    note = Column(VARCHAR)
    number = Column(Integer)
    rank = Column(Integer)
    slogan = Column(VARCHAR)
    theme = Column(VARCHAR)
    timestamp = Column(DATETIME)
    postnumber = Column(Integer)
    old_id = Column(BigInteger)

class TopicImageV2(BaseModel):
    __tablename__='t_topic_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    topic_id = Column(VARCHAR)



class PostV2(BaseModel):

    __tablename__='t_post'
    id = Column(BigInteger,primary_key=True)
    title = Column(VARCHAR)
    body = Column(LONGTEXT)
    timestamp = Column(DATETIME)
    publish_user_id = Column(Integer)
    topic_id = Column(Integer)
    top = Column(Integer)
    disable = Column(BOOLEAN)
    old_id = Column(BigInteger)


class LikeUserV2(BaseModel):
    __tablename__='t_like_user_relation'
    id =Column(BigInteger,primary_key=True)
    timestamp = Column(DATETIME)
    liked_id = Column(BigInteger)
    liker_id = Column(BigInteger)

class FoodCardV2(BaseModel):
    __tablename__='t_foodcard'
    id = Column(BigInteger,primary_key=True)
    comment = Column(VARCHAR)
    disable =  Column(BOOLEAN)
    image_url = Column(VARCHAR)
    location = Column(VARCHAR)
    latitude = Column(VARCHAR)
    longitude = Column(VARCHAR)
    pass_flag = Column(BOOLEAN)
    price = Column(VARCHAR)
    timestamp = Column(DATETIME)
    title = Column(VARCHAR)
    author_id = Column(BigInteger)
    old_id = Column(BigInteger)


class FollowV2(BaseModel):
    __tablename__='t_follow_relation'
    id = Column(BigInteger,primary_key=True)
    timestamp = Column(DATETIME)
    followed_id = Column(BigInteger)
    follower_id = Column(BigInteger)

class UserAttendActivityV2(BaseModel):
    __tablename__='t_user_attend_activity_relation'
    id = Column(BigInteger,primary_key=True)
    state = Column(Integer)
    timestamp = Column(DATETIME)
    activity_id = Column(BigInteger)
    user_id = Column(BigInteger)

class UserImageV2(BaseModel):
    __tablename__='t_user_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    user_id = Column(BigInteger)
    old_id = Column(BigInteger)

class UserLifeImageV2(BaseModel):
    __tablename__='t_activity_life_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    imageid = Column(BigInteger)
    activity_id=Column(BigInteger)
    user_id = Column(BigInteger)
    old_id = Column(BigInteger)

class UserVisitV2(BaseModel):
    __tablename__='t_user_visit_relation'
    id = Column(BigInteger,primary_key=True)
    timestamp = Column(DATETIME)
    visited_id = Column(BigInteger)
    visiter_id = Column(BigInteger)

class UserLikePostV2(BaseModel):
    __tablename__='t_user_like_post_relation'
    id = Column(BigInteger,primary_key=True)
    timestamp = Column(DATETIME)
    post_id = Column(BigInteger)
    user_id = Column(BigInteger)

class UserLikeFoodV2(BaseModel):
    __tablename__='t_user_like_foodcard'
    id = Column(BigInteger,primary_key=True)
    foodcard_id = Column(BigInteger)
    user_id = Column(BigInteger)
    timestamp = Column(DATETIME)


class UserLikeActivityV2(BaseModel):
    __tablename__='t_user_like_activity_relation'
    id = Column(BigInteger,primary_key=True)
    activity_id = Column(BigInteger)
    user_id = Column(BigInteger)
    timestamp = Column(DATETIME)

class CommentV2(BaseModel):
    __tablename__='t_comment'
    id = Column(BigInteger,primary_key=True)
    content = Column(LONGTEXT)
    has_image = Column(BOOLEAN)
    state = Column(BOOLEAN)
    timestamp = Column(DATETIME)
    type = Column(Integer)
    activity_id = Column(BigInteger)
    authoruser_id= Column(BigInteger)
    comment_id = Column(BigInteger)
    post_id = Column(BigInteger)
    to_user_id = Column(BigInteger)
    old_id = Column(BigInteger)

class CommentImageV2(BaseModel):
    __tablename__='t_comment_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    comment_id = Column(BigInteger)

class ReportV2(BaseModel):
    __tablename__ = 't_report'
    id = Column(BigInteger, primary_key=True)
    be_reported_id = Column(BigInteger)
    body = Column(LONGTEXT)
    type = Column(Integer)
    authoruser_id = Column(BigInteger)
    timestamp = Column(DATETIME)
    type_id = Column(Integer)

class PostImageV2(BaseModel):
    __tablename__ = 't_post_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    post_id = Column(BigInteger)


class PosterImageV2(BaseModel):
    __tablename__='t_activity_poster_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    activity_id = Column(BigInteger)
    rank = Column(Integer)

class MessageV2(BaseModel):
    __tablename__='t_message'
    id =Column(BigInteger,primary_key=True)
    has_image = Column(BOOLEAN)
    state = Column(BOOLEAN)
    text = Column(TEXT)
    timestamp = Column(DATETIME)
    sendfrom_id = Column(BigInteger)
    sendto_id = Column(BigInteger)
    old_id = Column(BigInteger)

class MessageImageV2(BaseModel):
    __tablename__='t_message_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    message_id = Column(BigInteger)


class CommunityPosterImageV2(BaseModel):
    __tablename__='t_community_poster_image'
    id = Column(BigInteger,primary_key=True)
    disable = Column(BOOLEAN)
    thumbnail_url = Column(VARCHAR)
    timestamp = Column(DATETIME)
    url = Column(VARCHAR)
    rank = Column(Integer)
    post_id = Column(BigInteger)





