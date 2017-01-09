# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME,BigInteger,BOOLEAN
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

# class ReportV2(BaseModel):
#     __tablename__ = 'reports'
#
#     id = Column(Integer, primary_key=True)
#     authorid = Column(Integer)
#     body = Column(TEXT)
#     type = Column(VARCHAR)
#     typeid = Column(Integer)
#     timestamp = Column(DATETIME)

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
    image_url = Column(VARCHAR)
    note = Column(VARCHAR)
    number = Column(Integer)
    rank = Column(Integer)
    slogan = Column(VARCHAR)
    theme = Column(VARCHAR)
    timestamp = Column(DATETIME)
    postnumber = Column(Integer)
    old_id = Column(BigInteger)

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



